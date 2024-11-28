print("Nguyễn Xuân Dịu")
print("235752021610078")
import math

def Tinh(R):
    # Kiểm tra giá trị bán kính có hợp lệ không (bán kính phải là số dương)
    if R <= 0:
        return "Bán kính không hợp lệ! Vui lòng nhập số dương."
    
    # Tính chu vi và diện tích
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R * R
    
    # Trả về chu vi và diện tích
    return f"Chu vi hình tròn: {chu_vi:.2f}\nDiện tích hình tròn: {dien_tich:.2f}"

# Nhập bán kính từ người dùng
try:
    R = float(input("Nhập bán kính hình tròn: "))
    # Gọi hàm và in kết quả
    print(Tinh(R))
except ValueError:
    print("Vui lòng nhập một số hợp lệ!")
