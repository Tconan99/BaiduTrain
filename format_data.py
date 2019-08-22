import csv
from snownlp import sentiment
import datetime
import time
import codecs

step = 500

def format():
    pos = []
    neg = []

    filename = "data/data_train.csv"
    with open(filename, encoding='gbk') as f:
        f_csv = csv.reader(f, delimiter='\t')

        for row in f_csv:
            id = row[0]

            content = row[2]
            answer = row[3]

            if False:
                print(row)
                print(content)
                if int(id) % 10 == 0:
                    input()

            if int(answer) == 0:
                neg.append(content)
            elif int(answer) == 2:
                pos.append(content)

      
        with open('target/pos.txt', 'w+') as f_pos:
            f_pos.write('\n'.join(pos))

        with open('target/neg.txt', 'w+') as f_neg:
            f_neg.write('\n'.join(neg))

def train():
    time_str = (datetime.datetime.now().strftime('%Y%m%d %H%M%S'))   #日期格式化
    sentiment.train('target/neg.txt', 'target/pos.txt')
    sentiment.save('target/sen %s.marshal' % time_str)

format()
train()