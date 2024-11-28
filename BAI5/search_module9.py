print("Nguyễn Xuân Dịu")
print("235752021610078")
# File: search_module.py

def binary_search(sorted_list, value):
    """Tìm kiếm nhị phân trong danh sách đã được sắp xếp."""
    lower_bound = 0
    upper_bound = len(sorted_list) - 1

    while lower_bound <= upper_bound:
        mid_point = (lower_bound + upper_bound) // 2  # Tính chỉ số giữa
        
        if sorted_list[mid_point] < value:
            lower_bound = mid_point + 1  # Tìm trong nửa bên phải
        elif sorted_list[mid_point] > value:
            upper_bound = mid_point - 1  # Tìm trong nửa bên trái
        else:
            return True  # Giá trị được tìm thấy

    return False  # Giá trị không tồn tại
