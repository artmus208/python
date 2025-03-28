


def some_list_op(l: list):
    print(f"id в функции: {id(l)}")
    l[0] = 0
    print(f"id в функции после изменения: {id(l)}")
    
l = [5, 2]
print(f"id до вызова функции: {id(l)}")
some_list_op(l)


def some_int_op(i: int):
    print(f"id числа в функции: {id(i)}")
    i = 32
    print(f"id числа в функции после изменения: {id(i)}")
    
i = 52
print(f"id числа до вызова функции: {id(i)}")
some_int_op(i)