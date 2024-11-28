print("Nguyễn Xuân Dịu")
print("235752021610078")
import tkinter as tk

def show_choice():
    print(f"Ngôn ngữ bạn chọn là: {languages[v.get()]}")

root = tk.Tk()
root.title("Chọn ngôn ngữ lập trình")

languages = [("Python",1), ("Perl",2), ("Java",3), ("C++",4), ("C#",5)]
v = tk.IntVar()
v.set(0) 

# Tạo một frame để nhóm các radio button
language_frame = tk.Frame(root)
language_frame.pack()

for i, language in enumerate(languages):
    tk.Radiobutton(language_frame,
                   text=language,
                   variable=v,
                   value=i,
                   padx=20).pack(anchor=tk.W)

# Nút hiển thị lựa chọn
tk.Button(root, text="Hiển thị lựa chọn", command=show_choice).pack()

root.mainloop()
