# -*- coding: utf-8 -*-
"""
myapp.views
===========
This package contains all of the application's blueprints.

:copyright: (C) 2011, Matthew Frazier
:license:   MIT/X11, see LICENSE for details
"""
from .blueprint import blueprint

#: The items of `BLUEPRINTS` should either be actual `Blueprint` objects or
#: tuples of ``(blueprint, url_prefix)``.
BLUEPRINTS = (
    blueprint,
)
