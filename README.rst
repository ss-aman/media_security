==============
Media Security
==============

Media Security is a Django App, to put restrications of public accessing of media
files from, after employing Media Security App, media files of model(registered models
for media security) would be accessible only by the user who put those files.

How To Use
----------

1. Add "media_security" to INSTALLED_APPS ::

    INSTALLED_APPS = [
        ...
        "media_security",
    ]

2. Remove url for media files serving if exists in projects urls.py file.

3. Add "media_security.urls" to projects urls.py file urlpatterns path::

    path('', include('media_security.urls')),

4. Run `python manage.py migrate` to create the models for "media_security".

5. Register Models for Media Security in settings.py file::

    MEDIA_SECURITY_MODEL = [
        '<app_mame_1>.<model_name_1>',
        '<app_mame_2>.<model_name_2>',
        '<app_mame_3>.<model_name_3>',
        ...
        ...
        ]
