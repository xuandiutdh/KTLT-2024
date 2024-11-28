print("Nguyễn Xuân Dịu")
print("235752021610078")

input_string = input("Nhập chuỗi các số nhị phân (cách nhau bởi dấu phẩy): ")


binary_numbers = input_string.split(',')


print("Các số nhị phân đã nhập là:")
for binary in binary_numbers:
    print(binary.strip())  
