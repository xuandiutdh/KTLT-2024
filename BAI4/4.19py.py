print("Nguyễn Xuân Dịu")
print("235752021610078")
def sieve_of_eratosthenes(limit):
   
    is_prime = [True] * limit
    is_prime[0], is_prime[1] = False, False  
    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            
            for multiple in range(number * number, limit, number):
                is_prime[multiple] = False
    
    prime_numbers = tuple(num for num, prime in enumerate(is_prime) if prime)
    return prime_numbers

limit = 1000000

prime_tuple = sieve_of_eratosthenes(limit)

print(f"co tong cong {len(prime_tuple)}so nguyen to nho hon 1trieu.")
print(f"cac so nguyen to dau tien la: {prime_tuple[:10]}") 
