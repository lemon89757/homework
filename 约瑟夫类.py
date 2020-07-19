class Josephu(object):
    def __init__(self, people, start_num, step):
        self.people = []
        self.start_num = start_num
        self.step = step
    def append(self, person):
        self.people.append(person)
        self.total_peson = len(people)

    def pop(self):
        assert isinstance(start_num,int)
        assert isinstance(step,int)
        assert self.total_peson >= self.start_num
        x = self.step % self.total_peson
        if x == 0:
            y = self.step+self.start_num
            self.start_num = 0
            if y>self.total_peson:
                y = y-self.total_peson-1
            else:
                y = y-1
            list_former = people[y:]
            list_latter = people[:y]
            people = list_former+list_latter
        else:
            z = x + self.start_num
            self.start_num = 0
            if z>self.total_peson:
                z = z-self.total_peson-1
            else:
                z = z-1
            list_former = people[z:]
            list_latter = people[:z]
            people = list_former+list_latter
        return people,self.start_num

    def traverse(self):    #只考虑了step小于等于total_peson的情况；第一次时，traverse的调用应在pop前。
        list_traverse = []
        if start_num != 0:
            m = start_num+step
            if m>total_peson:
                n = m-total_peson-1
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
            list_whole = people[:step]
            for i in list_whole:
                list_traverse = append(i)
        return list_traverse       