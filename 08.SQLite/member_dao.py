#
# member table에 대한 Data Access Object(DAO)
#
import sqlite3 as sq
# member table에 있는 데이터 모두 읽기
def get_members():
    conn = sq.connect('test.db')
    cur = conn.cursor()

    sql = 'select * from member;'
    cur.execute(sql)
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows

# 성별로 가져오기
def get_members_by_gender(gender):
    conn = sq.connect('test.db')
    cur = conn.cursor()

    sql = 'select * from member where gender=?;'
    cur.execute(sql, (gender,))           # parameter는 반드시 tuple 형태라야 함
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

# mid에 해당하는 데이터 한 건만 가져오기
def get_member_by_mid(mid):
    conn = sq.connect('test.db')
    cur = conn.cursor()

    sql = 'select * from member where mid=?;'
    cur.execute(sql, (mid,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    return row

# 데이터 추가하기
def insert_member(params):
    conn = sq.connect('test.db')
    cur = conn.cursor()

    sql = 'insert into member(mname, gender) values (?, ?);'
    cur.execute(sql, params)
    conn.commit()               # DB 내용을 변경하는 경우에는 반드시 commit()을 해주어야 함

    cur.close()
    conn.close()

# 데이터 수정하기 - 파라메터 순서에 주의할 것
def update_member(params):
    conn = sq.connect('test.db')
    cur = conn.cursor()

    sql = 'update member set mname=?, gender=? where mid=?;'
    cur.execute(sql, params)
    conn.commit()

    cur.close()
    conn.close()

# 데이터 삭제하기
def delete_member(mid):
    conn = sq.connect('test.db')
    cur = conn.cursor()

    sql = 'delete from member where mid=?;'
    cur.execute(sql, (mid,))
    conn.commit()

    cur.close()
    conn.close()