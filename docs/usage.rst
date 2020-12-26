=====
Usage
=====

To use django-indian-currency in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_indian_currency.apps.DjangoIndianCurrencyConfig',
        ...
    )

Add django-indian-currency's URL patterns:

.. code-block:: python

    from django_indian_currency import urls as django_indian_currency_urls


    urlpatterns = [
        ...
        url(r'^', include(django_indian_currency_urls)),
        ...
    ]
