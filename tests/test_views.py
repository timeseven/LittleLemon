from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from restaurant.views import MenuItemsView


class MenuViewTest(TestCase):
    def setUp(self):
        # add a few test instances of the Menu model
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Chocolate", price=30, inventory=50)
        Menu.objects.create(title="Coke", price=50, inventory=150)

    def test_getall(self):
        # Retrieve all Menu objects and serialized them
        retrieved_data = MenuSerializer(
            Menu.objects.all(), many=True).data

        # Create an instance of a GET request.
        request = RequestFactory().get("/restaurant/menu")

        # Use this syntax for class-based views.
        response = MenuItemsView.as_view()(request)

        # Check if the response data matches the serialized retrieved data
        self.assertEqual(response.data, retrieved_data)
