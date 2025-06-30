class IceCreamStand(Restaurant):
    def __init__(self, name, location, hours):
        super().__init__(name, "мороженое")
        self.flavors = []
        self.location = location
        self.hours = hours
        self.ice_cream_types = {
            "на палочке": [],
            "мягкое": [],
            "в стаканчике": []
        }
    
    def add_flavor(self, flavor, ice_type="на палочке"):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            self.ice_cream_types[ice_type].append(flavor)
            print(f"Добавлен новый сорт: {flavor} ({ice_type})")
        else:
            print(f"Сорт '{flavor}' уже есть в списке!")
    
    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            for ice_type in self.ice_cream_types:
                if flavor in self.ice_cream_types[ice_type]:
                    self.ice_cream_types[ice_type].remove(flavor)
            print(f"Сорт '{flavor}' удалён")
        else:
            print(f"Сорт '{flavor}' не найден!")
    
    def check_flavor(self, flavor):
        return flavor in self.flavors
    
    def show_ice_types(self):
        print("\nТипы мороженого и сорта:")
        for ice_type, flavors in self.ice_cream_types.items():
            if flavors:
                print(f"{ice_type.capitalize()}: {', '.join(flavors)}")

# Пример использования
cafe = IceCreamStand("Морожко", "ул. Ленина, 1", "10:00-22:00")
cafe.add_flavor("фисташковое", "мягкое")
cafe.add_flavor("пломбир", "на палочке")
cafe.add_flavor("крем-брюле", "в стаканчике")

print("\nПроверка сорта 'фисташковое':", cafe.check_flavor("фисташковое"))
cafe.show_ice_types()