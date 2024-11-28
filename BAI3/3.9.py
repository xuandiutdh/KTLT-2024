print("Nguyễn Xuân Dịu")
print("235752021610078")
import math

def add(x, y):
    return x + y

# Hàm trừ hai số
def subtract(x, y):
    return x - y

# Hàm nhân hai số
def multiply(x, y):
    return x * y

# Hàm chia hai số
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Lấy lựa chọn từ người dùng
choice = input("Enter choice (1/2/3/4): ")

# Lấy hai số từ người dùng
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Thực hiện phép tính dựa trên lựa chọn
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid input")
