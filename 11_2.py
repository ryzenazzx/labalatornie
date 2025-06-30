import os

def check_files(folder, extensions):
    for file in os.listdir(folder):
        if file.lower().endswith(extensions):
            print(f"Обрабатывается: {file}")
        else:
            print(f"Пропущен: {file} (неподходящий формат)")

check_files("documents", ('.txt', '.csv'))