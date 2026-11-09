# def second_largest(*num):
#     num_list = list(num)

#     biggest_num = max(num)

#     num_list.remove(biggest_num)

#     return max(num_list)

# print(second_largest(22, 45, 65, 89, 188))    

# def second_largest(*num):
#     sorted_nums = sorted(num)

#     return sorted_nums[-2]
    
# print(second_largest(20, 50, 60, 8))


def second_largest(*num):
    largest = float('-inf')
    second = float('-inf')
    for n in num:
        if n > largest:
            second = largest
            largest = n
        else:
            if n > second:
                second = n
    return second

print(second_largest(20, 50, 60, 8))
