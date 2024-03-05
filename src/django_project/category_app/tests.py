from rest_framework.test import APITestCase

class TestCategoryAPI(APITestCase):
    def test_list_categories(self):
        response = self.client.get("/api/categories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, world!"})