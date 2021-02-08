from django.test import TestCase
from django.contrib.auth.models import User

from .models import Topic, News

class TopicModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser', password='testuser@123',email='test@test.com')
        Topic.objects.create(title="Test topic",slug='test-topic')
        Topic.objects.get(id=1).subscriber.add(user)

    def test_title_content(self):
        topic = Topic.objects.get(id=1)
        expected_object_name = f'{topic.title}'
        count = Topic.objects.count()
        self.assertEquals(expected_object_name, 'Test topic')
        self.assertEquals(count,1)

        
class NewsmodelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        News.objects.create(title='Test news title',content='Test news content',url='https://www.test.com',source='test')

    def test_news(self):
        news = News.objects.get(id=1)
        news_title = f'{news.title}'
        news_content = f'{news.content}'
        news_url = f'{news.url}'
        news_source = f'{news.source}'
        self.assertEquals(news_title, 'Test news title')
        self.assertEquals(news_content, 'Test news content')
        self.assertEquals(news_url, 'https://www.test.com')
        self.assertEquals(news_source, 'test')