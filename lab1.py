import math

print(math.pi)

radius = 5
area = math.pi * radius ** 2
volume = (4 / 3) * math.pi * radius ** 3

radius = 3
side_a = 3
side_b = 4
side_c_sq = side_a ** 2 + side_b ** 2
side_c = int(math.sqrt(side_c_sq))

first_name = "Jackson"
last_name = "Dehority"
my_name = first_name + " " + last_name
name_len = len(first_name) + len(last_name)

my_name_uc = my_name.upper()
my_name_lc = my_name.lower()

age = 18
weight: float = 120.0
height = 70
bmi = (weight / height ** 2) * 703

print(area)
print(volume)
print(side_c)
print(my_name)
print(name_len)
print(type(age), type(weight), type(height))
print(bmi)
