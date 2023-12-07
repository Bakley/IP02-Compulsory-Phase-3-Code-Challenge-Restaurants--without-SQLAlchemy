import unittest

from challenge_restaurants import Customer, Restaurant, Review
# from challenge_restaurants import Customer, Restaurant, Review


class TestRestaurantReview(unittest.TestCase):
     def setUp(self):
        self.customer1 = Customer("John", "Doe")
        self.customer2 = Customer("Alice", "Smith")
        self.restaurant1 = Restaurant("Tasty Treats")
        self.restaurant2 = Restaurant("Burger Palace")
        self.review1 = Review(self.customer1, self.restaurant1, 4)
        self.review2 = Review(self.customer2, self.restaurant2, 5)
    
    
class TestUserName(TestRestaurantReview):
        def test_customer_full_name(self):
            """Testing user full name"""
            self.assertEqual(self.customer1.full_name(), "John Doe")
            self.assertNotEqual(self.customer2.full_name(), "Al1ce Smith")
            
            
class TestRestRating(TestRestaurantReview):
  def test_restaurant_rating(self):
        self.assertEqual(self.restaurant1.average_star_rating(), 4.0)
        self.assertEqual(self.restaurant2.average_star_rating(), 5.0)


if __name__ == '__main__':
    unittest.main()