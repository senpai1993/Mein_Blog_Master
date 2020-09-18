from app import db

class Blogeintrag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String, nullable=False)
    kategorie = db.Column(db.ForeignKey("kategorie.id"), nullable=False)
    text = db.Column(db.String, nullable=False)
    datum = db.Column(db.Date, nullable=False)

class Kategorie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    value = db.Column(db.String, nullable=False)
    blogeintrag = db.relationship("Blogeintrag", backref="Kategorie")








