import random

for _ in range(10):
    print("Hello!")

list_names = []
for _ in range(5):
    list_names.append(input("Please input a name\n=> "))
print(list_names)

list_name_lower = []
for v in list_names:
    list_name_lower.append(v.lower())
print(list_name_lower)

even_strings = []
for i in list_name_lower:
    if len(i) % 2 == 0:
        even_strings.append(i)

print(even_strings)