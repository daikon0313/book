# x_list = []
# for x in range(5):
#     x_list.append(x/10)

# print(x_list)

# x_list = [x/10 for x in range(5)]
# print(x_list)

# num = [3,4,5,6,7]
# even_num = [n for n in num if n % 2 == 0]
# print(even_num)

x_list = [2,5,9]
y_list = [100, 1000, 100]
z_list = [x+y for x, y in zip(x_list, y_list)]
print(z_list)
