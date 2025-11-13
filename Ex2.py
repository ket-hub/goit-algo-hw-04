from pathlib import Path
import re

with open("text.txt", "w", encoding="utf-8") as file:
        file.write('60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5')

def get_cats_into(path):
    path = Path(path)
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file: #кожна змінна line — це один рядок з текстового файлу, тобто все до символу \n (переносу рядка).
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats.append({
                        "ID" : cat_id,
                        "NAME": name,
                        "AGE": int(age)
                    
                    })
                except ValueError:
                    print(f"Пропущено рядок через помилку формату: {line.strip()}")

    except FileNotFoundError:
        print("Файл не знайдено.")
    except PermissionError:
        print("Немає доступу до файлу.")
    return cats

cats = get_cats_into("text.txt")
print(cats)



