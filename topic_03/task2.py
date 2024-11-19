list0 = [5, 3, 8, 1, 2] 
print("Початковий список:", list0)

list0.extend([6, 7, 9])
print("extend() додає всі елементи іншого списку до кінця:", list0)

list0.append(10)
print("append() додає один елемент до кінця:", list0)

list0.insert(2, 15)
print("insert(2, 15) вставляє 15 у позицію 2:", list0)

list0.remove(3)
print("remove(3) видаляє перше входження числа 3:", list0)

list0.clear()
print("clear() очищає список:", list0)

list0 = [5, 3, 8, 1, 2]
print("\nоновлений список для подальшого тестування:", list0)

list0.sort()
print("sort() сортує список за зростанням:", list0)

list0.reverse()
print("reverse() змінює порядок елементів на протилежний:", list0)

list_copy = list0.copy()
print("copy() створює копію списку:", list_copy)
