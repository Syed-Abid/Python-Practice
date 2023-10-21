# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This Program illustrates a chaotic funtion")
    x = eval(input("Enter a number betwen 0 and 1:"))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()

        

