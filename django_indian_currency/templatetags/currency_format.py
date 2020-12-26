
from django import template

from . import utils


register = template.Library()

def indian_currency(amount, keep_decimal=True):
    return utils.indian_currency(amount, keep_decimal=keep_decimal)

register.filter('indian_currency', indian_currency)