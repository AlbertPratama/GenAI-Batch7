

# def keywords(n):
#     if n < 1:
#         print('Salah')
#     else:
#         for i in range(1, n+1):
#             print('+')


# keywords(int(input('enter: ')))


# def keywords(n):
#   deret = []
#   for numn in n:
#     if numn % 2 == 0 and n !=0:
#       deret.append(numn)
#   return deret


# n = int(input('input angka: ').split)
# res = keywords(n)
# print(res)


# def even(numbers):
#   """Returns a list of even numbers from the input string."""
#   even_numbers = []
#   for num in numbers.split():  # Split the input string by spaces
#     try:
#       number = int(num)  # Attempt to convert each item to an integer
#       if number % 2 == 0 and number != 0:  # Check if even and non-zero
#         even_numbers.append(number)
#     # Handle cases where conversion fails (non-numeric input)
#     except ValueError:
#       pass  # Do nothing, ignore non-numeric input
#   return even_numbers


# # Get input from the user
# input_string = input("Masukkan deret angka (pisahkan dengan spasi): ")

# # Find even numbers
# result = even(input_string)

# # Print the result
# print("Bilangan genap:", result)


# Working area
def triangle(p, l):
    return round(p*l)


def rectangle(a, t):
    return round(a*t/2)


mode = input('''
                1. Persegi
                2. Segitiga
              ''')
n1 = int(input('N1: '))
n2 = int(input('N2: '))
if mode == "1":
    print(rectangle)
elif mode == "2":
    print(triangle)
