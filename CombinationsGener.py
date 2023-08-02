import random
stop = 0
start = 1
numbers = list(input('enter numbers you want to know the number of their possible combinations'))
poss_comb = [map(list, numbers)]
all_comb = (map(str, numbers))
all_comb = ''.join(all_comb)

while start == 1:
    random.shuffle(numbers)
    comb = (map(str, numbers))
    comb = ''.join(comb)
    if comb not in all_comb:
        stop = 0
        poss_comb.append((map(str, numbers)))
        all_comb = all_comb + ', ' + comb

    elif stop < 50000:
        stop += 1

    else:
        start = 0

print('Number of possible combinations: ', len(poss_comb))
if len(all_comb) < 501:
    print('The combinations: ', all_comb)
