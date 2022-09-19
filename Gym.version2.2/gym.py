from database import connect

class Athlete(object):
    def __init__(self, userId, name, family, age, sex, weight = 'Unknown', hight ='Unknown', tell= '09**..***', date = 'yy/mm/dd', payment= 0, Id = None):
        self._userId = userId
        self._name = name
        self._family = family
        self._age = age
        self._sex = sex
        self._weight = weight
        self._hight = hight
        self._tell = tell
        self._date = date 
        self._payment = payment
        self._Id = Id


    def _set_pay(self, payment):
        if(isinstance(payment, int) and payment > 0):
            self._payment = payment
        else:
            print("Enter your payment in correct way !")

    def _get_pay(self):
        return self._payment

    Payment = property(_get_pay, _set_pay)



    def saveToDb(self):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute("insert into Users( user_id, name, family, age, sex, weight, hight, tell, date, payment) values(%s, %s,  %s, %s, %s, %s, %s, %s, %s, %s )",
                (self._userId, self._name, self._family, self._age, self._sex, self._weight, self._hight, self._tell, self._date, self._payment))


    def insertUserSport(self, sport_id):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute("select id from Users where user_id = {}".format(self._userId))
                Id = cur.fetchone()
                cur.execute("insert into us_Sport values(%s, %s) ", (Id, sport_id ))



    def insertUserDrug(self, drug_id):
        with connect() as con:
            with con.cursor()  as cur:
                cur.execute("Insert into us_drug values(%s, %s)", (self._Id, drug_id))




    @classmethod
    def getUsersInfo(cls, sort):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute(f"select * from  Users Us join sex S on Us.sex = S.sex_id order by {sort} Asc")
                z = cur.fetchall()
        return z


    @classmethod
    def getUserByfamily(cls, family):
        with connect() as con:
            with con.cursor()  as cur:
                cur.execute(f"select * from Users Us join sex S on Us.sex = S.sex_id where family like '%{family}%' ")
                z = cur.fetchall()

        return z


    @classmethod
    def getUsersById(cls, Id):
        with connect() as con:
            with con.cursor()  as cur:
                cur.execute("select * from Users Us join sex S on Us.sex = S.sex_id where user_id = %s ", (Id,))
                z = cur.fetchone()
        
        return cls(userId= z[1], name = z[2], family = z[3], age = z[4], sex = z[12], weight = z[6], hight = z[7], tell = z[8], date = z[9], payment = z[10], Id = z[0] )


    @classmethod
    def deleteUser(cls, Id):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute("select id from Users where user_id = %s", (Id,))
                _id = cur.fetchone()
                cur.execute("Delete from us_sport where id = %s ", (_id,))
                cur.execute("Delete from us_drug where id = %s ", (_id,))
                cur.execute("Delete from Users where user_id = %s", (Id,))


    def __str__(self):
        return "UserId: {} // Name: {} // Family: {} // Age: {} // Sex: {} // Weight: {} // Hight: {} // Tell: {} // Date: {}".format(self._userId, self._name, self._family, self._age, self._sex, self._weight, self._hight, self._tell, self._date)


# ========================== #


class Drug(object):
    def __init__(self, Id, name, company, expire = "yy/mm/dd", cost = 0, count = 0):
        self._Id = Id
        self._name = name
        self._company = company
        self._expire = expire
        self._cost = cost
        self._count = count


    def _set_cost(self, cost):
        if(isinstance(cost, float), cost >= 0):
            self._cost = cost
        else:
            print("ERROR!enter your cost in correct way.")


    def _get_cost(self):
        return self._cost


    Cost = property(_get_cost, _set_cost)


    def saveToDb(self):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute("insert into Drug values(%s, %s, %s, %s, %s, %s)", 
                (self._Id, self._name, self._company, self._expire, self._cost, self._count))
                

    @classmethod
    def getDrugsInfo(cls, sort):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute(f"select * from Drug order by {sort} Asc")
                x = cur.fetchall()
                
        return x


    @classmethod
    def getDrugsUsers(cls, drugName):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute("select D.id, D.drug, D.company, U.user_id, U.name, U.family from Drug D join us_drug Ud on D.id = Ud.drug_id join Users U on Ud.id = U.id where drug = %s", (drugName,))
                x = cur.fetchall()

        return x 


    @classmethod
    def deleteDrugInfo(cls, drugId):
        with connect() as con:
            with con.cursor() as cur:
                cur.execute("Delete from drug where id = %s", (drugId,))




