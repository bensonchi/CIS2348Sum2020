# Name:Baichuan Chi
# PSID:1938207


def selection_sort_descend_trace(num_list):
    big = 0  # the biggest number in the unsorted portion
    start = 0  # start index of unsorted list
    index = 0  # index of the max number in the unsorted list portion
    end = len(num_list)  # ending index+1 of unsorted portion
    while start != end-1:  # when start == end-1, the list would have been sorted
        big = num_list[start]  # assign big to the biggest number
        for i in range(start, end):
            if num_list[i] > big:
                big = num_list[i]
                index = i
        if big != num_list[start]:  # if max is the first number, there is no need to change position
            temp = num_list[start]  # temp is a container to hold the number replaced by the max
            num_list[start] = big
            num_list[index] = temp
        start += 1  # update the starting index
        for num in num_list:
            print(num, end=' ')
        print()
    return num_list


if __name__ == '__main__':
    user_input = input()
    tokens = user_input.split(' ')
    unsorted_list = []
    for token in tokens:  # convert list items from str to int
        unsorted_list.append(int(token))

    selection_sort_descend_trace(unsorted_list)
