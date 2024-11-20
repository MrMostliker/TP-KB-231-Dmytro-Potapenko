students = [
    {'name': 'Kyrylo', 'score': 85},
    {'name': 'Dmytro', 'score': 92},
    {'name': 'Maxim', 'score': 78},
    {'name': 'Sofia', 'score': 88}
]


sorted_by_name = sorted(students, key=lambda x: x['name'])
print("Сортування за ім'ям:", sorted_by_name)


sorted_by_score = sorted(students, key=lambda x: x['score'], reverse=True)
print("Сортування за оцінкою:", sorted_by_score)
