from django.http import response
from django.test import TestCase
from tasks.models import Task

class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'taks/base.html')

    def test_can_save_a_POST_request(self):
        # TODO
        response = self.client.post('create_task', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'tasks.html')


