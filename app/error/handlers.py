import os
from flask import render_template
from app.error import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template(os.path.join('error', '404.html')), 404

