print("Nguyễn Xuân Dịu")
print("23572021610078")
import numpy as np

# Tạo dữ liệu với kiểu cấu trúc
data = np.array(
    [('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.1), ('Pit', 5, 40.11)],
    dtype=[('name', 'U10'), ('class', 'i4'), ('height', 'f4')]
)

# Sắp xếp theo lớp trước, sau đó đến chiều cao
sorted_data = np.sort(data, order=['class', 'height'])

print("Kết quả sắp xếp:")
print(sorted_data)
