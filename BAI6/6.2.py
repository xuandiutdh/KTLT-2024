print("Nguyễn Xuân Dịu")
print("235752021610078")
# Định nghĩa class Hinhchunhat
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

# Tạo đối tượng hình chữ nhật với chiều dài 5 và chiều rộng 3
hcn = Hinhchunhat(5, 3)

# Gọi method dien_tich để tính diện tích
dien_tich_hcn = hcn.dien_tich()
print("Diện tích hình chữ nhật là:", dien_tich_hcn)

