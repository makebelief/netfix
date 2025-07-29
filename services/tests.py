from django.test import TestCase
from django.urls import reverse
from .models import Service
from users.models import User
from .request_service import RequestService
from django.utils import timezone

class ServiceTests(TestCase):
    def setUp(self):
        self.service_data = {
            'name': 'Test Service',
            'description': 'Test Description',
            'price': 99.99,
            'is_active': True
        }
        self.service = Service.objects.create(**self.service_data)
        
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_service_creation(self):
        self.assertTrue(isinstance(self.service, Service))
        self.assertEqual(self.service.name, self.service_data['name'])
        self.assertEqual(self.service.price, self.service_data['price'])

    def test_service_str(self):
        self.assertEqual(str(self.service), self.service_data['name'])

class RequestServiceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.service = Service.objects.create(
            name='Test Service',
            description='Test Description',
            price=99.99,
            is_active=True
        )
        self.request_data = {
            'user': self.user,
            'service': self.service,
            'status': 'pending',
            'requested_date': timezone.now(),
            'notes': 'Test notes'
        }
        self.request = RequestService.objects.create(**self.request_data)

    def test_request_creation(self):
        self.assertTrue(isinstance(self.request, RequestService))
        self.assertEqual(self.request.user, self.request_data['user'])
        self.assertEqual(self.request.service, self.request_data['service'])

    def test_request_str(self):
        expected = f"{self.user.username} - {self.service.name} ({self.request.status})"
        self.assertEqual(str(self.request), expected)
