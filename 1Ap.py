num_list = [2,67,16,24,29,64]
print("The numbers whose square is divisible by 8 are ")
for num in num_list:
    if (num * num) % 8 == 0:
        print(num)
