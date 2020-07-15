class Josephu(object):
    def __init__(self, people):
        self.people = []

    def append(self, person):
        self.people.append(person)

    def pop(self, step, start_num, killed_num):
        self.step = len(people)
        self.start_num = int(input("the start number is:"))
        self.killed_num = int(input("the killed number is:"))
        assert isinstance(start_num,int)
        assert isinstance(killed_num,int)
        assert step>=start_num
        x = killed_num%step
        if x == 0:
            y = killed_num+start_num
            start_num = 0
            if y>step:
                y = y-step
            else:
                y = y
            list_former = people[y:]
            list_latter = people[:y]
            people = list_former+list_latter
        else:
            z = x + start_num
            start_num = 0
            if z>step:
                z = z-step
            else:
                z = z
            list_former = people[z:]
            list_latter = people[:z]
            people = list_former+list_latter
        return people,start_num

    def traverse(self):    #只考虑了killed_num小于等于step的情况；第一次时，traverse的调用应在pop前。
        list_traverse = []
        if start_num != 0:
            m = start_num+killed_num
            if m>step:
                n = m-step-1
                lsit_former = people[start_num:]
                for i in list_former:
                    list_traverse_former = append(i)
                list_latter = people[:n]
                for i in list_latter:
                    list_traverse_latter = append(i)
                list_traverse = list_traverse_former+list_traverse_latter
            else:
                list_whole = people[start_num:m]
                for i in list_whole:
                    list_traverse = append(i)
        else:
            list_whole = people[:killed_num]
            for i in list_whole:
                list_traverse = append(i)
        return list_traverse       