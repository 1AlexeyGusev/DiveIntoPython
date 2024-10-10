width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))
for i in range(height+1):
    for j in range(width+1):
        if j == 0 or j == width:
            print("|", end="")
        elif i == 0 or i == height:
            print("-", end="")
        else:
            print(" ", end="")
    print()
        