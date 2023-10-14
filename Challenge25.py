#Program to input a lowercase string and print a uppercase string
s=list(map(str,input("ENTER THE STRING:").split()))

for i in (range(len(s))):
    if s[i].islower():
        print(s[i].upper(),end="")

    else:
        print("NO need")