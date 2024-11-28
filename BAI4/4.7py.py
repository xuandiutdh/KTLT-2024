print("Nguyễn Xuân Dịu")
print("235752021610078")
input_string = input("Nhập chuỗi: ")

new_string = ''.join([char for char in input_string if not char.isdigit()])

print("Chuỗi mới:", new_string)
