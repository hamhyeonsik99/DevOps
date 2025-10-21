import pymysql
# mysql 서버에 연결
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="hamhyeonsik99!",
    database="example11"
)
# 커서 생성 -> 프롬프트 오른쪽에 깜빡깜빡하게 하는거
cursor = conn.cursor()
# 명령어 실행
sql = "SELECT * FROM employees;"
cursor.execute(sql)
employees = cursor.fetchall()
for employee in employees:
    print(employee)

print("데이터 조회 완료")
# 연결 해제
conn.close()