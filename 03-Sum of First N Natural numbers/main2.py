a = int(input("Enter a number: "))

def getsum(num):
    if num == 1:
        return 1
    return num + getsum(num - 1)
print(getsum(a))                                                        