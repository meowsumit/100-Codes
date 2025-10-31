num1 = int(input("Enter the 1st num "))
num2 = int(input("Enter the 2nd num "))
num3 = int(input("Enter the 3rd num "))

if num1>num2 or num1>num3:
  print(f"{num1} is largest")
elif num2>num1 or num2>num3:
  print(f"{num2} is largest")
else:
  print(f"{num3} is largest")