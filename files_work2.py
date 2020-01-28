file_open = open('people.csv')

for line in file_open:
    print('Nome: {} / Sobrenome:{}'.format(*line.split(',')))