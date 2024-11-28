print("Nguyễn Xuân Dịu")
print("235752021610078")
# File: sort_module.py

def bubbleSort(nlist):
    """Sắp xếp danh sách bằng thuật toán sắp xếp nổi bọt."""
    loop = len(nlist) 
    for i in range(loop):
        swapped = False  
        for j in range(loop - 1):  
            if nlist[j] > nlist[j + 1]: 
                # Tráo đổi chúng
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True  
        
        if not swapped:
            break
    return nlist  
