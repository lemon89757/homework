greet = " how you   doing ."
print (greet)

hello_L = greet.split(" ")
hello_LL =[s for s in hello_L if s!=""]
say_hello = " ".join(hello_LL)
print (say_hello)    #去掉字符串中连续的多余空格
