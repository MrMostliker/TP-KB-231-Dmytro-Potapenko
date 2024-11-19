import bisect

sorted_list = [1, 3, 5, 7, 9]
print("Поточний список:", sorted_list)
new_value = int(input("Введіть нове значення:"))

position = bisect.bisect_left(sorted_list, new_value)
print("Список з новим елементом:", sorted_list[:position] + [new_value] + sorted_list[position:])
