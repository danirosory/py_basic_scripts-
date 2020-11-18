from collections import Counter

def maximum_key_value():
    data = open('C:\\Users\playboi carti\Downloads\dataset_3363_3.txt').read().split()
    Dict = Counter(data)
    max_value = max(Dict, key=Dict.get)
    max_key = Dict.get(max(Dict, key=Dict.get))


    answer = open('C:\\Users\playboi carti\Downloads\data.txt', 'w')
    answer.write(str(max_value))
    answer.write(str(' '))

    answer.write(str(max_key))

    answer.close()

maximum_key_value()
