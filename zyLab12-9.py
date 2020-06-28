# Name:Baichuan Chi
# PSID:1938207

if __name__ == '__main__':
    my_list = []
    line = input()
    while line != '-1':
        my_list.append(line)
        line = input()
    single_list = []
    for entries in my_list:
        item = entries.split(' ')
        name = item[0]
        try:
            age = int(item[1])+1
        except ValueError:
            age = 0
        print(name, age)
