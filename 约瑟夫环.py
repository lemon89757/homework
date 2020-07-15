def joeseph_circle(num_person,num_killed):
    a = num_person
    b = num_killed
    assert isinstance(a,int)
    assert isinstance(b,int)
    assert a != 0
    order = list(range(a))
    while len(order) != 1:
        x = b%a  
        if x == 0:
            order.pop(b-1)
            list_former = order[b:]
            list_latter = order[:b]
            order = list_former + list_latter
            a = a-1
        else:
            order.pop(x-1)
            list_former = order[x:]
            list_latter = order[:x]
            order = list_former + list_latter
            a = a-1
    assert len(order) == 1
    return order
# print(joeseph_circle(20,3))
num_people = int(input("how many people:"))
num_kill = int(input("the munber is:"))
last_num = joeseph_circle(num_people,num_kill)
print("the last one is:",last_num)
