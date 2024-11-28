print("Nguyễn Xuân Dịu")
print("235752021610078")

def count_upper_lower(s):
    upper_case = 0
    lower_case = 0
    
    for char in s:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
    
    print(f"Chữ hoa: {upper_case}")
    print(f"Chữ thường: {lower_case}")

s = "Dai Hoc Vinh"
count_upper_lower(s)
