from snownlp import sentiment
import datetime

time_str = (datetime.datetime.now().strftime('%Y%m%d %H%M%S'))   #日期格式化

# todo 文件分片 展示进度
sentiment.train('run/neg.txt', 'run/pos.txt')
sentiment.save('run/sen %s.marshal' % time_str)