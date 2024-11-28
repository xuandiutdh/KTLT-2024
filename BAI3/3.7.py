print("Nguyễn Xuân Dịu")
print("235752021610078")
def check_even_or_odd(number):
    if number % 2 == 0:
        print("Đây là một số chẵn")
    else:
        print("Đây là một số lẻ")

# Nhập số nguyên từ người dùng
try:
    user_input = int(input("Nhập một số nguyên: "))
    check_even_or_odd(user_input)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
