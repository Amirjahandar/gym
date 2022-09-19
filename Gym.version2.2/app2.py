import gym
import database 


while(True):
    print("Insert : 1")
    print("show : 2")
    print("Delete : 3")


    cin = int(input("select your request : "))

    if(cin == 1):

        maxId = database.getMaxAttribute('Drug', 'id')
        newId = maxId + 1

        name = input("drugName : ")
        company = input("Company : ")
        expire = input("Expire : ")
        count = int(input("Count : "))


        Drug = gym.Drug(Id = newId, name = name, company = company, expire = expire, count = count)

        cost = input("Price : ")
        if(cost.isdigit()):
            cast_cost = float(cost)
            Drug.Cost = cast_cost
        else:
            print("Price is not correct!")


        Drug.saveToDb()


    elif(cin == 2):
        cin2 = int(input("1.Drug s information / 2.Drug s users"))

        if(cin2 == 1):
            sort = input("Sort : ")

            info = gym.Drug.getDrugsInfo(sort)

            for i in info:
                print('ID: ',i[0], end='//')
                print('Drug: ', i[1], end='//')
                print('company: ', i[2], end='//')
                print('Expire: ', i[3], end='//')
                print('Price: ', i[4], end='//')
                print('Count: ', i[5])
                print(10 * '_____________')

        elif(cin2 == 2):
            drug = input("Insert name of drug : ")

            z = gym.Drug.getDrugsUsers(drug)
            for i in z:
                print('ID:',i[0], end='// ')
                print('Drug:', i[1], end='// ')
                print('company:', i[2], end='// ')
                print('user_id:', i[3], end='// ')
                print('user_name:', i[4], end='// ')
                print('user_family:', i[5])
                print(10 * '_________')


    elif(cin == 3):
        cin3 = input("Insert ID of drug that you want delete : ")

        gym.Drug.deleteDrugInfo(cin3)


    cin4 = input("Do you want to Exit ?  1.Yes/2.No")
    if(cin4 == '1'):
        break
    else:
        continue

