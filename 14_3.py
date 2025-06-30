import tkinter as tk
from tkinter import messagebox

class IceCreamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Кафе-мороженое")
        
        # Данные
        self.stand = IceCreamStand("Sweet Dreams", "ул. Пушкина, 3", "09:00-23:00")
        self.stand.add_flavor("ванильное")
        self.stand.add_flavor("шоколадное")
        
        # Интерфейс
        self.label = tk.Label(root, text="Добро пожаловать в кафе-мороженое!")
        self.label.pack(pady=10)
        
        self.flavor_list = tk.Listbox(root)
        for flavor in self.stand.flavors:
            self.flavor_list.insert(tk.END, flavor)
        self.flavor_list.pack()
        
        self.add_button = tk.Button(root, text="Добавить сорт", command=self.add_flavor)
        self.add_button.pack(pady=5)
        
        self.remove_button = tk.Button(root, text="Удалить сорт", command=self.remove_flavor)
        self.remove_button.pack(pady=5)
    
    def add_flavor(self):
        flavor = simpledialog.askstring("Добавить", "Введите новый сорт:")
        if flavor:
            self.stand.add_flavor(flavor)
            self.flavor_list.insert(tk.END, flavor)
    
    def remove_flavor(self):
        selected = self.flavor_list.curselection()
        if selected:
            flavor = self.flavor_list.get(selected)
            self.stand.remove_flavor(flavor)
            self.flavor_list.delete(selected)
        else:
            messagebox.showwarning("Ошибка", "Выберите сорт для удаления!")

if __name__ == "__main__":
    root = tk.Tk()
    app = IceCreamApp(root)
    root.mainloop()