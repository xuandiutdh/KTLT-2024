print("Nguyễn Xuân Dịu")
print("235752021610078")
def check_binary_divisible_by_5(binary_string):
    
    binaries = binary_string.split(',')
    
    divisible_by_5 = []
    
    for binary in binaries:
      
        if len(binary) == 4 and all(bit in '01' for bit in binary):
           
            decimal = int(binary, 2)
            
            if decimal % 5 == 0:
                divisible_by_5.append(binary)

    if divisible_by_5:
        print("so nhi phan chia het cho 5:", ', '.join(divisible_by_5))
    else:
        print("ko co so nhi phan nao chia het cho5.")

input_string = input("nhap chuoi so nhi phan: ")
check_binary_divisible_by_5(input_string)
