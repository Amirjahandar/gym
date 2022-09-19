from database import connect, disconnect
import psycopg2


class Athlete(object):

    def __init__(self, name, family, age, sex, tell="unknown",  Id= None,):

        self._name = name
        self._family = family
        self._age = age
        self._sex = sex
        self._tell = tell
        self._Id = Id



    def createID(self):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute("select Max(id) last_id from Athlete")
                b = cur.fetchone()
                c = b[0]
                cast_c = int(c) + 1
                self._Id = cast_c




    def saveToDb(self):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute("insert into Athlete values(%s, %s, %s, %s, %s, %s)", (self._Id, self._name, self._family, self._age, self._sex, self._tell) )

        print("Confrimed!")


    def showRecord(self):
        print("ID: ", self._Id)
        print("Name: ", self._name)
        print("Family: ", self._family)
        print("Age: ", self._age)
        print("Sex: ", self._sex)
        print("Tell: ", self._tell)


    @classmethod
    def getUsersInfo(cls, sortby):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute(f"select * from Athlete At join Sex S on At.sex = S.sex_id order by {sortby}")
                x = cur.fetchall()
                object_list = list()
                for i in x:
                    S = cls(i[1], i[2], i[3], i[7], i[5], i[0])
                    object_list.append(S)

                return object_list


    @classmethod
    def getUserByID(cls, person_ID):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute(f"select * from Athlete At join Sex S on At.sex = S.sex_id where ID = {person_ID} ")
                x = cur.fetchone()

                return cls(x[1], x[2], x[3], x[7], x[5], x[0])


    @classmethod
    def getUserByName(cls, person_name):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute(f"select * from Athlete At join Sex S on At.sex = S.sex_id where At.name like'%{person_name}%' ")
                x = cur.fetchall()

                object_list = list()
                for i in x:
                    S = cls(i[1], i[2], i[3], i[7], i[5], i[0])
                    object_list.append(S)

                return object_list

    



class Bmi(object):
    def __init__ (self, ID, weight=0, hight=0, bmi=0, weightDate=None):
        self._Id= ID
        self._weight= weight
        self._hight= hight
        self._bmi= bmi
        self._weightDate= weightDate



    def bmi(self):
        bmi= (self._weight / (pow((self._hight/100), 2)))
        self._bmi = bmi


    def saveToDb(self):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute("insert into BMI values(%s, %s, %s, %s)", (self._Id, self._weight, self._hight, self._bmi))
                
                print("confrimed!")


    def showBmi(self):
        print("ID: ", self._Id)
        print("Weight: ",  self._weight)
        print("Hight: ", self._hight)
        print("BMI: ", self._bmi)
        print("weightDate: ", self._weightDate)




    @classmethod
    def getUsersBmi(cls):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute("select * from Bmi order by person_id")
                x = cur.fetchall()
                object_list = list()
                for i in x:
                    s= cls(i[0], i[1], i[2], i[3], i[4])
                    object_list.append(s)

                return object_list 


    @classmethod
    def getUserBmiByID(cls, person_ID):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute(f"select * from BMI where person_id = {person_ID}")
                x = cur.fetchall()
                object_list = list()
                for i in x:
                    s= cls(i[0], i[1], i[2], i[3], i[4])
                    object_list.append(s)

                return object_list 









