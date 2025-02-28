
from django.test import TestCase

from tabom.models import Article
from tabom.services.article_service import get_an_article


class TestArticleService(TestCase):
    def test_you_can_get_an_article_by_id(self):
        # Given
        title = "test_title"
        article = Article.objects.create(title=title)

        # When
        result_article = get_an_article(article.id)

        # Then
        self.assertEqual(article.id, result_article.id)
        self.assertEqual(title, result_article.title)

    def test_it_should_raise_exception_when_article_does_not_exist(self)->None:
        # Given
        invaild_article_id = 9988 #없는거 선언한거임

        # Expect
        with self.assertRaises(Article.DoesNotExist):
            get_an_article(invaild_article_id)