def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path,'r') as file:
            for content in file:
                list = content.strip().split(',')
                if len(list) > 1:
                    try:
                        num = float(list[1])
                        total += num
                        count += 1
                    except ValueError:
                        print(f'Заробітня плата не число {list[1]}')
                else:
                    print('Рядок не містить достатньо елемантів')                    
            if count > 1:
                average = total / count
                print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except FileNotFoundError:
        print(f'Файл за шляхом {path} не знайдено')
    except Exception as e:
        print(f"Сталася помилка: {e}")
        

total_salary('salary.txt')