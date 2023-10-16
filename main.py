# 1
def list_fullname(ref_list):
    names = ref_list[0]
    surnames = ref_list[1]
    result = []

    for name, surname in zip(names, surnames):
        result.append([name, surname])
    return result


ref_list = [['Радмир', 'Егор', 'Марат', 'Рамазан'], ['Тимеркаев', 'Тептев', 'Гайнутдинов', 'Медетбеков']]
f_list = list_fullname(ref_list)
print(f_list)


# 2
def del_rep(num):
    sort_list = sorted(list(set(num)))
    return sort_list


num = [2, 3, 1, 2, 3, 1, 3, 2, 4]
result = del_rep(num)
print(result)


# 3
def lim_max(nums, limit):
    max_value = -1

    for num in nums:
        if num < limit and num > max_value:
            max_value = num
    return max_value


nums = (10, 20, 30, 40, 50, 60, 70, 80,100)
limit = 100
result = lim_max(nums, limit)
print(result)


# 4
def temp_cat(temp):
    if temp < -20:
        return 0
    elif -20 <= temp < 0:
        return 1
    elif 0 <= temp < 15:
        return 2
    elif 15 <= temp < 25:
        return 3
    else:
        return 4


temp = 30
result = temp_cat(temp)
print(result)

# 5

