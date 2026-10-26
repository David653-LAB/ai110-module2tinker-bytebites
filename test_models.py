from models import FoodItem
burger=FoodItem("Spicy Burger",8.00,"Mains",4.5)
print(burger.name)
print(burger.price)
print(burger.category)
print(burger.popularity_rating)


from models import Order

order= Order()
order.add_item(burger)
print(order.selected_items)
print(order.calculate_total())

drink=FoodItem("Large Soda",2.50,"Drinks",4.0)
order.add_item(drink)

print(order.calculate_total())

empty_order=Order()
print(empty_order.calculate_total())


from models import Menu
menu=Menu()
menu.add_item(burger)
menu.add_item(drink)

drinks=menu.filter_by_category("Drinks")

print(len(menu.items))
print(len(drinks))  
print(drinks[0].name)  


from models import Customer
customer=Customer("Alice")
customer.add_order(order)
print(customer.name)
print(len(customer.purchase_history))
print(customer.purchase_history[0].calculate_total())


print("Sorted by popularity:")
for item in menu.sort_by_popularity():
    print(item.name, item.popularity_rating)

print("Original menu order:")
for item in menu.items:
    print(item.name, item.popularity_rating)