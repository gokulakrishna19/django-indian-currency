
import decimal


def add_decimal(amount):
    return '{0:.2f}'.format(amount)

def valiate_format(amount):

    if type(amount) == str:
        amount = float(amount.replace(",", ""))

    decimal_amount = decimal.Decimal(str(amount))
    if decimal_amount.as_tuple().exponent < -2:
        amount_string = str(amount)
    else:
        amount_string = add_decimal(amount)
    return amount_string

def split_decimal(amount_string):
    amount_list = amount_string.split(".")
    decimal_value = None
    if len(amount_list) > 1:
        decimal_value = amount_list[1]
    return amount_list[0], decimal_value
    

def indian_currency(amount, keep_decimal=True):
    if not amount:
        return 0.00
    
    amount_string = valiate_format(amount)
    amount_string, decimal_value = split_decimal(amount_string)
    length = len(amount_string)
    if length <=3:
        if keep_decimal and decimal_value and int(decimal_value) > 0:
            return amount_string + "." + decimal_value
        return amount_string
    
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
    return result