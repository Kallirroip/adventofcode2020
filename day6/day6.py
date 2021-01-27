file = open("input6.txt", "r")

data = file.read()
data = data.replace('\n',' ')
list = data.split('  ')

question_answered = []
sum_of_counts = 0
for group in list:
    question_answered = []
    all_answers = group.replace(' ', '')
    for question in all_answers:
        if question not in question_answered: question_answered.append(question)
    sum_of_counts +=  len(question_answered)

print(f'The sum of counts for part 1 is: {sum_of_counts}')

count = 0
for group in list:
    group = group.split()
    if len(group) == 1:
        count += len(group[0])
    else:
        common = group[0]
        for i in range(1,len(group)):
            answer = ''.join(sorted(set.intersection(set(common), set(group[i]))))
            common = answer
        count += len(common)

print(f'The sum of counts for part 2 is: {count}')
