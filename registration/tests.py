from django.test import TestCase
from django.utils import timezone

# Create your tests here.

from .models import Caterer, Consumer


class CatererModelTests(TestCase):

    def test_zip_code_is_valid(self):
        """
        is_valid_zip_code() returns false for zip codes that don't
        match the country's zip code set RE
        """
        new_caterer = Caterer(zip_code="6014")
        self.assertIs(new_caterer.has_valid_zip_code(), True)

    def test_zip_code_has_too_few_digits(self):
        """
        is_valid_zip_code() returns false for zip codes that don't
        match the country's zip code set RE... and here
        there are too few digits
        """
        new_caterer = Caterer(zip_code="601")
        self.assertIs(new_caterer.has_valid_zip_code(), False)

    def test_zip_code_has_too_many_digits(self):
        """
        is_valid_zip_code() returns false for zip codes that don't
        match the country's zip code set RE... and here
        there are too many digits
        """
        new_caterer = Caterer(zip_code="601412323")
        self.assertIs(new_caterer.has_valid_zip_code(), False)

    def test_zip_code_has_alpha_chars(self):
        """
        is_valid_zip_code() returns false for zip codes that don't
        match the country's zip code set RE... and here
        there are alpha chars
        """
        new_caterer = Caterer(zip_code="60as")
        self.assertIs(new_caterer.has_valid_zip_code(), False)

    def test_zip_code_has_symbols(self):
        """
        is_valid_zip_code() returns false for zip codes that don't
        match the country's zip code set RE... and here
        there are some symbols
        """
        new_caterer = Caterer(zip_code="$60#")
        self.assertIs(new_caterer.has_valid_zip_code(), False)

    def test_municipality_address_is_valid(self):
        """
        is_valid_municipality_address() returns false for municipalities
        that aren't found in the country
        """
        new_caterer = Caterer()
        pass

    def test_street_address_is_valid(self):
        """
        is_valid_street_address() returns false for streets
        that aren't found in the country
        """
        new_caterer = Caterer()
        pass

    def test_province_address_is_valid(self):
        """
        is_valid_province_address() returns false for provinces
        that aren't found in the country
        """
        new_caterer = Caterer()
        pass


class ConsumerModelTests(TestCase):

    def test_consumer_badge_is_valid(self):
        """
        is_valid_badge_value() returns false for integer badge values 
        above 1 and below 0
        """
        new_consumer = Consumer(badge=0)
        self.assertIs(new_consumer.is_valid_badge_value(), True)

    def test_consumer_badge_is_not_valid(self):
        """
        is_valid_badge_value() returns false for integer badge values 
        above 1 and below 0
        """
        new_consumer = Consumer(badge=-1)
        self.assertIs(new_consumer.is_valid_badge_value(), False)
