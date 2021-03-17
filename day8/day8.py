file = open("input8.txt", "r")

data = file.read()
data = data.split('\n')

def check_code(file):
    check = []
    accumulator = 0
    counter = 0
    operation = []
    argument = []

    for each in file:
        operation.append(each.split()[0])
        argument.append(int(each.split()[1]))

    for i in range(len(operation)):
        if counter not in check:
            check.append(counter)
            if operation[counter] == 'acc':
                accumulator += argument[counter]
                counter += 1
            elif operation[counter] == 'jmp':
                counter += argument[counter]
            else:
                counter += 1
        else:
            break
    return accumulator, counter, len(operation)

answer = check_code(data)

print(f'The accumulator is {answer[0]} and the program terminated on line {answer[1]}/{answer[2]}')

check = []
accumulator = 0
counter = 0
operation = []
argument = []
changed_arguments = []

for each in data:
    operation.append(each.split()[0])
    argument.append(int(each.split()[1]))

for i in range(len(operation)):
    operation_to_change = operation.copy()

    if operation[i] == 'jmp' and i not in changed_arguments:
        operation_to_change[i] = 'nop'
        changed_arguments.append(i)

        for j in range(len(operation_to_change)):
            if counter < len(operation_to_change):
                if counter not in check:
                    check.append(counter)
                    if operation_to_change[counter] == 'acc':
                        accumulator += argument[counter]
                        counter += 1
                    elif operation_to_change[counter] == 'jmp':
                        counter += argument[counter]
                    else:
                        counter += 1
                else:
                    accumulator = 0
                    counter = 0
                    check = []
                    break
            else :
                if counter == (len(operation_to_change)):
                    print(f'The accumulator is {accumulator} and the program terminated on line {counter}/{len(operation_to_change)}'
                          f', changed index {i} from jmp to nop')
                    quit()
                accumulator = 0
                counter = 0
                check = []
                break

    elif operation[i] == 'nop' and i not in changed_arguments:
        operation_to_change[i] = 'jmp'
        changed_arguments.append(i)

        for j in range(len(operation_to_change)):
            if counter < len(operation_to_change):
                if counter not in check:
                    check.append(counter)
                    if operation_to_change[counter] == 'acc':
                        accumulator += argument[counter]
                        counter += 1
                    elif operation_to_change[counter] == 'jmp':
                        counter += argument[counter]
                    else:
                        counter += 1
                else:
                    accumulator = 0
                    counter = 0
                    check = []
                    break
            else :
                if counter == (len(operation_to_change)):
                    print(f'The accumulator is {accumulator} and the program terminated on line {counter}/{len(operation_to_change)}'
                          f', changed index {i} from nop to jmp')
                    quit()
                accumulator = 0
                counter = 0
                check = []
                break



