immutable_var = 1, 3, False, 'Матрица', 'System'
print(immutable_var)
# print(immutable_var[3])
# immutable_var[3] = 'off'
# print(immutable_var)
# Изменить элементы кортежа нельзя, потому что кортеж не поддерживает обращение к элементам, т.е. они неизменяемые.
# Если внутри кортежа есть элемент ввиде списка, то элементы самого списка менять можно.
# Например: name = ([a, b, c], 5, 6, 7) меняем name[0][1] = x, получим ([a, x, c], 5, 6, 7)
mutable_list =['A', 1, 25, 'matrix']
print(mutable_list)
mutable_list.append(True)
print(mutable_list)
mutable_list[3] = 'sport'
print(mutable_list)
mutable_list.extend(['boll'])
print(mutable_list)
