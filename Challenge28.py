#Program to take string as input and then divide it into certain length of substring and remove 
#repeating characters,then print it.
import math
import textwrap
from collections import OrderedDict
string, k = input("Enter the string:"), int(input("Enter the value:"))
chunks, chunk_size = len(string), len(string)//k
word_list=textwrap.wrap(string,chunk_size)
for element in word_list:
    print("".join(OrderedDict.fromkeys(element)))



    