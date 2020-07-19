import csv
import zipfile

class Reader:       #最近一次作业添加
    def __init__(self,file_location):
        self.file_location = file_location

class Cvsreader(Reader):
    #def __init__(self, file_location):  #该处是上上次作业中滴，下同
        #self.file_location = file_location

    def read(self):
        with open(self.file_location, 'r', newline='') as cvs_file:
            reader = cvs.reader(cvs_file)
            return [row for row in reader]

class Txtreader(Reader):
    #def __init__(self, file_location):
        #self.file_location = file_location
    
    def read(self):
        with open(self.file_location) as txt_file:
            return [line for line in txt_file]

class Zipreader(Reader):
    #def __init__(self, file_location):
        #self.file_location = file_location
    
    def read(self, cvs_file_name):   #为实现统一将read_zip_cvs改成了read
        '''读取zip文件夹中的某个cvs文件'''
        with zipfile.ZipFile(self.file_lacation, 'r') as zip_file:
            cvs_file = zip_file.open(cvs_file_name)
            data = pd.read_cvs(data, header=None)
            return data

    def get_zip_list(self):
        '''获取zip文件夹的目录'''
        zip_file = zipfile.ZipFile(self.file_lacation)
        zip_file_list = zip_file.namelist()
        return zip_file_list
        
file_example_one = Zipreader(file_location)
print (file_example_one.read)
file_example_two = Txtreader(file_location)
print (file_example_two.read)
file_example_three = Cvsreader(file_location)
print (file_example_three.read)
