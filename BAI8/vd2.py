
import re

# Danh sách chứa mật khẩu hợp lệ
valid_passwords = []

# Nhập mật khẩu từ người dùng và chia nhỏ thành các phần tử trong danh sách
passwords = [x.strip() for x in input("Nhập mật khẩu: ").split(',')]

# Duyệt qua từng mật khẩu trong danh sách
for password in passwords:
    # Kiểm tra độ dài mật khẩu
    if len(password) < 6 or len(password) > 12:
        continue
    # Kiểm tra ít nhất một ký tự thường
    if not re.search("[a-z]", password):
        continue
    # Kiểm tra ít nhất một chữ số
    if not re.search("[0-9]", password):
        continue
    # Kiểm tra ít nhất một ký tự hoa
    if not re.search("[A-Z]", password):
        continue
    # Kiểm tra ít nhất một ký tự đặc biệt trong [$#@]
    if not re.search("[$#@]", password):
        continue
    # Kiểm tra xem mật khẩu có chứa khoảng trắng không
    if re.search("\s", password):
        continue
    # Thêm mật khẩu vào danh sách nếu thỏa mãn tất cả tiêu chí
    valid_passwords.append(password)

# In ra các mật khẩu hợp lệ
print("Các mật khẩu hợp lệ:", ",".join(valid_passwords))

