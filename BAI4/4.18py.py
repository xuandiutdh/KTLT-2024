print("Nguyễn Xuân Dịu")
print("235752021610078")
def fibonacci_less_than_n(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

n = int(input("nhap so nguyen n: "))

fibonacci_numbers = fibonacci_less_than_n(n)

print(f"cac so Fibonacci nho hon {n} là: {fibonacci_numbers}")
