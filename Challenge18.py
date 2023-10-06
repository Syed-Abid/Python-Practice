def count_substring(string, sub_string):
    c=0
    string=str(input("Enter a string:"))
    sub_string=str(input("Enter a substring:"))
    for i in range(0,len(string)):
        if string[i:].startswith(sub_string):
            c=c+1
    return c

count_substring(" ", " ")
