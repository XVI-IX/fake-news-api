import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, News

class NewsTestCase(unittest.TestCase):
  """Represents the tests for the api"""

  def setUp(self):
    """Defining variablea and initializing"""
    self.app = create_app()
    self.new_data = {
      "title": "Test data title",
      "text": "Text for test data",
      "label": "FAKE"
    }
    # makes requests to the application without running a live server.
    self.client = self.app.test_client()
    self.database_name = 'news_test'
    self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
    setup_db(self.app, self.database_name)

    # binding the app to the current context
    with self.app.app_context():
      self.db = SQLAlchemy()
      self.db.init_app(self.app)

      self.db.create_all()

    self.fail_news = {
      "title": "",
      "text": "",
      "label": None
    }

  def test_get_news(self):
    res = self.client().get("/news")
    data = json.loads(res.data)

    self.assertEqual(data["status"], 200)
    self.assertTrue(data["title"])
    self.assertTrue(data["text"])
    self.assertTrue(data["label"])

  def test_get_fake_news(self):
    res = self.client().get('/fake_news')
    data = json.loads(res.data)

    self.assertEqual(data["status"], 200)
    self.assertTrue(data["title"])
    self.assertTrue(data["text"])
    self.assertTrue(data["label"])

  def test_get_real_news(self):
    res = self.client().get('/get_real_news')
    data = json.loads(res.data)

    self.assertEqual(data["status"], 200)
    self.assertTrue(data["title"])
    self.assertTrue(data["text"])
    self.assertTrue(data["label"])

  def test_add_news(self):
    res = self.client().post('/get_real_news', json=self.new_data)
    data = json.loads(res.data)

    self.assertEqual(data["status"], 200)
    self.assertTrue(data["title"])
    self.assertTrue(data["text"])
    self.assertTrue(data["label"])

  def test_classify(self):
    res = self.client().get("/classify")
    data = json.loads(res.data)

    self.assertEqual(data["status"], 200)
    self.assertTrue(data["success"])
    self.assertTrue(data["label"])


if __name__ == "__main__":
  unittest.main()