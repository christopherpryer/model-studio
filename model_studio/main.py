"""Routes for core Flask app."""
import os
from flask import Blueprint, render_template, request, redirect, make_response
from flask_assets import Environment, Bundle
from werkzeug.utils import secure_filename
import pandas as pd
import csv, io

from . import db

from .auth import login_required
from .utils import url_for

bp = Blueprint('main', __name__,
                    template_folder='templates',
                    static_folder='static')

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/')
@login_required
def home():
    return render_template('home.html')

@bp.route('/upload', methods=('GET', 'POST'))
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            df = pd.read_csv(file)

            # quick fix: correct zipcodes
            df.origin_zip = df.origin_zip.astype(str).str.zfill(5)
            df.dest_zip = df.dest_zip.astype(str).str.zfill(5)

            df.to_sql('shipments', if_exists='replace', con=db.engine,
                index=False)
            return redirect('/geo')
    return render_template('upload.html')


@bp.route('/download')
def download():
    si = io.StringIO()
    cw = csv.writer(si)
    c = db.engine.execute('select * from shipments')
    columns = c.keys()
    rows = c.fetchall()
    cw.writerow(columns)
    cw.writerows(rows)
    response = make_response(si.getvalue())
    response.headers['Content-Disposition'] = \
        'attachment; filename=shipments.csv'
    response.headers['Content-type'] = 'text/csv'
    return response
