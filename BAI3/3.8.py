print("Nguyễn Xuân Dịu")
print("235752021610078")
def calculate_distance(movements):
    # Khởi tạo vị trí ban đầu
    x, y = 0, 0
    
    # Xử lý từng bước di chuyển
    for movement in movements:
        direction, steps = movement.split()
        steps = int(steps)  # Chuyển đổi số bước sang kiểu int
        
        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps
    
    # Tính khoảng cách từ điểm hiện tại đến điểm ban đầu
    distance = round((x**2 + y**2) ** 0.5)  # Tính khoảng cách Euclidean và làm tròn
    
    return distance

# Nhập dữ liệu từ người dùng
movements_input = []
while True:
    movement = input("Nhập hướng di chuyển (hoặc 'STOP' để kết thúc): ")
    if movement == "STOP":
        break
    movements_input.append(movement)

# Tính toán khoảng cách
result = calculate_distance(movements_input)
print("Khoảng cách đến vị trí ban đầu là:", result)
