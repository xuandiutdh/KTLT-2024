print("Nguyễn Xuân Dịu")
print("235752021610078")
# File: search_module.py

def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return True, i
        return False, -1 
