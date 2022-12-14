import os
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
import json

database_path = 'postgresql://{}/{}'.format('localhost:5432', 'news_db')

db = SQLAlchemy()

"""
setup_db(app)
    function that binds a flask application and a SQLAlchemy service
"""

def setup_db(app, database_path=database_path):
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  db.app = app
  db.init_app(app)
  db.create_all()

"""
Main_News
"""
class News(db.Model):
  __tablename__ = "news"

  id = Column(Integer, primary_key=True)
  title = Column(String(50), nullable=False)
  text = Column(String, nullable=False)
  label = Column(String(5), nullable=False)

  def __init__(self, title, text, label):
    self.title = title
    self.text = text
    self.label = label

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'text': f'{self.text[:50]}...',
      'label': self.label
    }