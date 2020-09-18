import os

from flask import render_template, request, redirect, url_for, flash

from app import db
from app.blog import bp
from app.blog.form import Blogform
from app.models import Blogeintrag, Kategorie

'''
@bp.route("/blog")
def create_route():
    blog = Blogeintrag.query.all()
    return render_template(os.path.join('category','overview.html'),bingo=bla)
    return render_template("blog/create.html", bongo=blog)
'''
@bp.route('/blog')
def overview():
    blog = Blogeintrag.query.all()
    return render_template("blog/overview.html", blog=blog)


@bp.route('/blog/erstellen', methods=['POST','GET'])
def create():
    form = Blogform(request.form)
    if request.method == 'POST' and form.validate():
        blog = Blogeintrag()
        blog.titel = form.title.data
        blog.kategorie = form.category.data
        blog.text = form.text.data
        blog.datum = form.date.data
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for("blog.overview"))
    return render_template("blog/create.html",form=form)

@bp.route('/blog/category/overview/<int:id>')
def get(id):
    kategorie=Kategorie.query.get_or_404(id)
    return render_template("blog/overview.html", kategorie=kategorie)


@bp.route('/blog/blogeintrag/blog/<int:id>',  methods=['POST','GET'])
def blog(id):
    blogeintrag = Blogeintrag.query.get_or_404(id)
    return render_template("blog/blog.html", blogeintrag=blogeintrag)

@bp.route('/blog/delete/<int:id>')
def delete(id):
    blog = Blogeintrag.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for("blog.overview"))

