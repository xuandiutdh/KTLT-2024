print("Nguyễn Xuân Dịu")
print("235752021610078")
import numpy as np

dtype = [('name', 'U20'), ('class', 'i4'), ('height', 'f4')]
students = np.array([
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
], dtype=dtype)

print("Mảng gốc:")
print(students)

sorted_students = np.sort(students, order='height')

print("\nMảng đã sắp xếp theo chiều cao:")
print(sorted_students)
