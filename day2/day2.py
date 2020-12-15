def check_password():
    f = open("input2.txt", "r")

    #read the data
    data = f.read()
    txt = data.split()

    correct = 0

    for i in range(0, len(txt), 3):
        slash = txt[i].find('-')
        print(f'slash {slash}')
        min = int(txt[i][0:slash])
        max = int(txt[i][slash+1:])
        letter = txt[i+1][0]
        password = txt[i+2]
        print(f'min {min},max {max}')
        print(f'letter:{letter}')
        print(f'pass:{password}')
        check = 0
        for j in range(len(password)):
            if password[j] == letter:
                check += 1
        print(check)
        if check >= min and check <= max:
            correct += 1
    return correct

def check_password2():
    f = open("input2.txt", "r")

    #read the data
    data = f.read()
    txt = data.split()

    correct = 0

    for i in range(0, len(txt), 3):
        slash = txt[i].find('-')
        print(f'slash {slash}')
        min = int(txt[i][0:slash])
        max = int(txt[i][slash+1:])
        letter = txt[i+1][0]
        password = txt[i+2]
        print(f'min {min},max {max}')
        print(f'letter:{letter}')
        print(f'pass:{password}')
        #check = 0
        if password[min-1] == letter or password[max-1] == letter:
            if password[min-1] != password[max-1]:
                correct += 1
    return correct


print(check_password2())





