from flask import Blueprint, render_template, g, session
from flask_login import login_required

from mod_admin.models import Admin

# For when we eventually add multi-user support
from decorators import check_admin

admin = Blueprint("admin", __name__, url_prefix="/lb-admin")

@admin.route("/")
@login_required
def home():
    return "Hello World"