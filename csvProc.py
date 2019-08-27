import pandas as pd

class csvProcessor():
    csv_paths = []
    csv = []
    
    def __init__(self,csv_paths):
        print('csvProcessor inited:')
        self.csv_paths = csv_paths
        csv=[]
        for path in csv_paths:
            f = open(path)
            temp = pd.read_csv(f,header=None)
            f.close()
            csv.append(temp)
        csv = pd.concat(csv,ignore_index= True)

        temp = csv[0].apply(self.fixstr)
        csv['id'] = [i[0] for i in temp]
        csv['boundary'] = [i[1] for i in temp]
        del csv[0]
        print(list(csv['id']))

        self.csv =csv

        print('csvProcessor finished:')

    def fixstr(self,s):
        l = s[5:].split(' : ((')
        l[0]=l[0].split(' ')[-1]
        l[0]=l[0].split(';')[-1].split('}')[0]
        l[0]=[e for e in l[0].split('-') if e != '']
        l[1]= l[1].split(') (')
        l[1][-1] = l[1][-1].split(') ')[0]
        l[1] = [(float(i.split(' ')[0]), float(i.split(' ')[1])) for i in l[1]]
        return l

if __name__=='__main__':
    csvprocessor = csvProcessor(['C:/Users/LuoZN/Desktop/客流数据/wanda-traffic/lisp/B1F.csv','C:/Users/LuoZN/Desktop/客流数据/wanda-traffic/lisp/1AF.csv'])
