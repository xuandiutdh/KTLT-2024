print("Nguyễn Xuân Dịu")
print("235752021610078")
from tkinter import *

# a, Tạo cửa sổ đồ họa
window = Tk()
window.title("Welcome to LikeGeeks app")
# Đặt kích thước cửa sổ
window.geometry('350x200')   

# Thêm nhãn (Label) với nội dung ban đầu là "Hello"
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

# Hàm xử lý sự kiện khi nhấn nút
def clicked():
    # c, Thay đổi nội dung của nhãn khi nhấn nút
    lbl.configure(text="Button was clicked!!")  

# b, Thêm nút bấm (Button), Nút có màu nền xanh và chữ trắng
btn = Button(window, text="Click Me", command=clicked, bg="blue", fg="white") 
btn.grid(column=1, row=0)

# Khởi động vòng lặp chính của cửa sổ
window.mainloop()
