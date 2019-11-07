from django.test import TestCase
from django.urls import reverse
from app import models


class TestHomePage(TestCase):
    def test_all_coffee_is_shown(self):
        coffees = [
            models.Coffee.objects.create(name="Test Coffee 1", price=1),
            models.Coffee.objects.create(name="Test Coffee 2", price=3),
            models.Coffee.objects.create(name="Test Coffee 3", price=7),
        ]

        response = self.client.get(reverse("home"))

        for coffee in coffees:
            self.assertContains(response, coffee.name)

    def test_has_a_button_to_buy_each_coffee(self):
        coffees = [
            models.Coffee.objects.create(name="Test Coffee 1", price=1),
            models.Coffee.objects.create(name="Test Coffee 2", price=3),
            models.Coffee.objects.create(name="Test Coffee 3", price=7),
        ]

        response = self.client.get(reverse("home"))

        for coffee in coffees:
            self.assertContains(response, f"Buy {coffee.name}")


# Create your tests here.
class TestBuyingACoffee(TestCase):
    def test_creates_a_transaction(self):
        coffee_to_buy = models.Coffee.objects.create(name="Test Coffee", price=2.85)

        self.client.post(reverse("buy_coffee", args=[coffee_to_buy.id]))

        self.assertEqual(
            coffee_to_buy.transaction_set.count(),
            1,
            "buying a coffee should create a new Transaction for that coffee",
        )

        transaction = coffee_to_buy.transaction_set.last()

        self.assertAlmostEqual(
            transaction.pre_tax,
            2.85,
            msg="pre tax should match the price of the coffee",
        )

        self.assertAlmostEqual(
            transaction.tax, 0.2, places=2, msg="tax should be 7% of the coffee's price"
        )

    def test_redirects_to_the_transaction_page(self):
        coffee_to_buy = models.Coffee.objects.create(name="Test Coffee", price=2.85)

        response = self.client.post(reverse("buy_coffee", args=[coffee_to_buy.id]))

        transaction = coffee_to_buy.transaction_set.last()

        self.assertRedirects(
            response, reverse("transaction_detail", args=[transaction.id])
        )


class TestTransactionPage(TestCase):
    def test_shows_transaction_information(self):
        coffee_to_buy = models.Coffee.objects.create(name="Test Coffee", price=2.85)
        transaction = coffee_to_buy.transaction_set.create(pre_tax=123, tax=456)

        response = self.client.get(reverse("transaction_detail", args=[transaction.id]))

        self.assertContains(response, transaction.id)
        self.assertContains(response, coffee_to_buy.name)
        self.assertContains(response, transaction.pre_tax)
        self.assertContains(response, transaction.tax)
