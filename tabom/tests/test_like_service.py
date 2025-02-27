from django.db import IntegrityError
from django.test import TestCase

from tabom.models import Article, User
from tabom.services.like_service import do_like


class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # Given : 테스트에 필요한 재료준비
        user = User.objects.create(name="test")
        article = Article.objects.create(
            title="test_title",
        )
        # When : 실제 테스트 대상이 되는 동작을 실행
        like = do_like(user.id, article.id)

        # Then : 동작 마친후 결과가 예상한대로 나왓는지 검증
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)

    def test_a_user_can_like_an_article_only_once(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # Expect
        like1 = do_like(user.id, article.id)
        with self.assertRaises(IntegrityError):
            like2 = do_like(user.id, article.id)
