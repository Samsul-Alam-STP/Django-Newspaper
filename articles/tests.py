from django.urls import reverse
from django.test import TestCase


class Test_VIEW(TestCase):
    def test_view(self):
        response = self.client.get(reverse("article_detail"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "article_edit.html")
