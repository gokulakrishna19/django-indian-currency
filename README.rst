=============================
django-indian-currency
=============================

.. image:: https://badge.fury.io/py/django-indian-currency.svg
    :target: https://badge.fury.io/py/django-indian-currency

.. image:: https://travis-ci.org/sgokulakrishna19/django-indian-currency.svg?branch=master
    :target: https://travis-ci.org/sgokulakrishna19/django-indian-currency

.. image:: https://codecov.io/gh/sgokulakrishna19/django-indian-currency/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/sgokulakrishna19/django-indian-currency

Convert float/int to indian currency format

Documentation
-------------

The full documentation is at https://django-indian-currency.readthedocs.io.

Quickstart
----------

Install django-indian-currency::

    pip install django-indian-currency

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
