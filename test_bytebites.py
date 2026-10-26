from models import Customer, FoodItem, Menu, Order


def test_calculate_total_with_multiple_items():
    burger=FoodItem("Burger", 10.00, "Mains", 4.5)
    soda=FoodItem("Soda", 5.0, "Drinks", 4.0)

    order=Order()
    order.add_item(burger)
    order.add_item(soda)

    assert order.calculate_total() == 15.0

def test_order_total_is_zerfo_when_empty():
    order=Order()
    assert order.calculate_total() == 0.0

def test_filter_menu_items_by_category():
    burger=FoodItem("Burger", 10.00, "Mains", 4.5)
    soda=FoodItem("Soda", 5.0, "Drinks", 4.0)

    menu=Menu()
    menu.add_item(burger)
    menu.add_item(soda)

    results=menu.filter_by_category("Drinks")
    assert results==[soda]

def test_sort_menu_items_by_popularity():
    burger=FoodItem("Burger", 10.00, "Mains", 4.5)
    soda=FoodItem("Soda", 5.0, "Drinks", 4.0)
  

    menu=Menu()
    menu.add_item(burger)
    menu.add_item(soda)
   

    results=menu.sort_by_popularity()
    assert results==[burger, soda]