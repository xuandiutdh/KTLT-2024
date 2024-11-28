print("Nguyễn Xuân Dịu")
print("235752021610078")
a = "Hello Guy!"

def say():
    global a  # Khai báo biến a là biến toàn cục
    a = " Vinh University "  # Thay đổi giá trị của biến toàn cục a
    print(a)

say()  # Gọi hàm say
print(a)  # In giá trị của biến a sau khi gọi hàm say
