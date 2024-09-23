# Taking the number from the user
num = int(input("Enter a number: "))

# List of all odd numbers under the input value
odd_numbers_under_input = [i for i in range(num) if i % 2 != 0]

# List of odd numbers up to the input value
all_odd_numbers = [i for i in range(1, num+1, 2)]

print("List of odd numbers under the input value:", odd_numbers_under_input)
print("List of all odd numbers up to the input value:", all_odd_numbers)

# List of fruits
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Capitalizing the first letter of each fruit using list comprehension
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original list of fruits:", fruits)
print("List of fruits with first letter capitalized:", capitalized_fruits)