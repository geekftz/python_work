# def greet_user(username: str):
#     print("hello! " + username.title())
#     return username


# if __name__ == "__main__":
#     greet_user("fanta")

# def describe_pet(animal_type, pet_name):
#     # """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# def describe_pet(pet_name, animal_type="dog"):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet()
# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()


# print("a b".title())
# print("ab".title())

# while True:
#     print("\nPlease tell me your name:")
#     print("enter 'q' at any time to quit")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

def make_pizza(*toppings):
    print(toppings)
    for topping in toppings:
        print(topping)


# make_pizza('pepperoni', True, [1, 2, 3])
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def build_profile(first, last, **user_info):
#     # print(user_info.items())
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile


# user_profile = build_profile('albert', 'einstein', location='princeton',
#                              field='physics')
# print(user_profile)
