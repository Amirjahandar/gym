import athlete



flag = True

while(flag):

    c_in = input("1.insert / 2.show")

    if(c_in == "1"):
        d_in = input("1.new Athlete / 2.new BMI record")
        if(d_in == "1"):
            a = input("Name : ")
            b = input("family : ")
            c = int(input("age : "))
            d = int(input("sex : 0.Male/1.Female"))
            e = input("Tell : ")      

            S = athlete.Athlete(a, b, c, d, e)
            S.createID()
            S.saveToDb()

        elif(d_in == "2"):
            a = input("ID : ")
            b = float(input("Weight : "))
            c = float(input("Hight : "))
            
            S = athlete.Bmi(a, b, c)
            S.bmi()
            S.saveToDb()
            

    elif(c_in == "2"):
        f_in = input("1.show Athlete records / 2.show BMI records ")
        if(f_in == '1'):
            d_in = input("For all records enter Space but for special record enter ID or NAME :")
            if(d_in.isspace()):
                sort = input("SortBy: ")
                S = athlete.Athlete.getUsersInfo(sort)
                for i in S:
                    i.showRecord()
                    print(5 * '_______________')
            elif(d_in.isdigit()):
                S = athlete.Athlete.getUserByID(d_in)
                S.showRecord()
            elif(d_in.isalpha()):
                S = athlete.Athlete.getUserByName(d_in)
                for i in S:
                    i.showRecord()
                    print(5 * '_______________')

        elif(f_in == '2'):
            d_in = input("For all BMI enter space and for special BMI record enter person_id :")
            if(d_in.isspace()):
                S = athlete.Bmi.getUsersBmi()
                for i in S:
                    i.showBmi()
                    print(5 * '_______________')
            elif(d_in.isdigit()):
                S = athlete.Bmi.getUserBmiByID(d_in)
                for i  in  S:
                    i.showBmi()
                    print(5 * '_______________') 


                        
    a = input("quit ? 1.Yes / 2.NO")
    if(a == '1'):
        flag = False
    else:
        continue


final = input("Have nice time!")










































