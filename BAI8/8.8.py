print("Nguyễn Xuân Dịu")
print("235752021610078")
import tkinter as tk
from tkinter import messagebox

# Phần a: Form thông tin cá nhân
def show_personal_info():
    info = (
        f"Họ và tên: {entry_name.get()}\n"
        f"Ngày sinh: {entry_dob.get()}\n"
        f"MSSV: {entry_student_id.get()}\n"
        f"Ngành học: {entry_major.get()}"
    )
    messagebox.showinfo("Thông tin cá nhân", info)

# Phần b: Xử lý sự kiện khi bấm vào nút "Click Me"
def show_selected_option():
    selected = radio_var.get()
    if selected == 1:
        message = "Bạn đã chọn nút First (1)"
    elif selected == 2:
        message = "Bạn đã chọn nút Second (2)"
    elif selected == 3:
        message = "Bạn đã chọn nút Third (3)"
    else:
        message = "Chưa chọn nút nào"
    messagebox.showinfo("Lựa chọn của bạn", message)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Thông tin cá nhân và Lựa chọn")

# Phần a: Form thông tin cá nhân
frame_info = tk.Frame(root)
frame_info.pack(pady=10)

tk.Label(frame_info, text="Họ và tên:").grid(row=0, column=0, sticky="e")
entry_name = tk.Entry(frame_info)
entry_name.grid(row=0, column=1)

tk.Label(frame_info, text="Ngày sinh:").grid(row=1, column=0, sticky="e")
entry_dob = tk.Entry(frame_info)
entry_dob.grid(row=1, column=1)

tk.Label(frame_info, text="MSSV:").grid(row=2, column=0, sticky="e")
entry_student_id = tk.Entry(frame_info)
entry_student_id.grid(row=2, column=1)

tk.Label(frame_info, text="Ngành học:").grid(row=3, column=0, sticky="e")
entry_major = tk.Entry(frame_info)
entry_major.grid(row=3, column=1)

btn_show_info = tk.Button(frame_info, text="Hiển thị thông tin", command=show_personal_info)
btn_show_info.grid(row=4, columnspan=2, pady=5)

# Phần b: Form lựa chọn radio button
frame_options = tk.Frame(root)
frame_options.pack(pady=10)

radio_var = tk.IntVar()

tk.Label(frame_options, text="Welcome").pack(side="left", padx=5)

tk.Radiobutton(frame_options, text="First", variable=radio_var, value=1).pack(side="left")
tk.Radiobutton(frame_options, text="Second", variable=radio_var, value=2).pack(side="left")
tk.Radiobutton(frame_options, text="Third", variable=radio_var, value=3).pack(side="left")

btn_click_me = tk.Button(frame_options, text="Click Me", command=show_selected_option)
btn_click_me.pack(side="left", padx=5)

# Chạy vòng lặp chính
root.mainloop()
