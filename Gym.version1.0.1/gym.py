import sqlite3
from athlete import Athlete

db = sqlite3.connect("Gym.sqlite")
cursor = db.cursor()


print("Insert : 1")
print("show : 2")
print("Delete : 3")

in_cast = int(input("What do you need : "))

if(in_cast == 1):

    cursor.execute("select max(Id) from sport")

    for Id in cursor:
        Id = Id[0]


    S = []
    while(True):
    
        name = input("Name : ")
        family = input("Family : ")
        tell = input("Tell : ")
        date = input("Date : ")

        Id += 1

        S1 = Athlete(Id, name, family, tell, date)
        S1.Payment = float(input("Payment : "))
        S.append(S1)

        finish = input("Continue?  1.YES/2.NO")

        if(finish == "1"):
            continue
        elif(finish == "2"):
            break

    for i in S:
        db.execute(f"insert into sport values({i._Id}, '{i._name}', '{i._family}', '{i._tell}', '{i._date}', {i.Payment})")

if(in_cast == 2):

    S = []

    while(True):

        code = input("select your records : ")

        if(code.isdigit()):

            code_cast = int(code)
            cursor.execute(f"select * from sport where Id = {code_cast}")
        elif(code.isalpha()):

            cursor.execute(f"select * from sport where name like '%{code}%'")
        else:
            print("ERROR!!!select ID or Name of your record in correct way.")

        for Id, name, family, tell, date, payment in cursor:
            S2 = Athlete(Id, name, family, tell, date, payment)
            S.append(S2)

        finish = input("Continue ?   1.YES/2.NO")
 
        if(finish == "1"):
            continue
        elif(finish == "2"):
            break

    for i in S:
        h = i.__str__()
        print(h)
        print("____" * 20)


if(in_cast == 3):

    c = input("Enter the ID or name which you want to delete : ")

    if(c.isdigit()):
        c_cast = int(c)    
        db.execute("delete from sport where Id = {}".format(c_cast))
    elif(c.isalpha()):
        db.execute("delete from sport where name = {}".format(c))
    else:
        print("ERROR!!!!!enter Id or name.")




db.commit()
cursor.close()
db.close()