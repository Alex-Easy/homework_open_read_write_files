import pprint


def create_cook_book(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            cook_book[dish_name] = []
            number_of_ingredients = int(file.readline().strip())
            for i in range(number_of_ingredients):
                ingredients_info = file.readline().strip().split(' | ')
                name_of_ingredient = ingredients_info[0]
                quantity_of_ingredient = int(ingredients_info[1])
                measure_of_ingredient = ingredients_info[2]
                ingredients = {
                    'ingredient_name': name_of_ingredient,
                    'quantity': quantity_of_ingredient,
                    'measure': measure_of_ingredient
                }
                cook_book[dish_name].append(ingredients)
            file.readline()
    return cook_book


cook_book_result = create_cook_book('recipes.txt')


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book_result:
            ingredients = cook_book_result[dish]
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                if name not in shop_list:
                    shop_list[name] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
                else:
                    shop_list[name]['quantity'] += ingredient['quantity'] * person_count
    return shop_list


result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint.pprint(result)
