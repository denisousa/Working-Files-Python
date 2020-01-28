with open('words.txt') as file_work:
    for line in file_work:
        print(line, line.replace(' ', ''))
