from rest_framework.test import APITestCase
from .models import BlogPost

class BlogPostDetailTests(APITestCase):
    def test_missing_post_is_404_for_all_methods(self):
        for method in [self.client.get, self.client.put, self.client.delete]:
            response = method('/blogposts/999/')
            self.assertEqual(response.status_code, 404)

    def test_update_validation_preserves_original(self):
        post = BlogPost.objects.create(title='Original', content='Body')
        response = self.client.put(f'/blogposts/{post.pk}/', {'title': '', 'content': 'changed'})
        self.assertEqual(response.status_code, 400)
        post.refresh_from_db()
        self.assertEqual(post.title, 'Original')

    def test_read_update_delete(self):
        post = BlogPost.objects.create(title='Original', content='Body')
        url = f'/blogposts/{post.pk}/'
        self.assertEqual(self.client.get(url).data['title'], 'Original')
        self.assertEqual(self.client.put(url, {'title': 'Updated', 'content': 'New'}).status_code, 200)
        self.assertEqual(self.client.delete(url).status_code, 204)
        self.assertFalse(BlogPost.objects.filter(pk=post.pk).exists())
