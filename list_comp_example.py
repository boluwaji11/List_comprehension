# classic way
old_list = [1, 2, 3, 4, 5]
new_list = []

for i in old_list:
    i = i ** 2
    new_list.append(i)

print(new_list)

new_list = [i**2 for i in old_list]
print(new_list)