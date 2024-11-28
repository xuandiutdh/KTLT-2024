print("Nguyễn Xuân Dịu")
print("235752021610078")
# File: main.py

from sort_module import bubbleSort

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các giá trị của danh sách
nlist = []
for i in range(n):
    value = int(input(f"Nhập giá trị phần tử thứ {i + 1}: "))
    nlist.append(value)

# Sắp xếp danh sách
sorted_list = bubbleSort(nlist)

# In kết quả
print("Danh sách đã sắp xếp:", sorted_list)
