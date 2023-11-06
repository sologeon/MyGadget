def get_add_set_for_two_len(aim_num=9, loop_low_num=1, up_num=9):
    loop_limit = int(aim_num / 2)
    upper_number = min(loop_limit, up_num)+1
    all_add_set = []
    for i in range(loop_low_num, upper_number):
        first_num = i
        second_num = aim_num-i
        if first_num>=loop_low_num and second_num>=loop_low_num and second_num<=up_num:
            tmp_add_set = [first_num, second_num]
            tmp_add_set.sort()
            all_add_set.append(tmp_add_set)
    return all_add_set

def recurive_get_add_set_for_any_len(aim_num=19, add_set_len=3, loop_low_num=1, up_num=9):
    add_set_list = []
    tail_len = add_set_len - 1
    for j in range(loop_low_num, up_num+1):
        front_num = j
        tail_num_sum = aim_num - front_num
        if tail_num_sum<=tail_len*up_num:
            if tail_len>2:
                layer_add_set = recurive_get_add_set_for_any_len(aim_num=tail_num_sum, add_set_len=tail_len, loop_low_num=front_num, up_num=up_num)
                _layer_add_set = [[front_num]+ele for ele in layer_add_set]
                add_set_list += _layer_add_set
            elif tail_len==2:
                layer_add_set = get_add_set_for_two_len(aim_num=tail_num_sum, loop_low_num=front_num, up_num=up_num)
                if len(layer_add_set)>0:
                    _layer_add_set = [[front_num]+ele for ele in layer_add_set]
                    add_set_list += _layer_add_set
    return add_set_list

res = recurive_get_add_set_for_any_len(aim_num=19, add_set_len=3, loop_low_num=1, up_num=9)
res
len(res)
res = recurive_get_add_set_for_any_len(aim_num=19, add_set_len=4, loop_low_num=1, up_num=9)
res
len(res)




