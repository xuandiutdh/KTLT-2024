print("Nguyễn Xuân Dịu")
print("235752021610078")
def count_letters_digits(s):
    letters = 0
    digits = 0
    
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    
    print(f"Số chữ cái là: {letters}")
    print(f"Số chữ số là: {digits}")


s = "hello world! 123"
count_letters_digits(s)
