n=int(input("Enter a number"))
if (n % 2) != 0:
   print("Weird")
elif (n % 2) == 0 and n in range(3,6):
    print("Not Weird")
elif (n % 2) == 0 and n in range(7,21):
   print("Weird")
elif (n % 2) == 0 and n > 20:
   print("Not Weird")


