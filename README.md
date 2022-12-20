# News API

## Setting up

### Install Dependencies

1. Python 3.7 - Follow instructions to install the latest python version in the [documentation](https://docs.python.org/3/)

2. Virtual Environment - Working within a virtual environment is recommended whenever using python for projects. This keeps dependencies seperated and organized. Instructions to set up a virtual environment can be found in the [documentation](https://docs.python.org/3/library/venv.html)

3. PIP Dependencies - when the virtual environment is up and running, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

#### Key dependencies

* [Flask](https://flask.palletsprojects.com/en/2.2.x/) is a lightweigth backend microservices framework, it is required to handle requests and responses
* [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) is a flask extension for handling Cross Origin Resource Sharing (CORS).
* [Pandas](https://pandas.pydata.org/) is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of python.
* [nltk](https://www.nltk.org/) is a platform for building Python programs to work with human language data.
* [scikit-learn](https://scikit-learn.org/stable/) is a library providing simple and efficient tools for predictive data analysis, and is built on Numpy, Scipy, and matplotlib.

### Set up the database

with Postgresql running, create a `news_db` database:

```bash
createdb news_db
```

Populate the database using the `news.psql` file provided. From the terminal run:

```bash
psql news_db < news.psql
```

## Run the server

Frim within the repository, ensure you are working using the virtual environment and in the terminal run:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and adjust the server accordingly.

## Endpoints

`GET '/news'`

* Endpoint to fetch news in the api ordered by their ids
* Arguments: None
* Return: Returns a json object containing the status, news,
    and total number of news in the api.
* Sample request: `curl http://127.0.0.1:5000/news`

```json
{
"news": [
{
"id": 2,
"label": "REAL",
"text": "Ever since Texas laws closed about half of the sta...",
"title": "Study: women had to drive 4 times farther after Texas laws closed abortion clinics"
},
{
"id": 3,
"label": "REAL",
"text": "Donald Trump and Hillary Clinton, now at the start...",
"title": "Trump, Clinton clash in dueling DC speeches"
},
{
"id": 5,
"label": "REAL",
"text": "WASHINGTON -- Forty-three years after the Supreme ...",
"title": "As Reproductive Rights Hang In The Balance, Debate Moderators Drop The Ball"
},
{
"id": 6,
"label": "REAL",
"text": "It's been a big week for abortion news.\n\nCarly Fio...",
"title": "Despite Constant Debate, Americans' Abortion Opinions Rarely Change"
},
{
"id": 7,
"label": "REAL",
"text": "President Barack Obama said Saturday night that Co...",
"title": "Obama Argues Against Goverment Shutdown Over Planned Parenthood"
},
{
"id": 9,
"label": "REAL",
"text": "PLANNED PARENTHOOD’S LOBBYING GETS AGGRESSIVE. Con...",
"title": "Planned Parenthood’s lobbying effort; pay raises for federal workers; and the future Fed rates"
},
{
"id": 10,
"label": "REAL",
"text": "The unexpected death of Justice Antonin Scalia com...",
"title": "Scalia’s death comes just a month before the court’s biggest abortion case in years"
},
{
"id": 12,
"label": "REAL",
"text": "Fact Check: Was Planned Parenthood Started To 'Con...",
"title": "Fact Check: Was Planned Parenthood Started To 'Control' The Black Population?"
},
{
"id": 14,
"label": "REAL",
"text": "Errol Louis is the host of \"Inside City Hall,\" a n...",
"title": "How Planned Parenthood hoax avoids the truth"
},
{
"id": 16,
"label": "REAL",
"text": "WASHINGTON -- Planned Parenthood President Cecile ...",
"title": "P. Parenthood Chief Goes Toe-to-Toe with Attackers"
}
],
"news_total": 6335,
"success": true
}
```

`GET '/fake_news'`

* Endpoint to fetch all news classified as FAKE in api
* Arguments: None
* Return: Returns a json object containing status, fake news and
          total number of fake news present in api
* Sample Request: `curl http://127.0.0.1:5000/fake_news`

```json
{
"fake_news": [
{
"id": 8476,
"label": "FAKE",
"text": "Daniel Greenfield, a Shillman Journalism Fellow at...",
"title": "You Can Smell Hillary’s Fear"
},
{
"id": 10294,
"label": "FAKE",
"text": "Google Pinterest Digg Linkedin Reddit Stumbleupon ...",
"title": "Watch The Exact Moment Paul Ryan Committed Political Suicide At A Trump Rally (VIDEO)"
},
{
"id": 10142,
"label": "FAKE",
"text": "— Kaydee King (@KaydeeKing) November 9, 2016 The l...",
"title": "Bernie supporters on Twitter erupt in anger against the DNC: 'We tried to warn you!'"
},
{
"id": 6903,
"label": "FAKE",
"text": "  \nI’m not an immigrant, but my grandparents are. ...",
"title": "Tehran, USA"
},
{
"id": 7341,
"label": "FAKE",
"text": "Share This Baylee Luciani (left), Screenshot of wh...",
"title": "Girl Horrified At What She Watches Boyfriend Do After He Left FaceTime On"
},
{
"id": 7049,
"label": "FAKE",
"text": "Is Trump the lesser of two evils or are both candi...",
"title": "Celebrity Deathmatch: Darkmoon Sages Make Their Final Predictions on US Election"
},
{
"id": 9648,
"label": "FAKE",
"text": "(Live Streams Available Below) \nAnti-Trump protest...",
"title": "It Begins: Crowds Mass In Major Cities: DC, LA, NYC, Philly, Portland, More… | Will It Escalate? | “95% Chance Of Widespread Violence”"
},
{
"id": 7041,
"label": "FAKE",
"text": "Click Here To Learn More About Alexandra's Persona...",
"title": "Strong Solar Storm, Tech Risks Today | S0 News Oct.26.2016 [VIDEO]"
},
{
"id": 7623,
"label": "FAKE",
"text": "October 31, 2016 at 4:52 am \nPretty factual except...",
"title": "10 Ways America Is Preparing for World War 3"
},
{
"id": 7737,
"label": "FAKE",
"text": "Shocking! Michele Obama & Hillary Caught Glamorizi...",
"title": "Shocking! Michele Obama & Hillary Caught Glamorizing Date Rape Promoters"
}
],
"fake_news_total": 3164,
"success": true
}
```

`GET '/real_news'`

* Enpoint to fetch all news classified as REAL in api
* Arguments: None
* Return: Returns a JSON object containing status, real news
          and total number of real news present in api
* Sample Request: `curl http:127.0.0.1:5000/real_news`

```json
{
"real_news": [
{
"id": 3608,
"label": "REAL",
"text": "U.S. Secretary of State John F. Kerry said Monday ...",
"title": "Kerry to go to Paris in gesture of sympathy"
},
{
"id": 875,
"label": "REAL",
"text": "It's primary day in New York and front-runners Hil...",
"title": "The Battle of New York: Why This Primary Matters"
},
{
"id": 95,
"label": "REAL",
"text": "A Czech stockbroker who saved more than 650 Jewish...",
"title": "‘Britain’s Schindler’ Dies at 106"
},
{
"id": 4869,
"label": "REAL",
"text": "Hillary Clinton and Donald Trump made some inaccur...",
"title": "Fact check: Trump and Clinton at the 'commander-in-chief' forum"
},
{
"id": 2909,
"label": "REAL",
"text": "Iranian negotiators reportedly have made a last-di...",
"title": "Iran reportedly makes new push for uranium concessions in nuclear talks"
},
{
"id": 1357,
"label": "REAL",
"text": "CEDAR RAPIDS, Iowa — “I had one of the most wonder...",
"title": "With all three Clintons in Iowa, a glimpse at the fire that has eluded Hillary Clinton’s campaign"
},
{
"id": 988,
"label": "REAL",
"text": "Donald Trump’s organizational problems have gone f...",
"title": "Donald Trump’s Shockingly Weak Delegate Game Somehow Got Even Worse"
},
{
"id": 3343,
"label": "REAL",
"text": "(CNN) Secretary of State John Kerry said Thursday ...",
"title": "John Kerry: ISIS responsible for genocide"
},
{
"id": 4348,
"label": "REAL",
"text": "With the shake of an Etch-A-Sketch, Mitt Romney re...",
"title": "Mitt Romney's Re-Invention As Anti-Poverty Warrior"
},
{
"id": 1571,
"label": "REAL",
"text": "Killing Obama administration rules, dismantling Ob...",
"title": "Trump takes on Cruz, but lightly"
}
],
"real_news_total": 3171,
"success": true
}
```

`POST '/classify'`

* Endpoint to classify news
* Arguments: None
* Return: Returns a json object containing status and predicted class
* Sample Request: curl `http://127.0.0.1:5000/classify`

```json
```
