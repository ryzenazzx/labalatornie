class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' открыт!")

# Создание экземпляра и вызов методов
new_restaurant = Restaurant("Вкусно и точка", "русская")
print(new_restaurant.restaurant_name)
print(new_restaurant.cuisine_type)
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()