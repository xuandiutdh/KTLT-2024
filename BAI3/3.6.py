print("Nguyễn Xuân Dịu")
print("235752021610078")
def get_sum(*num):
    tmp = 0
    # Duyệt qua các tham số
    for i in num:
        tmp += i
    return tmp

result = get_sum(1, 2, 3, 4, 5)
print(result)
