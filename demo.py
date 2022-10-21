# def make_shirt(shirt_size, shirt_print):
#     print(f"Размер футболки - {shirt_size}.")
#     print(f"Принт на футболке - {shirt_print}.")
#
#
# make_shirt("XL", "Summer")
# make_shirt(shirt_print="Spring", shirt_size="L")

# def make_shirt(shirt_size="L", shirt_print="I love Python"):
#     print(f"Размер футболки - {shirt_size}.")
#     print(f"Принт на футболке - {shirt_print}.")
#
#
# make_shirt()
# make_shirt(shirt_print="Art", shirt_size="M")

# def describe_city(name_of_city, name_of_country="Kyrgyzstan"):
#     print(f"{name_of_city.title()} is in {name_of_country.title()}")
#
#
# describe_city("Bishkek")
# describe_city("New York", "USA")
# describe_city("Moscow", "Russia")

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# list = ['Dastan', 'Almaz', 'Akyl']
# name = input()
# if name in list:
#     print(list)

# num1 = int(input(' '))
# num2 = int(input(' '))
# print(num1 + num2)

def num(n):
   return int(n) == float(n)
print(num(2))
print(num(2.2))
