# ByteBites class models
# Customer: Stores customer information and purchase history.
# FoodItem: Stores information about an individual food item.
# Menu: Stores food items and filters them by category.
# Order: Stores selected food items and calculates the total cost.


class FoodItem:
    """Holds the data for one item we sell, e.g. "Spicy Burger" or "Large Soda"."""

    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Order:
    """Groups the items a user picks into one transaction and computes the total cost."""

    def __init__(self):
        self.selected_items = []

    def add_item(self, item):
        self.selected_items.append(item)

    def calculate_total(self):
        total = 0.0
        for item in self.selected_items:
            total += item.price
        return total


class Menu:
    """Holds the full collection of items and filters it by category."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        matches = []
        for item in self.items:
            if item.category == category:
                matches.append(item)
        return matches

    def sort_by_popularity(self):
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)
    


class Customer:
    """Stores who the customer is and their past orders."""

    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_order(self, order):
        self.purchase_history.append(order)