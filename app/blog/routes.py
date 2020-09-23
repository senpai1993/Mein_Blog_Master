import os

from flask import render_template, request, redirect, url_for, flash

from app import db
from app.blog import bp
from app.blog.form import Blogform
from app.models import Blogeintrag, Kategorie


@bp.route('/blog')
def overview():
    blog = Blogeintrag.query.all()
    return render_template("blog/overview.html", blog=blog)


@bp.route('/')
def index():
    """
    only three
    :return:
"""
    blog = Blogeintrag.query.order_by(Blogeintrag.datum).limit(3)
    return render_template("blog/overview.html", blog=blog)

    """
    blog = Blogeintrag.query(blog).order_by(Blogeintrag.date.desc()).first()
    return render_template("blog/overview.html", blog=blog)
"""

@bp.route('/blog/erstellen', methods=['POST','GET'])
def create():
    flash("Blogeintrag erfolgreich erstellt!")
    form = Blogform(request.form)
    kategorien = Kategorie.query.all()
    if request.method == 'POST' and form.validate():
        blog = Blogeintrag()
        blog.titel = form.title.data
        blog.kategorie = form.category.data
        blog.text = form.text.data
        blog.datum = form.date.data
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for("blog.overview"))
    return render_template("blog/create.html",form=form,kategorien=kategorien)


@bp.route('/blog/modify/<int:id>', methods=['POST', 'GET'])
def update(id):
    flash("Blogeintrag erfolgreich aktualisiert!")
    blogeintrag = Blogeintrag.query.get_or_404(id)
    form = Blogform(request.form)
    if request.method == 'POST' and form.validate():
        blogeintrag.titel = form.title.data
        blogeintrag.kategorie = form.category.data
        blogeintrag.text = form.text.data
        blogeintrag.datum = form.date.data
        db.session.add(blogeintrag)
        db.session.commit()
        return redirect(url_for("blog.overview"))
    form.title.data = blogeintrag.titel
    form.category.data = blogeintrag.kategorie
    form.text.data = blogeintrag.text
    form.date.data = blogeintrag.datum
    return render_template("blog/update.html", form=form)

@bp.route('/blog/category/overview/<int:id>')
def get(id):
    blog=Blogeintrag.query.filter_by(kategorie=id)
    return render_template("blog/overview.html", blog=blog)


@bp.route('/blog/blogeintrag/blog/<int:id>',  methods=['POST','GET'])
def blog(id):
    blogeintrag = Blogeintrag.query.get_or_404(id)
    return render_template("blog/blog.html", blogeintrag=blogeintrag)

@bp.route('/blog/delete/<int:id>')
def delete(id):
    flash("Blogeintrag erfolgreich gelöscht!")
    blog = Blogeintrag.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for("blog.overview"))

