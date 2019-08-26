import os
from flask import Flask
from flask_assets import Environment, Bundle

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load instance config if it exists when not testing
        app.config.from_object('config.Config')
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    less_bundle = Bundle('less/*.less',
                         filters='less,cssmin',
                         output='dist/css/styles.css',
                         extra={'rel': 'stylesheet/less'})
    js_bundle = Bundle('js/*.js',
                       filters='jsmin',
                       output='dist/js/main.js')
    assets.register('less_all', less_bundle)
    assets.register('js_all', js_bundle)

    from .dashboards import main
    app = main.Add_Routes_App(app)

    return app
