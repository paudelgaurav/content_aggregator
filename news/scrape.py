import requests
from bs4 import BeautifulSoup

from django.shortcuts import get_object_or_404

from .models import Topic, News


def doScrape(topic):
    topic_url = topic   
    s_url = 'https://kathmandupost.com'
    if topic == 'business':
        topic_url = 'money'
    elif topic == 'trending':
        topic_url = 'opinion'
    elif topic == 'technology':
        topic_url = 'science-technology'

    url = 'https://kathmandupost.com/{0}'.format(topic_url)
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    newss = soup.find_all('article',class_='article-image')

    for news in newss[:2]:
        news_title = news.find('h3').text
        news_content = news.find('p').text
        news_link = news.find('a',href=True)
        link = s_url+news_link['href']
        t = get_object_or_404(Topic, slug=topic)
        News.objects.create(title=news_title,content=news_content,url=link,source='Kathmandu Post',topic=t)



def doSccrape(topic):
    topic_url = topic
    if topic == 'trending':
        topic_url = 'main-news'
    if topic == 'technology':
        return None

    t_url = 'https://risingnepaldaily.com/{0}'.format(topic_url)
    html_text = requests.get(t_url).text
    soup = BeautifulSoup(html_text, 'lxml')
    newss = soup.find_all('div', class_='business')

    for news in newss[:2]:
        news_title = news.find('p', class_='trand').text.strip()
        news_content = news.find('p', class_='description').text.strip()
        news_link = news.find('a',href=True)
        t = get_object_or_404(Topic, slug=topic)
        News.objects.create(title=news_title, content=news_content, url=news_link['href'],source='Rising Nepal',topic=t)



def doScccrape(topic):
    topic_url = topic
    if topic == 'trending':
        topic_url = 'features'
    elif topic == 'technology':
        topic_url = 'auto-and-tech'

    a_url = 'https://theannapurnaexpress.com/category/{0}'.format(topic_url)
    html_text = requests.get(a_url).text
    soup = BeautifulSoup(html_text, 'lxml')
    newsss = soup.find_all('div',class_='col-md-8')

    for newss in newsss[:2]:
        news = newss.find('div',class_='article-text')
        news_title = news.find('a').text
        news_content = news.find('p', class_='mainnews-content').text
        news_link = news.find('a',href=True)
        t = get_object_or_404(Topic, slug=topic)
        News.objects.create(title=news_title, content=news_content,url=news_link['href'],source='Annapurna Express',topic=t)

def getNews(topic):
    doScrape(topic)
    doSccrape(topic)
    doScccrape(topic)