
import decimal


def add_decimal(amount):
    return '{0:.2f}'.format(amount)

def valiate_format(amount):

    if type(amount) == str:
        amount = float(amount.replace(",", ""))

    decimal_amount = decimal.Decimal(str(amount))
    if decimal_amount.as_tuple().exponent < -2:
        amount_string = str(abs(amount))
    else:
        amount_string = add_decimal(abs(amount))
    return amount_string

def split_decimal(amount_string):
    amount_list = amount_string.split(".")
    decimal_value = None
    if len(amount_list) > 1:
        decimal_value = amount_list[1]
    return amount_list[0], decimal_value
    

def indian_currency(amount, keep_decimal=True):
    
    """
    Convert a number into comma notation as per Indian number system.
    This function accepts integer, float. If keep_decimal is true, we 
    the decimal value will be be returned else decimal place will be ignored.
    Example:
        25 becomes 25
        121250.6 becomes 1,125.6
        25.675 becomes 25.675
        126500.25 becomes 1,26,500.25
        -126500.75 becomes -1,26,500.75
    :param amount: integer or float
    :param keep_decimal: boolean
    :return: String
    """
    if not amount:
        return 0.00
    
    amount_string = valiate_format(amount)
    neg = True if amount < 0 else False
    amount_string, decimal_value = split_decimal(amount_string)
    length = len(amount_string)
    if length <=3:
        if keep_decimal and decimal_value and int(decimal_value) > 0:
            return amount_string + "." + decimal_value
        return amount_string if not neg else "-" + amount_string
    
    index = length - 3
    start = -3
    end = -1

    result = amount_string[start:]
    while index > 0:
        start += -2
        end += -2
        result = amount_string[start:end] + "," + result
        index -= 2
        
    if keep_decimal and decimal_value and int(decimal_value) > 0:
        return result + "." + decimal_value
    return result if not neg else "-" + result


def indian_word_currency(value):
    """
    Converts a large integer number into a friendly text representation.
    Denominations used are: Hundred, Thousand, Lakh, Crore
    Examples:
        1000 becomes 1 Thousand
        15000 becomes 15 Thousands
        15600 becomes 15.60 Thousands
        100000 becomes 1 Lakh
        1125000 becomes 11.25 Lakhs
        10000000 becomes 1 Crore
        56482485 becomes 5.64 Crore
    :return: String
    """
    if isinstance(value, int) and value < 100:
        return str(value)
    if isinstance(value, float) and value < 99:
        return str(value)

    try:
        if isinstance(value, str):
            if '.' not in value and int(value) < 99:
                return value
            if float(value) < 99:
                return value
    except (ValueError, TypeError):
        return value

    value_integer = str(value).split('.')[0]
    value_len = len(value_integer)
    if value_len > 7:
        crores = value_integer[:-7]
        lakhs = value_integer[-7:-5]
        if crores == '1' and lakhs == '00':
            return '1 Crore'
        if lakhs == '00':
            return '%s Crores' % crores
        return '%s.%s Crores' % (crores, lakhs)
    elif value_len > 5:
        lakhs = value_integer[:-5]
        thousands = value_integer[-5:-3]
        if lakhs == '1' and thousands == '00':
            return '1 Lakh'
        if thousands == '00':
            return '%s Lakhs' % lakhs
        return '%s.%s Lakhs' % (lakhs, thousands)
    elif value_len > 3:
        thousands = value_integer[:-3]
        hundreds = value_integer[-3:-1]
        if thousands == '1' and hundreds == '00':
            return '1 Thousand'
        if hundreds == '00':
            return '%s Thousands' % thousands
        return '%s.%s Thousands' % (thousands, hundreds)
    else:
        hundreds = value_integer[:-2]
        tens_ones = value_integer[-2:]
        if hundreds == '1' and tens_ones == '00':
            return '1 Hundred'
        if tens_ones == '00':
            return '%s Hundreds' % hundreds
        return '%s.%s Hundreds' % (hundreds, tens_ones)