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
            f_pos.write('\n'.join(pos[:]))
        
        with open('target/neg.txt', 'w+') as f_neg:
            f_neg.write('\n'.join(neg[:]))

printTime = lambda t: "%02d:%02d:%02d" % (int(t/60/60)%60, int(t/60)%60, int(t)%60)
start = 0
def printPer(index, total, type):

    if index % 100 != 0:
        return

    pass_time = time.time() - start
    per = index * 100.0 / total

    total_time = 999999
    if index > 0:
        total_time = int(pass_time / index * total)
    
    print("%d: %.2f%% -> %s/%s" % (type, per, printTime(pass_time), printTime(total_time)))

def train():
    time_str = (datetime.datetime.now().strftime('%Y%m%d %H%M%S'))   #日期格式化
    print("prepare...")
    global start
    start = time.time()
    sentiment.train('target/neg.txt', 'target/pos.txt', printPer)
    sentiment.save('target/sen %s.marshal' % time_str)

format()
train()