import pymysql
# mysql 서버에 연결
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="hamhyeonsik99!",
    database="example11",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
# 커서 생성 -> 프롬프트 오른쪽에 깜빡깜빡하게 하는거
cursor = conn.cursor()
# 명령어 실행
cursor.execute("SELECT DATABASE()")
print("현재 데이터베이스: ", cursor.fetchone()) # 한번 호출에 하나의 row를 가져올때 사용
# print("현재 데이터베이스: ", cursor.fetchall())
# print("현재 데이터베이스: ", cursor.fetchmany(2))
# 연결 해제
conn.close()