print("Nguyễn Xuân Dịu")
print("235752021610078")
import sorting_and_finding

def main():
    numbers = []
    n = int(input("Nhập số lượng phần tử: "))
    for i in range(n):
        num = int(input("Nhập phần tử thứ {}: ".format(i+1)))
        numbers.append(num)

    sorted_numbers = sorting_and_finding.selection_sort(numbers)
    max_index, min_index = sorting_and_finding.find_max_min_index(sorted_numbers)

    max_num = sorted_numbers[max_index]
    min_num = sorted_numbers[min_index]

    print("Danh sách đã sắp xếp:", sorted_numbers)
    print("Phần tử lớn nhất:", max_num, "tại vị trí:", max_index)
    print("Phần tử nhỏ nhất:", min_num, "tại vị trí:", min_index)

if __name__ == "__main__":
    main()
