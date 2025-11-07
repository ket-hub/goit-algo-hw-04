from pathlib import Path
import re

with open('zarplata.txt', 'w', encoding='utf-8') as fh:
    fh.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')

def total_salary(path):
    path = Path(path)
    if path.exists():
        with open(path, 'r', encoding='utf-8') as fh:
            content = fh.read()
            matches = re.findall(r"\d+", content)
            salaries = [int(num) for num in matches]
            total = sum(salaries)
            average = total // len(salaries)
            return (total, average)
    else:
        print(f'Файл {path} не існує')    

print(total_salary('zarplata.txt'))



               

      
        
    




