from flask import Blueprint, render_template, abort

auth_api = Blueprint('Auth API', 'auth_api', template_folder="templates")