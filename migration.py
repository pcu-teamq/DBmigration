import pymysql
import csv
import os
import glob

files = glob.glob("") # 바꿀 파일의 디렉토리
for name in files:
    if not os.path.isdir(name):
        src = os.path.isdir(name)
        os.rename(name, src[0]+'.csv')

conn = pymysql.connect(host='localhost', user='root', password='', db='arduino', charset='utf8')
curs = conn.cursor()
sql = "INSERT IGNORE INTO board (NAME, LOG, TIME, ID) VALUES (%s, %s, %s, %s)"
f = open('/Users/hyeokjulee/Downloads/execl_fingerprint/PLX-DAQ-v2.11/data.csv', 'r', encoding='utf-8')
rd = csv.reader(f)

for line in rd:
    curs.execute(sql, (line[0], line[1], line[2], line[3]))

conn.commit()
conn.close()
f.close()
