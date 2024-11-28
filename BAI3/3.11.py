print("Nguyễn Xuân Dịu")
print("235752021610078")
def benefit(t, n, k):
    # Tính số tiền nhận được sau k tháng
    total_amount = n * (1 + t/100)**k
    return total_amount

# Nhập lãi suất, số vốn ban đầu và số tháng gửi
t = float(input("Nhập lãi suất (%/tháng): "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))

# Gọi hàm và in kết quả
result = benefit(t, n, k)
print(f"Số tiền nhận được sau {k} tháng là: {result:.2f}")
