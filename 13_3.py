from task_13_1 import Restaurant

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0  # Новый атрибут
    
    def update_rating(self, new_rating):
        if 0 <= new_rating <= 5:
            self.rating = new_rating
            print(f"Рейтинг обновлён: {self.rating}")
        else:
            print("Ошибка: рейтинг должен быть от 0 до 5")

# Пример использования
rest = Restaurant("Токио Сити", "азиатская")
rest.update_rating(4.5)
print(f"Текущий рейтинг: {rest.rating}")