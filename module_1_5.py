immutable_var = (12, "Urban", [True, 1.2])
print(immutable_var)
# immutable_var[0] = 1 Вылезет ошибка т.к. кортеж неизменяем
immutable_var[-1][0] = False # Но если элемент кортежа изменяем, то этот элемент можно поменять
mutable_list = ["", 3.14, None]
mutable_list[0] = -2
print(mutable_list)