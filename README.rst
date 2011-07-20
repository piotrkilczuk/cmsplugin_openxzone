======================
DjangoCMS OpenX Plugin
======================

Provides OpenX brigde for DjangoCMS. Allows user to embed OpenX zone as a block in the page.


Installation
============

First, install required django_openx using PIP:

  $> pip install -e git://github.com/hint/django-openx.git#egg=django_openx

Then install cmsplugin_openxzone using PIP:

  $> pip install -e git://github.com/centralniak/cmsplugin_openxzone.git#egg=cmsplugin_openxzone

Applications
------------

Register **cmsplugin_openxzone**, and these following applications in the INSTALLED_APPS section of your project's settings. ::

  >>> INSTALLED_APPS = (
  ...   # Your favorites apps
  ...   'cmsplugin_openxzone',)
  
Database 
--------

Run ./manage.py syncdb as usual.
