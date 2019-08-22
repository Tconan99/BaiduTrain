import csv
from snownlp import SnowNLP
from snownlp import sentiment
import numpy as np

sentiment.classifier.load('run/sen 20190822 133553.marshal')

def run(isTrain=True):
    list = []
    filename = '../data_train.csv'
    if not isTrain:
        filename = 'run/test.csv'
    with open(filename, encoding='gbk') as f:
        f_cvs = csv.reader(f, delimiter='\t')
        rows = []
        for row in f_cvs:
            rows.append(row)

        wrong = 0
        total = len(rows)
        index = 0
        progress = 0
        for row in rows:
            id = row[0]
            content = row[2]
            answer = ''
            if isTrain:
                answer = row[3]
            s = SnowNLP(content)
            # avg = np.mean(s.sentences)
            avg = s.sentiments

            if progress % 50 == 0:
                print("progress=" + str(progress) + "," + str(100.0 * progress / total) + "%, wrong: " + str(wrong) + " -> " + str(100.0 * wrong / (progress + 1)) + "%")
            progress += 1

            if False :
                print(row)
                # print(content)
                print(avg)

                if index > 0:
                    index = 0
                    key = input()
                index = index + 1

            result = 1
            if avg < 0.33:
                result = 0
            elif avg > 0.667:
                result = 2
            
            if isTrain and result != int(answer):
                wrong += 1

            if not isTrain:
                list.append([id, result])
        
        with open('run/answer.csv', encoding='gbk') as csv_answer:
            writer = csv.writer(csv_answer)
            writer.writerows(list)

run(isTrain=True)
