import psycopg2

def connect():
    x = psycopg2.connect(user = 'postgres', password = '111', database = 'Gym', host = 'localhost')
    return x


def getMaxAttribute(table, attribute):
    with connect() as con:
        with con.cursor() as cur:
            cur.execute(f"select max({attribute}) from {table}")
            x = cur.fetchone()
            Max = x[0]

    return Max


def getTableInfo(table):
    with connect() as con:
        with con.cursor() as cur:
            cur.execute(f"select * from {table}")
            x = cur.fetchall()

    return x

