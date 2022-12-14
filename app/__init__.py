import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from data_prep import clean_text, classify

from models import setup_db, News

PAGE_MAX = 10

def pagination(request, selection):
  """
  Function to apply pagination to api responses
  """

  page = request.args.get("page", 1, type=int)

  start = (page - 1) * PAGE_MAX
  end = PAGE_MAX

  formatted_selection = [item.format() for item in selection]

  return formatted_selection[start:end]

def create_app(test_config=None):

  app = Flask(__name__)

  with app.app_context():
    setup_db(app)

  """
  Set up CORS. Allow '*' for origins.
  """
  CORS(app)

  """
  Use the after_request decorator to set Access-Control-Allow
  """
  @app.after_request
  def after_request(response):
    response.headers.add(
      "Access-Control-Allow-Headers",
      "Content-Type, Authorization, true"
    )
    response.headers.add(
      "Access-Control-Allow-Methods",
      "GET, PUT, POST"
    )
    response.headers.add(
      "Access-Control-Allow-Origin", "*"
    )

    return response

  """
  Endpoint to handle GET requests for all news.
  """
  @app.route("/news", methods=['GET'])
  def get_news():
    """
    * Endpoint to fetch news in the api ordered by their ids
    * Arguments: None
    * Return: Returns a json object containing the status, news,
      and total number of news in the api.
    * Sample request: `curl http://127.0.0.1:5000/news`
    """

    # get page value used in pagination from front end
    all_news = News.query.order_by(News.id).all()
    current_news = pagination(request, all_news)

    if len(current_news) == 0:
      abort(404)

    return jsonify({
      "success": True,
      "news": current_news,
      "news_total": len(all_news)
    })

  @app.route("/fake_news", methods=["GET"])
  def get_fake_news():
    """
    * Endpoint to fetch all news classified as FAKE in api
    * Arguments: None
    * Return: Returns a json object containing status, fake news and
              total number of fake news present in api
    * Sample Request: `curl http://127.0.0.1:5000/fake_news`
    """
    page = request.args.get("page", 1, type=int)
    fake_news = News.query.filter(News.label == 'FAKE').all()
    
    current_news = pagination(request, fake_news)

    if len(current_news) == 0:
      abort(404)

    return jsonify({
      "success": True,
      "fake_news": current_news,
      "fake_news_total": len(fake_news)
    })
  
  @app.route("/real_news", methods=["GET"])
  def get_real_news():
    """
    Endpoint to fetch all news classified as REAL in api

    * Arguments: None
    * Return: Returns a JSON object containing status, real news
              and total number of real news present in api
    * Sample Request: `curl http:127.0.0.1:5000/real_news`
    """
    real_news = News.query.filter(News.label == "REAL").all()

    current = pagination(request, real_news)
    if len(current) == 0:
      abort(404)

    return jsonify({
      "success": True,
      "real_news": current,
      "real_news_total": len(real_news)
    })

  @app.route("/add_news", methods=['POST'])
  def add_news():
    news = request.get_json()

    title = news.get("title")
    text = clean_text(news.get("text"))
    label = news.get("label")

    params = [title, text, label]

    for param in params:
      if not param:
        abort(422)
    
    news = News(
      title=title,
      text=text,
      label= label
    )

    try:
      news.insert()
    except Exception as e:
      print(e)
      return (500)
    
    return jsonify({
      "success": True,
      "added": str(news.id)
    })

  @app.route("/classify", methods=["POST"])
  def predict():
    """
    Endpoint to classify news
    Arguments: None
    Return: Returns a json object containing status and predicted class

    Sample Request: curl `http://127.0.0.1:5000/classify`
    """
    
    news = request.get_json()
    text = news.get("text")

    if not text:
      abort(422)

    text = clean_text(text)

    prediction = classify(text)

    return jsonify({
      "success": True,
      "label": prediction
    })

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "message": "File not found"
    }), 404

  @app.errorhandler(422)
  def not_processed(error):
    return jsonify({
      'success': False,
      "message": "Not processed"
    }), 422

  @app.errorhandler(500)
  def server_error(error):
    return jsonify({
      "success": False,
      "message": "Internal Server error"
    }), 500
    
  return app