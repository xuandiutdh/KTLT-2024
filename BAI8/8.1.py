print("Nguyễn Xuân Dịu")
print("235752021610078")



import turtle

window = turtle.Screen()
# Đặt màu nền cho cửa sổ
window.bgcolor("lightgreen") 

painter = turtle.Turtle()
# Đặt màu tô bên trong là màu xanh dương
painter.fillcolor('blue')
# Đặt màu đường vẽ là màu xanh dương
painter.pencolor('blue')
# Đặt kích thước của bút vẽ là 3
painter.pensize(3)         

# Hàm vẽ hình vuông
def drawsq(t, s):
    for i in range(4):
        # Di chuyển về phía trước một khoảng s
        t.forward(s)
          # Quay trái 90 độ để tạo một góc của hình vuông
        t.left(90)   

# Vẽ nhiều hình vuông xoay dần
for i in range(1, 180):
    # Quay con rùa sang trái 18 độ
    painter.left(18)
    # Vẽ một hình vuông có cạnh 200 pixel
    drawsq(painter, 200)   
# Giữ cửa sổ mở cho đến khi người dùng đóng
turtle.done()  