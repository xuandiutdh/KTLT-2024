print("Nguyễn Xuân Dịu")
print("235752021610078")
# File: main.py

import mymodule

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các giá trị của danh sách
numbers = []
for i in range(n):
    value = float(input(f"Nhập giá trị phần tử thứ {i + 1}: "))
    numbers.append(value)

# Tìm giá trị lớn nhất và nhỏ nhất
max_value, min_value = mymodule.find_max_min(numbers)

# Sắp xếp danh sách
sorted_numbers = mymodule.sort_list(numbers)

# In kết quả
print(f"Giá trị lớn nhất: {max_value}")
print(f"Giá trị nhỏ nhất: {min_value}")
print(f"Danh sách đã sắp xếp: {sorted_numbers}")
