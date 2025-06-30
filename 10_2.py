from PIL import Image

holidays = {
    "Новый год": "new_year.jpg",
    "8 Марта": "womens_day.jpg",
    "День рождения": "birthday.jpg"
}

def show_holiday_card():
    holiday = input("К какому празднику нужна открытка? (Новый год/8 Марта/День рождения): ")
    if holiday in holidays:
        try:
            img = Image.open(holidays[holiday])
            img.show()
        except FileNotFoundError:
            print("Открытка не найдена!")
    else:
        print("Праздник не распознан")

show_holiday_card()