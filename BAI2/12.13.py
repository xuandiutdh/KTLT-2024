print("Nguyễn Xuân Dịu")
print("235752021610078")
import math

# Nhập các hệ số a, b, c từ bàn phím
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Kiểm tra hệ số a
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        # Giải phương trình bậc nhất bx + c = 0
        x = -c / b
        print(f"Phương trình có một nghiệm: x = {x}")
else:
    # Tính delta
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("Phương trình vô nghiệm (delta < 0).")
    elif delta == 0:
        # Nghiệm kép
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        # Hai nghiệm phân biệt
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
