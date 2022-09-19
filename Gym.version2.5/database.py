import  psycopg2

def connect():
    x = psycopg2.connect(user="postgres", password="111", database="Gym_sport", host="localhost")
    return x


def disconnect(connectionName, cursorName):
    connectionName.commit()
    cursorName.close()
    connectionName.close()
    print("confrim!")




















