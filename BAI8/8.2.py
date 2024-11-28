print("Nguyễn Xuân Dịu")
print("235752021610078")

import turtle, random

# Tạo danh sách màu
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Tạo đối tượng turtle
painter = turtle.Turtle()
# Đặt độ dày bút vẽ là 3
painter.pensize(3)  

# Vòng lặp vẽ các hình tròn xoay dần
for i in range(10):
    # Chọn ngẫu nhiên một màu từ danh sách
    color = random.choice(colors)
    # Đặt màu cho bút vẽ
    painter.pencolor(color)
    # Vẽ một hình tròn bán kính 100
    painter.circle(100)
    # Xoay phải 30 độ
    painter.right(30)
    # Xoay trái 60 độ
    painter.left(60)
    # Đặt vị trí của rùa về tọa độ gốc (0, 0)
    painter.setposition(0, 0) 
# Giữ cửa sổ mở cho đến khi người dùng đóng nó
turtle.done()  
