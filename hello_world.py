
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


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# print("The following languages have been mentioned:")

# for language in set(favorite_languages.values()):
#     print(language.title())

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# print(len(aliens))
# name = input("Please enter your name: ")
# print("Hello, " + name + "!")


# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name 11
# = input(prompt)

# print("\nHello, " + name + "!")

# age = input("how old are you ")
# age = int(age)
# print(age > 18)


# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print("\nThe number " + str(number) + " is even.")
# else:
#     print("\nThe number " + str(number) + " is odd.")

# current_number = 1

# while current_number <= 10:
#     print(current_number)
#     current_number += 1
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' when you are done. "

# message = ""

# while message != "quit":
#     message = input(prompt)

#     if message != "quit":
#         print(message)

# active = True

# while active:
#     message = input(prompt)

#     if message == "quit":
#         active = False
#     else:
#         print(message)

# while True:
#     city = input(prompt)

#     if (city == "quit"):
#         break
#     else:
#         print("i would like to go to ", city.title() + "!")

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("verifying ", current_user.title())
#     confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
# responses = {}

# polling_active = True

# while polling_active:
#     name = input("please enter your name\n")
#     response = input("which is your favorite mountain?\n")

#     responses[name] = response

#     repeat = input("would you like to let another person respond? (y/n): ")

#     if repeat == "n":
#         polling_active = False

# print("\n -- Results --")
# for name, response in responses.items():
#     print(name + "'s favorite mountain is" + response.title())
