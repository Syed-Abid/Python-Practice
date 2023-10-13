#Program to print Alphabet Rangoli
import string 
def print_rangoli(size):
    n=int(input("Enter the number:"))
    width = 4 * size - 3
    alpha = string.ascii_lowercase
    for i in list(range(size))[::-1] + list(range(1, size)):
        print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))

print_rangoli(5)