import csv

def format(isTrain=True):
    rows = []
    pos = []
    neg = []
    train = []

    filename = "../data_train.csv"
    if not isTrain:
        filename = "../data_test.csv"
    with open(filename, encoding='gbk') as f:
        f_csv = csv.reader(f, delimiter='\t')

        for row in f_csv:
            data = row[0]
            if len(row) > 0:
                data = "".join(row)
            
            item = data.split("\t")
            id = item[0]
            lastpost = len(item)
            if isTrain:
                lastpost = lastpost - 1

            content = "".join(item[2:lastpost])
            answer = ""
            if isTrain:
                answer = item[lastpost]
                train.append([id, content, answer])
            else:
                train.append([id, content])

            if False:
                print(data)
                print(content)
                if int(id) % 10 == 0:
                    value = input()

            if isTrain:
                if int(answer) == 0:
                    neg.append(content)
                elif int(answer) == 2:
                    pos.append(content)

        if isTrain:
            f_pos = open('run/pos.txt', 'w+')
            f_pos.write('\n'.join(pos[0:1000]))
            f_pos.close()

            f_neg = open('run/neg.txt', 'w+')
            f_neg.write('\n'.join(neg[0:1000]))
            f_neg.close()

            with open('run/train.csv', 'w+', encoding='gbk') as f_train:        
                writer = csv.writer(f_train)
                writer.writerows(train)
        else:
            with open('run/test.csv', 'w+', encoding='gbk') as f_test:        
                writer = csv.writer(f_test)
                writer.writerows(train)

format()
format(isTrain=False)