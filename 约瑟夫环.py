def joeseph_circle(a,b):
    assert isinstance(a,int)
    assert isinstance(b,int)
    assert a != 0
    order = list(range(a))
    while len(order) != 1:
        x = b%a  
        if x == 0:
            order.pop(b-1)
            list_1 = order[b:]
            list_2 = order[:b]
            order = list_1 + list_2
            a = a-1
        else:
            order.pop(x-1)
            list_3 = order[x:]
            list_4 = order[:x]
            order = list_3 + list_4
            a = a-1
    assert len(order) == 1
    return order
# print(joeseph_circle(20,3))
num_people = int(input("how many people:"))
num_kill = int(input("the munber is:"))
last_num = joeseph_circle(num_people,num_kill)
print("the last one is:",last_num)
