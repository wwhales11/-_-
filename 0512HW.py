# 다이아몬드 만들기

line = int(input("size of Diamond: "))

for row1 in range(1, line * 2, 2):
    print((" " * ((line * 2 - 1 - row1) // 2)) + ("*" * row1))

for row2 in range(line * 2 - 3, 0, -2):
    print((" " * ((line * 2 - 1 - row2) // 2)) + "*" * row2)
