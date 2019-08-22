import csv
from snownlp import SnowNLP
from snownlp import sentiment
import numpy as np
import os

sentiment.classifier.load('target/sen 20190822 165752.marshal')

def run(isTrain=True):
    rows = []
    list = []

    filename = 'data/data_train.csv'
    if not isTrain:
        filename = 'data/data_test.csv'
    with open(filename, encoding='gbk') as f:
        f_cvs = csv.reader(f, delimiter='\t')
        for row in f_cvs:
            rows.append(row)

    filename_answer = 'target/answer.csv'
    if os.path.exists(filename_answer): 
        os.remove(filename_answer)
    
        
    wrong = 0
    total = len(rows)
    progress = 0
    for row in rows[0:]:

        progress += 1

        id = row[0]
        content = row[2]
        answer = ''
        if isTrain:
            answer = row[3]

        avg = 1
        if content and content != '':
            s = SnowNLP(content)
            # avg = np.mean(s.sentences)
            avg = s.sentiments

        if progress % 50 == 0:
            print("progress=" + str(progress) + "," + str(100.0 * progress / total) + "%, wrong: " + str(wrong) + " -> " + str(100.0 * wrong / (progress)) + "%")

        if False :
            print(row)
            # print(content)
            print(avg)

            if progress % 1 == 0:
                input()

        result = 1
        if avg < 0.2:
            result = 0
        elif avg > 0.8:
            result = 2
        
        if isTrain and result != int(answer):
            wrong += 1

        if not isTrain:
            list.append([id, result])

    if len(list) > 0:
        with open(filename_answer, 'w+', encoding='gbk') as csv_answer:
            writer = csv.writer(csv_answer)
            writer.writerows(list)
        list.clear()            
# run(isTrain=True)
run(isTrain=False)