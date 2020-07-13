class Person(object):
    def __init__(self,name,gender,age,serial_num):
        self.name = name
        self.gender = gender
        self.age = age
        self.serial_num = serial_num
    def print_information(self):
        print("number %d information is: %s,%s,%d ."%(self.serial_num,self.name,self.gender,self.age))     
person_one = Person('name0','male',20,0)
person_two = Person('name1','female',21,1)
person_three = Person('name2','male',22,2)
person_four = Person('name3','female',23,3)
person_five = Person('name4','male',24,4)
person_six = Person('name5','female',25,5)
person_seven = Person('name6','male',26,6)
person_eight = Person('name7','female',27,7)
person_nine = Person('name8','male',28,8)
person_ten = Person('name9','female',29,9)


def joeseph_circle(a,b):
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

num_people = 10
num_kill = int(input("the munber is:"))
last_num_list = joeseph_circle(num_people,num_kill)
last_num = last_num_list[0]
print("the last one is:",last_num)
if last_num == 0:
    person_one.print_information()
elif last_num == 1:
    person_two.print_information()
elif last_num == 2:
    person_three.print_information()
elif last_num == 3:
    person_four.print_information()
elif last_num == 4:
    person_five.print_information()
elif last_num == 5:
    person_six.print_information()
elif last_num == 6:
    person_seven.print_information()
elif last_num == 7:
    person_eight.print_information()
elif last_num == 8:
    person_nine.print_information()
elif last_num == 9:
    person_ten.print_information()
else:
    print("Error")

