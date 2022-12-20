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

    # makes requests to the application without running a live server.
    self.client = self.app.test_client
    self.database_name = 'news_test'
    self.database_path = 'postgresql://{}/{}'.format('localhost:5432', self.database_name)

    # binding the app to the current context
    with self.app.app_context():
      setup_db(self.app, self.database_path)
      self.db = SQLAlchemy()
      self.db.init_app(self.app)

      self.db.create_all()
    
    self.new_data = {
      "title": "Test data title",
      "text": "Text for test data",
      "label": "FAKE"
    }

    self.fail_news = {
      "title": "",
      "text": "",
      "label": None
    }

  def test_get_news(self):
    res = self.client().get("/news")
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data["success"])
    self.assertTrue(data["news"])
    self.assertTrue(data["news_total"])

  def test_get_fake_news(self):
    res = self.client().get('/fake_news')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data["success"])
    self.assertTrue(data["fake_news"])
    self.assertTrue(data["fake_news_total"])

  def test_get_real_news(self):
    res = self.client().get('/real_news')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data["success"])
    self.assertTrue(data["real_news"])
    self.assertTrue(data["real_news_total"])

  def test_add_news(self):
    res = self.client().post('/add_news', json=self.new_data)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data["success"])
    self.assertTrue(data["added"])

  def test_classify(self):
    res = self.client().post("/classify", json=self.new_data)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data["success"])
    self.assertTrue(data["label"])


if __name__ == "__main__":
  unittest.main()