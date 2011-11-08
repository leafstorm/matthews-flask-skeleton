# -*- coding: utf-8 -*-
"""
myapp.application
=================
This is the main entry point for your app. It contains the app factory.

:copyright: (C) 2011, Matthew Frazier
:license:   MIT/X11, see LICENSE for details
"""
from flask import Flask
from .views import BLUEPRINTS

def create_app(config=None, extras=None):
    # create application object
    app = Flask("myapp")
    
    # configure application
    app.config.from_object("myapp.defaults")
    if isinstance(config, dict):
        app.config.update(config)
    elif isinstance(config, str):
        app.config.from_pyfile(config)
    if isinstance(extras, dict):
        # extras is primarily for the use of the ep.io launcher
        app.config.update(extras)
    
    # setup extensions
    
    for blueprint in BLUEPRINTS:
        if isinstance(blueprint, tuple):
            app.register_blueprint(blueprint[0], url_prefix=prefix[1])
        else:
            app.register_blueprint(blueprint)
    
    # template utilities, etc.
    
    return app
