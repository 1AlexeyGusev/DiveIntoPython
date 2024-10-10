num = int(input("Введите число:"))
for line in range(num):
    for left_num in range(num,num-line-1, -1):
        print(left_num, end="")
    point_count = 2*(num-line-1)
    print("."*point_count, end="")
    for right_num in range(num-line, num+1):
        print(right_num, end="")
    print()
    