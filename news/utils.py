import requests
from bs4 import BeautifulSoup

from django.shortcuts import get_object_or_404

from .models import Topic, News

news_bulk_create_list = []


# Scraping The kathmandu Post
def scrape_KTM_Post(topic):
    topic_url = topic
    s_url = 'https://kathmandupost.com'
    if topic == 'business':
        topic_url = 'money'
    elif topic == 'trending':
        topic_url = 'opinion'
    elif topic == 'technology':
        topic_url = 'science-technology'

    url = f'https://kathmandupost.com/{topic_url}'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, features="lxml")
    news_list = soup.find_all('article', class_='article-image')

    for news in news_list[:2]:
        news_title = news.find('h3').text
        news_content = news.find('p').text
        news_link = news.find('a', href=True)
        link = s_url+news_link['href']

        topic_obj = get_object_or_404(Topic, slug=topic)
        news_bulk_create_list.append(
            News(
                title=news_title,
                content=news_content,
                url=link,
                source='Kathmandu Post',
                topic=topic_obj
            )
        )


# Scraping The Rising Nepal
def scrape_Rising_Nepal(topic):
    topic_url = topic

    if topic == 'trending':
        topic_url = 'main-news'
    elif topic == 'technology':
        return None

    t_url = f'https://risingnepaldaily.com/{topic_url}'
    html_text = requests.get(t_url).text
    soup = BeautifulSoup(html_text, 'lxml')
    news_list = soup.find_all('div', class_='business')

    for news in news_list[:2]:
        news_title = news.find('p', class_='trand').text.strip()
        news_content = news.find('p', class_='description').text.strip()
        news_link = news.find('a', href=True)

        topic_obj = get_object_or_404(Topic, slug=topic)
        news_bulk_create_list.append(
            News(
                title=news_title,
                content=news_content,
                url=news_link['href'],
                source='Rising Nepal',
                topic=topic_obj
            )
        )


# Scraping Annapurna Express
def scrape_annapurna(topic):
    topic_url = topic
    if topic == 'trending':
        topic_url = 'features'
    elif topic == 'technology':
        topic_url = 'auto-and-tech'

    a_url = f'https://theannapurnaexpress.com/category/{topic_url}'
    html_text = requests.get(a_url).text
    soup = BeautifulSoup(html_text, 'lxml')
    news_list = soup.find_all('div', class_='col-md-8')

    for news_data in news_list[:2]:
        news = news_data.find('div', class_='article-text')
        news_title = news.find('a').text
        news_content = news.find('p', class_='mainnews-content').text
        news_link = news.find('a', href=True)

        topic_obj = get_object_or_404(Topic, slug=topic)
        news_bulk_create_list.append(
            News(
                title=news_title,
                content=news_content,
                url=news_link['href'],
                source='Annapurna Express',
                topic=topic_obj
            )
        )


def get_news(topic):
    topic = topic.lower()
    scrape_KTM_Post(topic)
    scrape_Rising_Nepal(topic)
    scrape_annapurna(topic)
    News.objects.bulk_create(news_bulk_create_list)
