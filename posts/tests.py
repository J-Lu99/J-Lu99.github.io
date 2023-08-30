from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.

class PostTest(TestCase):

    def setUp(self):
        Post.objects.create(text="just a test")

    def test_text_post(self):
        post=Post.objects.get(id=1)
        expected_text=f"{post.text}"
        self.assertEqual(expected_text,"just a test")

class HomeViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
    
class MessageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/messages/')
        self.assertEqual(resp.status_code, 200)
    def test_view_url_by_name(self):
        resp = self.client.get(reverse("messages"))
        self.assertEqual(resp.status_code, 200)
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('messages'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'messages.html')