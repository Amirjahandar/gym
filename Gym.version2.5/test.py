from athlete import Athlete, Bmi


# a = Athlete.getUsersInfo('ID')
# for i in a:
#     print(i)


# s = Athlete("davood", "heydarpour", 30, 0, "09334561122")
# s.createID()
# s.saveToDb()

# print(s._Id, s._name, s._tell)



# a = Athlete.getUserByID(7128)
# print(a._Id, a._name, a._family, a._age, a._sex, a._tell)

# b = Athlete.getUserByName('Amir')
# for i in  b:
#     i.showRecord()
    # print(5 * '////////////')

a =  Athlete.getUsersInfo('Id')
for i in a:
    i.showRecord()
    print(5 * '_________________')



s = Bmi.getUsersBmi()
for i in  s:
    i.showBmi()
    print(5 * '_________')






