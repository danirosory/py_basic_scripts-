import re
def unpackage():
    data = open('C:\\Users\playboi carti\Downloads\dataset_3363_2.txt').read()
    letters = re.split('\d+',data)
    numbers = re.split('\D', data)


    letters.remove('\n')
    numbers.remove('')
    numbers.remove('')

    s = ''
    for x, i in zip(letters, numbers):
        s += x * int(i)

    decoded = open('C:\\Users\playboi carti\Downloads\data.txt', 'w')
    decoded.write(s)
    decoded.close()
unpackage()