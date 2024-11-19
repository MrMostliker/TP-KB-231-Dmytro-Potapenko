dict0 = {"a": 1, "b": 2, "c": 3}
print("Початковий словник:", dict0)

dict0.update({"d": 4, "a": 10})
print("update({'d': 4, 'a': 10}) додає нові пари і оновлює існуючі ключі:", dict0)

del dict0["b"]
print("del dict0['b'] видаляє пару з ключем 'b':", dict0)

dict0.clear()
print("clear() очищає словник:", dict0)

dict0 = {"x": 5, "y": 10, "z": 15}
print("\nоновлений словник для подальшого тестування:", dict0)

print("keys() повертає всі ключі:", dict0.keys())

print("values() повертає всі значення:", dict0.values())

print("items() повертає всі пари ключ-значення:", dict0.items())
