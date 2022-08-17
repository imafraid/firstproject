import pymysql
import pymysql.cursors


def get_conn():
    return pymysql.connect(
        host='47.117.52.162',
        port=32171,
        user='root',
        password='78RxktksG2z3NrDL',
        database='xyy_settings_db',
        charset='utf8'
    )


def insert_or_update(sql):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()


def query_data(sql):
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn.close()


if __name__ == "__main__":
    sql = "select * from employee"
    datas = query_data(sql)
    import pprint

    pprint.pprint(datas)
