from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post, Comment
from .views import post_list, post_create, post_update, post_delete, post_detail, like_post
import faker

fake = faker.Faker()

class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')

    def test_post_creation(self):
        post = Post(title='Test Post', content='This is a test post', author=self.user)
        post.save()
        self.assertEqual(Post.objects.count(), 1)

    def test_post_str_representation(self):
        post = Post(title='Test Post', content='This is a test post', author=self.user)
        self.assertEqual(str(post), 'Test Post')

class CommentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.post = Post(title='Test Post', content='This is a test post', author=self.user)

    def test_comment_creation(self):
        # Create a unique username for each test run
        username = fake.user_name()

        # Create an author instance with the unique username
        author = User.objects.create_user(username, 'test@example.com', 'password')

        # Use the same author instance to create the Post instance
        post = Post(title="Test Post", content="This is a test post", author=author)
        post.save()  # Save the post first

        comment = Comment(post=post, content="This is a test comment", author=author)
        comment.save()  # Now you can save the comment

