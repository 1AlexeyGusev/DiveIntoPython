n = int(input("Введите количество числел: "))
count = 0
for i in range(n):
    num = int(input("Введите число: "))
    for div in range(2, num):
        if num % div == 0:
            break
    else:
        count += 1
print("Количество простых числел = ", count)