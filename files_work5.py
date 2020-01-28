import csv

with open('people.csv') as people:
    for person in csv.reader(people):
        print('Nome: {} Sobrenome: {}'.format(*person))