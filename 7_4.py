group1 = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов"]
group2 = ["Федоров", "Васильев", "Николаев", "Алексеев", "Дмитриев"]

team = tuple(group1[:3] + group2[:2])

print("Исходные списки групп:")
print("Группа 1:", group1)
print("Группа 2:", group2)
print("\nСпортивная команда:", team)
print("Длина кортежа:", len(team))
print("Отсортированный кортеж:", sorted(team))
print("Входит ли 'Иванов' в команду?", "Иванов" in team)
print("Количество 'Иванов' в команде:", team.count("Иванов"))