print("Nguyễn Xuân Dịu")
print("23572021610078")
import numpy as np

# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.])

# Sắp xếp theo chiều cao tăng dần, nếu chiều cao giống nhau thì sắp xếp theo ID sinh viên
indices = np.lexsort((student_id, student_height))

# In ra chỉ số và dữ liệu đã sắp xếp
print("Chỉ số sắp xếp:")
print(indices)
print("\nDữ liệu sắp xếp:")
print("ID sinh viên: ", student_id[indices])
print("Chiều cao: ", student_height[indices])
