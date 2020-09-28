=============================
JB Django Zerodowntime
=============================

.. image:: https://badge.fury.io/py/dj-jb-zerodowntime.svg
    :target: https://badge.fury.io/py/dj-jb-zerodowntime

.. image:: https://travis-ci.org/berksonj/dj-jb-zerodowntime.svg?branch=master
    :target: https://travis-ci.org/berksonj/dj-jb-zerodowntime

.. image:: https://codecov.io/gh/berksonj/dj-jb-zerodowntime/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/berksonj/dj-jb-zerodowntime

Management commands to help Django users build & deploy their projects with low interruption for their users. This method is often called Zero Downtime Continous Delivery, or ZDCD.

Documentation
-------------

The full documentation is at https://dj-jb-zerodowntime.readthedocs.io.

Quickstart
----------

Install JB Django Zerodowntime::

    pip install dj-jb-zerodowntime

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_jb_zerodowntime.apps.DjJbZerodowntimeConfig',
        ...
    )

Add JB Django Zerodowntime's URL patterns:

.. code-block:: python

    from dj_jb_zerodowntime import urls as dj_jb_zerodowntime_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_jb_zerodowntime_urls)),
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
