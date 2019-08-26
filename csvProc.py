import pandas as pd

class csvProcessor():
    csv_path = ''
    csv = ''
    
    def __init__(self,csv_path):
        print('csvProcessor inited:')
        self.csv_path = csv_path
        f = open(csv_path)
        csv = pd.read_csv(f,header=None)
        f.close()

        temp = csv[0].apply(self.fixstr)
        csv[0] = [i[0] for i in temp]
        csv[1] = [i[1] for i in temp]
        print(csv.tail())
        self.csv =csv

        print('csvProcessor finished:')

    def fixstr(self,s):
        l = s[5:].split(' : ((')
        l[0]=l[0].split(' ')[-1]
        l[1]= l[1].split(') (')
        l[1][-1] = l[1][-1].split(') ')[0]
        l[1] = [(float(i.split(' ')[0]), float(i.split(' ')[1])) for i in l[1]]
        return l

if __name__=='__main__':
    csvprocessor = csvProcessor('C:/Users/LuoZN/Desktop/客流数据/wanda-traffic/lisp/B1F.csv')
