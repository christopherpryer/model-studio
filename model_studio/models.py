# TODO: token authentication & session management
from flask import abort, g
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import os

from . import db
from .utils import timestamp, url_for

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Integer, default=timestamp)
    updated_at = db.Column(db.Integer, default=timestamp, onupdate=timestamp)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(10), nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        self.token = None  # if user is changing passwords, also revoke token

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def create(data):
        user = User()
        user.from_dict(data, partial_update=False)
        return user

    def from_dict(self, data, partial_update=True):
        for field in ['email', 'password']:
            try:
                setattr(self, field, data[field])
            except KeyError:
                if not partial_update:
                    abort(400)

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'email': self.email,
            'role': self.role
        }

    def has_role(self, role):
        return role == self.role

class Shipment(db.Model):
    __tablename__ = 'shipments'
    id = db.Column(db.String(255), primary_key=True)
    route_id = db.Column(db.String(255))
    stop_id = db.Column(db.String(255))
    order_id = db.Column(db.String(255))
    load_id = db.Column(db.String(255))
    sku_id = db.Column(db.String(255))
    origin_id = db.Column(db.String(255))
    origin_city = db.Column(db.String(50))
    origin_state = db.Column(db.String(50))
    origin_zip = db.Column(db.String(10))
    origin_country = db.Column(db.String(50))
    dest_id = db.Column(db.String(255))
    dest_city = db.Column(db.String(50))
    dest_state = db.Column(db.String(50))
    dest_zip = db.Column(db.String(10))
    dest_country = db.Column(db.String(50))
    demand = db.Column(db.Float)
    demand_uom = db.Column(db.String(50))
