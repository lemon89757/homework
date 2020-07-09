import random
scores = [random.randint(0,100) for i in range(40)]   
print (scores)                  #随机产生40个0至100整数代表40个人成绩

num_students = len(scores)
sum_score = sum(scores)*1.0
average_score = sum_score/num_students
num_under_average = len([i for i in scores if i<average_score])
print('the average score is:%.1f' % average_score)
print("there are %d students' score is under the average" % num_under_average)    #计算平均成绩和在平均成绩以下人数

descend_score =sorted(scores,reverse=True)    
print (descend_score)        #对成绩由大到小降序排列，sort没有返回值
