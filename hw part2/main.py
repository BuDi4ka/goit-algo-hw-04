def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for lines in file:
                dict_el = lines.strip().split(',')
                if dict_el:
                    cat_dict = {
                        "id": dict_el[0].strip(),
                        "name": dict_el[1].strip(),
                        "age": dict_el[2].strip()
                    }
                    cats_list.append(cat_dict)
                else:
                    print('Виконная функції не є можливим')
    except FileNotFoundError:
        print(f'Файл з адресом: {path}, не знайдено')
    except Exception as e:
        print(f'При виконанні виявилась наступна помилка - {e}')
    return cats_list

print(get_cats_info('hw part2/cats.txt'))