# News Aggregator with django rest framework

It scraps TheKtmPost, Annapurna and Rising nepal for subscribed topics



To run in your local environment

At first install packages with
## `pip install - r requirements.txt`

Then setup database

## `python manage.py makemigrations`

## `python manage.py migrate`

Finally run server with 
## `python manage.py runserver`

Credentials for superuser is as follows:
username: admin
password: admin

You can find documentation of api in /docs endpoint.

---

##### Scraping logic is handeled in this [util](https://github.com/paudelgaurav/content_aggregator/blob/master/news/utils.py)
