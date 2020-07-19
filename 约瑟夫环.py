def joeseph_circle(total_person,step):
    assert isinstance(total_person,int)
    assert isinstance(step,int)
    if total_person == 0:
        print("总人数为零")
    elif step<0:
        print("请输入一个正整数")
    else:
        order = list(range(total_person))
        while len(order) != 1:
            x = step % total_person  
            if x == 0:
                step = step-1
                order.pop(step)
                list_former = order[step:]
                list_latter = order[:step]
                order = list_former + list_latter
                total_person = total_person-1
            else:
                x = x-1
                order.pop(x)
                list_former = order[x:]
                list_latter = order[:x]
                order = list_former + list_latter
                total_person = total_person-1    #考虑到step可能大于total_peson的情况，不能直接将x!=0时的step的值直接赋给x
        assert len(order) == 1
        return order
# print(joeseph_circle(20,3))
num_people = int(input("请输入总人数:"))
num_kill = int(input("请输入一个正整数:"))
last_num = joeseph_circle(num_people,num_kill)
print("the last one is:",last_num)
