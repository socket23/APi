from datetime import datetime

from malwear_api import db
from malwear_api.application.statuses import Status
from malwear_api.util import ModelUtil


class Application(db.Model, ModelUtil):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)

    address_line_one = db.Column(db.String(100), nullable=False)
    address_line_two = db.Column(db.String(100), nullable=False)
    address_city = db.Column(db.String(100), nullable=False)
    address_state = db.Column(db.String(20), nullable=False)
    address_zip = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    additional_info = db.Column(db.Text, nullable=True)
    income = db.Column(db.String(20), nullable=False)
    parent_name = db.Column(db.String(100), nullable=True)
    foster_child = db.Column(db.Boolean, default=False)
    status = db.Column(db.Integer, default=Status.SUBMITTED)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
