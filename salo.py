clay = int(input())

for i in range(clay):
    for j in range(clay - i - 1):
        print(" ", end=" ")
    for k in range(i * 2 + 1):
        print("*", end=" ")
    print()

