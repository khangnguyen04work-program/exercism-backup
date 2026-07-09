def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    general_list = [number]
    for each_number in general_list:
        if each_number == 1:
            break
        cal_1 = 0
        cal_1 = each_number % 2
        if cal_1 == 0:
            cal_2 = each_number // 2
            if cal_2 == 1:
                general_list.append(cal_2)
                break
            general_list.append(cal_2)
        else:
            cal_3 = each_number * 3 + 1
            general_list.append(cal_3)
    return len(general_list) - 1


