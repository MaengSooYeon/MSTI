import pymysql

conn = pymysql.connect(host = 'localhost', user = 'root', password = 'mirim2' , db = 'test', charset='utf8')
# host = DB주소(localhost 또는 ip주소), user = DB id, password = DB password, db = DB명
curs = conn.cursor()

sql = "SELECT * FROM test_table" # 실행 할 쿼리문 입력
curs.execute(sql) # 쿼리문 실행

rows = curs.fetchall() # 데이터 패치

for i in rows :
     print(i)

conn.close()