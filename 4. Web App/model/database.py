import cx_Oracle as ora
# ----------------------------------------------------------------------------------
# 오라클 연결 및 접속하기
def getConnection() :
    dsn = ora.makedsn('localhost', 1521, service_name='orcl')
    conn = ora.connect(user='wcprj', password='qwerty123', dsn=dsn)
    return conn

# 커서 받기
def getCursor(conn):
    cursor = conn.cursor()
    return cursor

# 접속 정보 및 커서 반납하기
def dbClose(cursor, conn):
    cursor.close()
    conn.close()
# ----------------------------------------------------------------------------------
# 회원정보 불러오기
def getLogin(id, pwd):
    conn = getConnection()
    cursor = getCursor(conn)

    sql = f'''SELECT * 
        FROM member
        WHERE id = '{id}'
        AND pwd = '{pwd}'
        '''

    cursor.execute(sql)
    row = cursor.fetchall()
    dbClose(cursor, conn)

    try:
        return row[0]
    except:
        return False