import os

from flask import render_template

from app.category import bp
from app.models import Test

@bp.route("/")
def create_route():
    bla = Test.query.all()
    '''
    return render_template(os.path.join('category','overview.html'),bingo=bla)
'''
    return render_template("category/overview.html", bingo=bla)

@app.route('/add', methods=['POST'])
def add_entry():
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

