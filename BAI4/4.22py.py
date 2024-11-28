print("Nguyễn Xuân Dịu")
print("235752021610078")
def is_all_digits_even(number):
    
    return all(int(digit) % 2 == 0 for digit in str(number))

def find_even_digit_numbers(start, end):
    even_digit_numbers = []
    for number in range(start, end + 1):
        if is_all_digits_even(number):
            even_digit_numbers.append(str(number))
    
    print(', '.join(even_digit_numbers))

find_even_digit_numbers(1000, 3000)
