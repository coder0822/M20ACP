#Create a list of square value of numbers between specified range by the user, and then seperate the odd and even values.
def get_square_range(start, end):
    squares = [i**2 for i in range(start, end+1)]
    odd_squares = [square for square in squares if square % 2!= 0]
    even_squares = [square for square in squares if square % 2 == 0]
    return odd_squares, even_squares

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
odd, even = get_square_range(start, end)
print("Odd")
#Write a function that accepts beginning and end range of numbers, and find the square values of those numbers. Then filter the odd and even sqaure values and print them.
def square_range(start, end):
    squares = [i**2 for i in range(start, end+1)]
    even_squares = [i for i in squares if i % 2 == 0]
    odd_squares = [i for i in squares if i % 2!= 0]
    print("Even Squares:", even_squares)
    print("Odd Squares:", odd_squares)