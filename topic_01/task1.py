input_string = input("Write your line here:")

def reverse(input_string):
    return input_string[::-1]

reversed_string = reverse(input_string)
print("Raw line:", input_string)
print("Reversed line:", reversed_string)