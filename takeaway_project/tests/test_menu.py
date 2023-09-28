



# """
# When adding a dish to a menu
# menu stores it in a list
# """
# def test_adding_dish_to_menu_mock():
#     menu = Menu()
#     dish = Dish("name")
#     menu.add(dish)
#     assert menu._all_dishes == [dish]

# """
# When adding two dishes to a menu
# we can see a list of all dishes and their prices
# """
# def test_show_all_lists_dishes_with_prices_mock():
#     menu = Menu()
#     moussaka = Dish("Moussaka")
#     fattoush = Dish("Fattoush Salad")
#     moussaka.set_price(12.5)
#     fattoush.set_price(9.0)
#     menu.add(moussaka)
#     menu.add(fattoush)
#     assert menu.show_all() == ["Moussaka £12.5", "Fattoush Salad £9.0"]