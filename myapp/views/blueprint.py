# -*- coding: utf-8 -*-
"""
myapp.views.blueprint
=====================
This is an example of how your blueprints would look.

:copyright: (C) 2011, Matthew Frazier
:license:   MIT/X11, see LICENSE for details
"""
import os
from flask import Blueprint, request, render_template

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/')
def index():
    return render_template("index.html")
