def slope(right, down):
    f = open("input3.txt", "r")

    data = f.read()
    list = data.split()

#   i is the horizontal movement of the slope
    i = 0

    tree_counter = 0
    for item in range(0, len(list), down):
        if list[item][i] == "#":
            tree_counter += 1
        i += right
        if i >= len(list[item]):
            i = i - len(list[item])
    return tree_counter

print(slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2))