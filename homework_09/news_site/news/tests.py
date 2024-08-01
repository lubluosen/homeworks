from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import News

class NewsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.news = News.objects.create(
            title='Тестовая новость',
            content='это тестовая новость для проверки теста',
            author=self.user
        )

    def tearDown(self):
        self.user.delete()
        self.news.delete()

    def test_news_list_view(self):
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовая новость')
        self.assertTemplateUsed(response, 'news/news_list.html')

    def test_news_detail_view(self):
        response = self.client.get(reverse('news_detail', args=[self.news.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'это тестовая новость для проверки теста')
        self.assertTemplateUsed(response, 'news/news_detail.html')