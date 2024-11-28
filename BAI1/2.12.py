print ("Nguyễn Xuân Dịu")
print ("235752021610078")

import re

def kiem_tra_mat_khau(mat_khau):
    if len(mat_khau) < 6 or len(mat_khau) > 12:
        return "Mật khẩu phải có từ 6 đến 12 kí tự. \nHãy nhập lại mật khẩu"
    
    if not re.search(r'[A-Z]', mat_khau):
        return "Mật khẩu phải có ít nhất một chữ cái viết hoa. \nHãy nhập lại mật khẩu"
    
    if not re.search(r'[a-z]', mat_khau):
        return "Mật khẩu phải có ít nhất một chữ cái viết thường. \nHãy nhập lại mật khẩu"
    
    if not re.search(r'\d', mat_khau):
        return "Mật khẩu phải có ít nhất một chữ số. \nHãy nhập lại mật khẩu"
    
    if not re.search(r'[@#$%^&+=]', mat_khau):
        return "Mật khẩu phải có ít nhất một ký tự đặc biệt (@, #, $, %, ^, &, +, =). \nHãy nhập lại mật khẩu"
    
    return "Mật khẩu hợp lệ."

while True:
   mat_khau = input("Nhập mật khẩu của bạn: ")
   ket_qua = kiem_tra_mat_khau(mat_khau)
   print(ket_qua)
   if ket_qua == "Mật khẩu hợp lệ.":
       break
