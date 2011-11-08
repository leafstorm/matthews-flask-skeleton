# -*- coding: utf-8 -*-
"""
myapp.manager
=============
This contains commands for the management script.

:copyright: (C) 2011, Matthew Frazier
:license:   MIT/X11, see LICENSE for details
"""
from flask import current_app
from flaskext.script import Manager
from .application import create_app

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)
