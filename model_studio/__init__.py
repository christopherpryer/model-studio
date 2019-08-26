from flask import Flask
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
import click
import os

db = SQLAlchemy()
from . import models

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

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @click.command('init-db')
    @with_appcontext
    def init_db_command():
        # clear existing data + create new tables
        db.create_all()
        db.session.commit()
        click.echo('Initialized the database.')

    app.cli.add_command(init_db_command)

    from .dashboards import main
    app = main.Add_Routes_App(app)

    return app
