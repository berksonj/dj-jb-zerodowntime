=====
Usage
=====

To use JB Django Zerodowntime in a project, add it to your `INSTALLED_APPS`:

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
