def create_ru_en_dict(input_file, output_file):
    translations = {}
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if ' - ' in line:
                en, ru = line.strip().split(' - ')
                ru_words = [word.strip() for word in ru.split(',')]
                for word in ru_words:
                    if word not in translations:
                        translations[word] = set()
                    translations[word].add(en)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in sorted(translations):
            f.write(f"{word} -- {', '.join(sorted(translations[word]))}\n")

create_ru_en_dict("en-ru.txt", "ru-en.txt")