
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# age_0 = 22
# age_1 = 18

# age_1 = 23

# if age_0 >= 22 and age_1 >= 22:
#     print('both are adults')

# requested_toppings = ['mushrooms', 'onions', 'pineapple']

# if 'a' not in requested_toppings:
#     print('yes, a is not in requested')

# else:
#     print('a are requested')


# age = 12

# if age < 4:
#     print('too many children')
# elif age < 12:
#     print('teenagers')
# else:
#     print('adults')


# alien_0 = {'color': 'green', 'points': 5}
# alien_0['x_position'] = 0

# del alien_0['color']
# print(alien_0)


# list = ['a', 'b', 'c', 'd', 'e', 'f']

# del list[0]

# print(list)


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }

# user_0 = {
#     'username': 'efermi', 'first': 'enrico', 'last': 'fermi',
# }

# print(user_0.items())

# for key, value in user_0.items():
#     print('\nKey: ', key)
#     print('Value: ', value)

# for item in user_0.items():
#     print(item)

# for value in user_0.values():
#     print(value.title())


favorite_languages = {'jen': 'python', 'sarah': 'c',
                      'edward': 'ruby', 'phil': 'python', }
print("The following languages have been mentioned:")

for language in (favorite_languages.values()):
    print(language.title())
