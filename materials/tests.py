from rest_framework.test import APITestCase
from rest_framework import status

from materials.models import Section, Materials, Tests
from users.models import User


class SectionTestCase(APITestCase):
    """Test case for Sections"""
    def setUp(self) -> None:
        User.objects.create_user(
            username='test',
            password='12345',
            is_staff=True
        )

        Section.objects.create(
            title='test',
            description='test'
        )

    def test_update_section(self):
        """Tests the update of the section"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        data = {
            'title': 'test1'
        }
        # print(Section.objects.get(title='test').id)

        response = self.client.patch('/section/update/11/', data=data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], 'test1')

    def test_create_section(self):
        """Tests the creation of section"""
        data = {
            'title': 'test',
            'description': 'test'
        }
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        response = self.client.post('/section/create/', data=data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Section.objects.all().count(), 2)

    def test_list_section(self):
        """Test the view of lists of sections"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        response = self.client.get('/section/list/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_section(self):
        """Tests the view of one section"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        # print(Section.objects.get(title='test').id)

        response = self.client.get('/section/10/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_section(self):
        """Tests delete of section"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        # print(Section.objects.get(title='test').id)

        response = self.client.delete('/section/delete/8/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class MaterialsTestCase(APITestCase):
    """Test case for Materials"""
    def setUp(self) -> None:
        User.objects.create_user(
            username='test',
            password='12345',
            is_staff=True
        )

        Section.objects.create(
            title='test',
            description='test'
        )

        Materials.objects.create(
            title='test',
            content='test',
            section=Section.objects.get(title='test')
        )

    def test_update_material(self):
        """Tests the update of the section"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        data = {
            'title': 'test1'
        }
        # print(Section.objects.get(title='test').id)
        # print(Materials.objects.get(title='test').id)

        response = self.client.patch('/materials/update/6/', data=data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], 'test1')

    def test_create_material(self):
        """Tests the creation of material"""
        data = {
            'title': 'test',
            'content': 'test',
            'section': Section.objects.get(title='test')
        }
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        response = self.client.post('/materials/create/', data=data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Materials.objects.all().count(), 2)

    def test_list_material(self):
        """Test the view of lists of materials"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        response = self.client.get('/section/1/materials/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_material(self):
        """Tests the view of one material"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        response = self.client.get('/materials/5/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_material(self):
        """Tests delete of material"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        # print(Section.objects.get(title='test').id)

        response = self.client.delete('/materials/delete/3/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestsTestCase(APITestCase):
    """Test case for Tests"""

    def setUp(self) -> None:
        User.objects.create_user(
            username='test',
            password='12345',
            is_staff=True
        )

        Section.objects.create(
            title='test',
            description='test'
        )

        Materials.objects.create(
            title='test',
            content='test',
            section=Section.objects.get(title='test')
        )

        Tests.objects.create(
            materials=Materials.objects.get(title='test'),
            question='test',
            correct_answer='test'
        )

    def test_update_test(self):
        """Tests the update of the test"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        data = {
            'question': 'test1'
        }
        # print(Section.objects.get(title='test').id)
        # print(Tests.objects.get(question='test').id)

        response = self.client.patch('/tests/update/7/', data=data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['question'], 'test1')

    def test_create_test(self):
        """Tests the creation of test"""
        data = {
            'question': 'test1',
            'correct_answer': 'test1',
            'materials': Materials.objects.get(title='test')
        }
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        response = self.client.post('/tests/create/', data=data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_tests(self):
        """Test the view of lists of tests"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        response = self.client.get('/materials/3/tests_list/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_tests(self):
        """Tests the view of one test"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        response = self.client.get('/tests/6/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_test(self):
        """Tests delete of test"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        # print(Section.objects.get(title='test').id)

        response = self.client.delete('/tests/delete/4/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_answer_test(self):
        """Tests answering for tests"""
        token = self.client.post('/users/token/', data={'username': 'test', 'password': '12345'})
        headers = {'Authorization': 'Bearer ' + token.json()['access']}

        data = {
            'answer': 'test'
        }

        # print(Tests.objects.get(question='test').id)

        response = self.client.post('/tests/1/answer/', data=data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

