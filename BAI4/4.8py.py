print("Nguyễn Xuân Dịu")
print("235752021610078")
s = input("Nhập dãy các từ: ").split()


max_length = max(len(word) for word in s)


longest_words = [word for word in s if len(word) == max_length]

print("Từ dài nhất:", longest_words)
