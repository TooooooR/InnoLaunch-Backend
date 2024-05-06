from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

from api.models import Service, Address, Amenity, EstablishmentImage, Establishment, Comment, PriceCategory


class CreateModelsTestCase(TestCase):
    def test_create_establishment(self):
        establishment = Establishment.objects.create(
            slug='test-slug',
            name='Test Establishment',
            type='Test Type',
            short_description='Test Description',
            address=Address.objects.create(city='Test City', street='Test Street', build_number='123'),
            price_category=PriceCategory.objects.create(price_range='Test Price Range'),
            capacity=10,
            work_mobile_number='1234567890',
            is_recommended=True
        )
        self.assertIsNotNone(establishment.pk)

    def test_create_address(self):
        address = Address.objects.create(city='Test City', street='Test Street', build_number='123')
        self.assertIsNotNone(address.pk)

    def test_create_price_category(self):
        price_category = PriceCategory.objects.create(price_range='Test Price Range')
        self.assertIsNotNone(price_category.pk)

    def test_create_establishment_image(self):
        establishment = Establishment.objects.create(
            slug='test-slug',
            name='Test Establishment',
            type='Test Type',
            short_description='Test Description',
            address=Address.objects.create(city='Test City', street='Test Street', build_number='123'),
            price_category=PriceCategory.objects.create(price_range='Test Price Range'),
            capacity=10,
            work_mobile_number='1234567890',
            is_recommended=True
        )
        establishment_image = EstablishmentImage.objects.create(
            establishment=establishment,
            image='service/media/establishment_images/woods.jpg'
        )
        self.assertIsNotNone(establishment_image.pk)

    def test_create_amenity(self):
        amenity = Amenity.objects.create(name='Test Amenity', description='Test Description')
        self.assertIsNotNone(amenity.pk)

    def test_create_service(self):
        service = Service.objects.create(name='Test Service')
        self.assertIsNotNone(service.pk)

    def test_create_comment(self):
        establishment = Establishment.objects.create(
            slug='test-slug',
            name='Test Establishment',
            type='Test Type',
            short_description='Test Description',
            address=Address.objects.create(city='Test City', street='Test Street', build_number='123'),
            price_category=PriceCategory.objects.create(price_range='Test Price Range'),
            capacity=10,
            work_mobile_number='1234567890',
            is_recommended=True
        )
        comment = Comment.objects.create(
            author='Test Author',
            rating=5,
            content='Test Content',
            establishment=establishment
        )
        self.assertIsNotNone(comment.pk)


class HomePageViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='admin', password='adminpassword', is_staff=True)

    def test_view_returns_recommended_establishments(self):
        response = self.client.get('/api/v1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_fields = ['name', 'type', 'work_mobile_number', 'url', 'address', 'price_category', 'images',
                           'is_recommended']
        for establishment in response.data:
            self.assertTrue(establishment['is_recommended'])
            self.assertCountEqual(establishment.keys(), expected_fields)

