import os

from flask import render_template, request, redirect, url_for, flash

from app import db
from app.category import bp
from app.category.form import Kategorieform
from app.models import Kategorie



@bp.route('/category')
def overview():
    kategorien = Kategorie.query.all()
    return render_template("category/overview.html", kategorien=kategorien)


@bp.route('/category/erstellen', methods=['POST','GET'])
def create():
    form = Kategorieform(request.form)
    if request.method == 'POST' and form.validate():
        kategorie = Kategorie()
        kategorie.value = form.kategorie.data
        db.session.add(kategorie)
        db.session.commit()
        return redirect(url_for("category.overview"))
    return render_template("category/create.html",form=form)

@bp.route('/category/delete/<int:id>')
def delete(id):
    kategorie = Kategorie.query.get_or_404(id)
    db.session.delete(kategorie)
    db.session.commit()
    return redirect(url_for("category.overview"))

@bp.route('/category/modify/<int:id>', methods=['POST','GET'])
def update(id):
    kategorie = Kategorie.query.get_or_404(id)
    form = Kategorieform(request.form)
    if request.method == 'POST' and form.validate():
        kategorie.value = form.kategorie.data
        db.session.add(kategorie)
        db.session.commit()
        return redirect(url_for("category.overview"))
    form.kategorie.data = kategorie.value
    return render_template("category/update.html",form=form)





