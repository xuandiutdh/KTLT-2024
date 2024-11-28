print("Nguyễn Xuân Dịu")
print("235752021610078")

def filter_odd_numbers(s):
    odd_numbers = [num for num in s if num % 2 != 0]
    return odd_numbers


s1 = input("Nhập danh sách các số, phân tách bằng dấu phẩy: ")
s = list(map(int,s1.split(',')))


odd_numbers = filter_odd_numbers(s)
print(f"Các số lẻ là: {odd_numbers}")
