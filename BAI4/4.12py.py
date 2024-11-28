print("Nguyễn Xuân Dịu")
print("235752021610078")

s = input("nhap chuoi: ").split()


element_to_remove = input("xoa phan tu: ")

if element_to_remove in s:
   s.remove(element_to_remove)
else:
    print("phan tu ko co.")

print("sau khi xoa:", s)
