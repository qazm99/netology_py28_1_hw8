# Фильтр только целые положительные числа
def posintput(string):
    while True:
        integer = input(string)
        if integer.isdigit():
            return int(integer)
        else:
            print("Нужно ввести целое положительное число")

# Чтение файла и запись кулинарной книги в словарь
def read_from_file(file):
    with open(file, encoding='utf8') as file:
        current_read_status = 'dish'
        current_dish = ''
        current_food_count = 0
        food_atributs = []
        for line in file:
            if current_read_status == 'dish' and line.strip() != '':
                current_dish = line.strip('\n')
                current_dish_list = []
                current_read_status = 'food_count'
            elif current_read_status == 'food_count':
                current_food_count = int(line)
                current_read_status = 'food_in_dish_list'
            elif current_read_status == 'food_in_dish_list':
                food_atributs = line.split(' | ')
                current_dish_list.append({'ingredient_name': food_atributs[0], 'quantity': float(food_atributs[1]),
                                          'measure': food_atributs[2].strip('\n')})
                current_food_count -= 1
                if current_food_count == 0:
                    cook_book[current_dish] = current_dish_list
                    current_read_status = 'dish'

# Составляем список покупок, учитывая блюда и количество персон
def get_shop_list_by_dishes(dishes, person_count):
    all_ingredients = {}
    for dish in dishes:
        if cook_book.get(dish) != None:
            for food in cook_book.get(dish):
                if all_ingredients.get(food['ingredient_name']) != None:
                    # print(food['ingredient_name'])
                    new_count_food = food['quantity'] + all_ingredients.get(food['ingredient_name']).get('quantity')
                    all_ingredients[food['ingredient_name']] = {'measure': food['measure'], 'quantity': new_count_food}
                else:
                    all_ingredients[food['ingredient_name']] = {'measure': food['measure'],
                                                                'quantity': food['quantity']}
        else:
            print(f'Блюда {dish} нет в нашей кулинарной книге')

        # for food, food_atributs in cook_book:
        #     all_ingredients.update({})
        # all_ingredients_list.append(cook_book.get(dish))
    print('Для приготовления нам понадобится: ')
    for ingredient in all_ingredients:
        measure = all_ingredients[ingredient]['measure']
        quantity = all_ingredients[ingredient]['quantity'] * person_count
        all_ingredients.update({ingredient: {'measure': measure, 'quantity': quantity}})
        print(f'{ingredient}: {all_ingredients[ingredient]["quantity"]} {all_ingredients[ingredient]["measure"]}')


def main():
    while True:
        if input('\nПрочитаем файл?(Да/Нет)').upper() != 'ДА':
            print('Программа остановлена')
            break
        read_from_file('recipes.txt')
        print("Блюда в кулинарной книге:")
        for dish in cook_book:
            print(f'\nБлюдо: {dish}')
            for food in cook_book[dish]:
                print(f'  {food["ingredient_name"]} {food["quantity"]} {food["measure"]}')

        # print()
        # print('')
        # print(cook_book)
        if input('\nНакроем стол?(Да/Нет)').upper() == 'ДА':
            get_shop_list_by_dishes(input('Введите названия блюд через пробел: ').split(),
                                    posintput('Введите количество персон: '))


if __name__ == '__main__':
    cook_book = {}
    main()
