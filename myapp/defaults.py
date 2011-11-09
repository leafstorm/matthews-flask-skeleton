# -*- coding: utf-8 -*-
"""
myapp.defaults
==============
This contains the default settings for the application. (Copy this and delete
the header, and you can use it as a config file.)

:copyright: (C) 2011, Matthew Frazier
:license:   MIT/X11, see LICENSE for details
"""

#: Whether to run the application in debug mode or not. (Most of the time,
#: this should be `False`. Running this with `True` in production is a HUGE
#: security loophole.)
DEBUG = False

#: The secret key used to sign sessions. You can generate one with the command
#: ``python -c "import os; print(repr(os.urandom(20)))"``. Note that if you
#: are deploying on ep.io, leaving ``[launcher] use_epio_secret`` as true will
# use the secret key that ep.io generates for your app, so you don't have to
# add one yourself.
SECRET_KEY = 'Not actually secret'

#: The name of the cookie used to store user sessions.
SESSION_COOKIE_NAME = 'myapp_session'
