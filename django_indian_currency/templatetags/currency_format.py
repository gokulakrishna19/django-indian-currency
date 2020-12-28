
from django import template

from . import utils


register = template.Library()

def indian_currency(amount, keep_decimal=True):
    return utils.indian_currency(amount, keep_decimal=keep_decimal)


def indian_word_currency(amount, keep_decimal=True):
    return utils.indian_word_currency(amount, keep_decimal=keep_decimal)


register.filter('indian_currency', indian_currency)
register.filter('indian_word_currency', indian_word_currency)