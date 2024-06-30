size = int(input("Enter the size of the pattern: "))

column = size
while size:
    for _ in range(column):
        print("*",end="")
    print()
    size -= 1