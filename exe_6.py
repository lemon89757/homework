#此程序用于统计考试成绩

def average_score(x):   #计算平均成绩
    scores_values = x.values()    #dict.values用于返回给定字典中可用的所有值的列表
    sum_scores = sum(scores_values)*1.0
    average = sum_scores/len(scores_values)
    return average

def descend_score(x):    #将成绩降序排列
    name_score_lst = [(x[i],i) for i in x]
    sort_lst =sorted(name_score_lst,reverse=True)
    return [(j[1], j[0]) for j in sort_lst]

examine_scores = {"google":98, "facebook":99, "baidu":52, "alibaba":80, "yahoo":49, "IBM":70, "android":76, "apple":99, "amazon":99}

AverageSocre = average_score(examine_scores)
print ("the average score is: ",AverageSocre)

score_sort = descend_score(examine_scores)
print ("list of the scores: ",score_sort)
