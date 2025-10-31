num1 = int(input("Enter the 1st num "))
num2 = int(input("Enter the 2nd num "))

def recsum(sum, num1, num2):
    if num1 > num2 :
        return sum
    return num1 + recsum(sum, num1+1, num2) 
print(recsum(sum, num1, num2))