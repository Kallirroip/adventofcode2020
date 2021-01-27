f = open("input4.txt", "r")

data = f.read()
data = data.replace('\n',' ')
list = data.split('  ')
print(list)


def validate_passoprts_no_missing_fields():
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid = 0
    for item in list:
        check_fields = 0
        for i in range(len(item)):
            if item[i] == ':':
                if item[(i-3):i] in required_fields:
                    check_fields += 1
        if check_fields == 7:
            valid += 1
    return valid
valid_passports = validate_passoprts_no_missing_fields()
print(f' Number of valid passports: {valid_passports}')


def validate_all_fields():
    valid = 0
    for item in list:
        passport = item.split(' ')
        check = 0
        for i in passport:
            field = i.split(':')[0]
            value = i.split(':')[1]
            if field == 'byr':
                if int(value) >= 1920 and int(value) <= 2002:
                    check += 1
                else: break
            elif field == 'iyr':
                if int(value) >= 2010 and int(value) <= 2020:
                    check += 1
                else: break
            elif field == 'eyr':
                if int(value) >= 2020 and int(value) <= 2030:
                    check += 1
                else: break
            elif field == 'hgt':
                if value.endswith('cm'):
                    if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
                        check += 1
                elif value.endswith('in'):
                    if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
                        check += 1
                else: break
            elif field == 'hcl':
                hair_colour = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
                if value[0] == '#':
                    colour_check = 0
                    for letter in value:
                        if letter in hair_colour:
                            colour_check += 1
                    if colour_check == 6:
                        check += 1
                else: break
            elif field == 'ecl':
                eye_colour = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
                if value in eye_colour:
                    check += 1
                else: break
            elif field == 'pid':
                print(i)
                if len(value) == 9:
                    value = int(value)
                    if type(value) is int:
                        check += 1
        if check == 7:
            valid += 1
    return valid
valid = validate_all_fields()
print(f'No of passports with valid fields: {valid}')
