# Automatic ep.io launcher. This will configure some stuff for your app.
# Note that this assumes it is in the same directory as your epio.ini.

import os
from bundle_config import config as service_config
from ConfigParser import ConfigParser   # ...I hate that name
from os.path import join, dirname
from werkzeug.utils import import_string

EPIO_INI = join(dirname(__file__), "epio.ini")

config = ConfigParser()
config.read(EPIO_INI)

factory_path = config.get("launcher", "package") + ":create_app"
factory = import_string(factory_path)

if config.has_option("launcher", "config_file"):
    config_file = config.get("launcher", "config_file")
else:
    config_file = None

extras = {}

has_service = lambda svc: (config.has_option("services", svc) and
                           config.getboolean("services", svc))

if (config.has_option("launcher", "use_epio_secret") and
    config.getboolean("launcher", "use_epio_secret")):
    extras["SECRET_KEY"] = service_config['core']['secret_key']

if has_service("postgres"):
    extras['SQLALCHEMY_DATABASE_URI'] = (
        "postgresql://%(username)s:%(password)s@%(host)s:%(port)s/%(database)s"
        % service_config['postgres']
    )

if has_service("redis"):
    extras["REDIS_HOST"] = service_config['redis']['host']
    extras["REDIS_PORT"] = service_config['redis']['port']
    extras["REDIS_PASSWORD"] = service_config['redis']['password']

app = factory(config_file, extras)
