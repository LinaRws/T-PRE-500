user_input = input("Please enter a string: ")

# Double each character in the string
doubled_string = ''.join(char * 2 for char in user_input)

# Display the doubled string
print("Doubled string:", doubled_string)
