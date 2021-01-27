file = open("input5.txt", "r")

data = file.read()
data = data.split('\n')
seat_id = 0
seat_id_list = []

for item in data:
    line_from = 0
    line_to = 127
    seat_l = 0
    seat_r = 7
    for digit in item[:-4]:
        if digit == 'F':
            line_to = line_to - round((line_to - line_from)/2)
        else:
            line_from = line_from + round((line_to - line_from)/2)
    if item[-4] == 'F': line = line_from
    else: line = line_to
    for digit in item[-3:-1]:
        if digit == 'L':
            seat_r = seat_r - round((seat_r-seat_l)/2)
        else:
            seat_l = seat_l + round((seat_r-seat_l)/2)
    if item[-1] == 'L': seat = seat_l
    else: seat = seat_r
    seat_id_list.append((line * 8 + seat))

list_sorted = sorted(seat_id_list)

print(f' The highest seat ID is: {list_sorted[-1]}')

for i in range(0, (len(list_sorted)-1)):
    if (list_sorted[i]+2) == list_sorted[i+1]: my_seat = list_sorted[i]+1

print(f'My seat is: {my_seat}')
