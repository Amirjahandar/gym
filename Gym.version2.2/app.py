import gym
import database


print("Insert : 1")
print("show : 2")
print("Delete : 3")

cin = int(input("select your request : "))

if(cin == 1):
    cin2 = int(input("1.Insert new user / 2.Insert user sport / 3.Insert user drug"))
    if(cin2 == 1):
        maxUserId = database.getMaxAttribute('Users', 'user_id')
        newUserId = maxUserId + 1

        name = input('Name : ')
        family = input('Family : ')
        age = input('Age : ')
        print("0.Male//1.Female")
        sex = input('Sex : ')
        weight = input('Weight : ')
        hight = input('Hight : ')
        tell = input('Tell : ')
        date = input('Date : ')
    
        user = gym.Athlete(newUserId, name, family, age, sex, weight, hight, tell, date)

        pay = input("Enter your payment :")
        if(pay.isdigit()):
            cast_pay = int(pay)
            user.Payment = cast_pay
        else:
            print('Payment is Incorrect!')


        user.saveToDb()
    
        z = database.getTableInfo('Sports')
        for i in z:
            print(i)
    
        sport_id = int(input("Enter sport : "))

        user.insertUserSport(sport_id)

    elif(cin2 == 2):
        user_id = int(input("Enter user ID, please :"))
        user = gym.Athlete.getUsersById(user_id)

        z = database.getTableInfo('Sports')
        for i in z:
            print(i)
    
        sport_id = int(input("Enter sport : "))

        user.insertUserSport(sport_id)


    elif(cin2 == 3):
        user_id = int(input("Enter user ID, please :"))
        user = gym.Athlete.getUsersById(user_id)

        z = database.getTableInfo("Drug")
        for i in z:
            print(i)
            
        drug_id = int(input("Enter drug : "))

        user.insertUserDrug(drug_id)
        


elif(cin == 2):

    search = input("To show all of information select SPACE ,also you can get it by Family or Id : ")

    if(search.isspace()):

        sort = input("Sort by :")
        info = gym.Athlete.getUsersInfo(sort)

        for i in info:
            print("UserId :", i[1], end=' // ')
            print("Name :", i[2], end=' // ')
            print("Family :", i[3], end=' // ')
            print("Age :", i[4], end=' // ')
            print("Sex :", i[12])
            print("weight :", i[6], end=' // ')
            print("Hight :", i[7], end=' // ')
            print("Tell :", i[8], end=' // ')
            print("Date :", i[9], end=' // ')
            print("Payment :", i[10])
            print( 10 * '______________')

    elif(search.isalpha()):
        info = gym.Athlete.getUserByfamily(search)

        for i in info:
            print("UserId :", i[1], end=' // ')
            print("Name :", i[2], end=' // ')
            print("Family :", i[3], end=' // ')
            print("Age :", i[4], end=' // ')
            print("Sex :", i[12])
            print("weight :", i[6], end=' // ')
            print("Hight :", i[7], end=' // ')
            print("Tell :", i[8], end=' // ')
            print("Date :", i[9], end=' // ')
            print("Payment :", i[10])
            print( 10 * '______________')

    elif(search.isdigit()):
        cast_search = search
        info = gym.Athlete.getUsersById(cast_search)

        print(info)
        print(info.Payment)


elif(cin == 3):
    Id = int(input("For delete record you must enter ID :"))
    gym.Athlete.deleteUser(Id)

