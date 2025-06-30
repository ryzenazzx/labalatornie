from task_13_1 import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type="мороженое"):
        super().__init__(name, cuisine_type)
        self.flavors = ["ванильное", "шоколадное", "клубничное"]
    
    def show_flavors(self):
        print("Доступные сорта мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Создание экземпляра и вызов методов
ice_cream_stand = IceCreamStand("Cold Stone")
ice_cream_stand.describe_restaurant()
ice_cream_stand.show_flavors()