print("Nguyễn Xuân Dịu")
print("235752021610078")
def calculate_balance():
    balance = 0
    transactions = []

    while True:
        transaction = input("Nhập nhật ký giao dịch (D số hoặc W số), hoặc nhấn Enter để kết thúc: ")
        
        if not transaction:  
            break

        action, amount = transaction.split()
        amount = int(amount)

        if action == 'D':  
            balance += amount
        elif action == 'W':  
            balance -= amount

    return balance


final_balance = calculate_balance()
print(f"Số dư cuối cùng: {final_balance}")
