# son = 1
# while son<=5:
#     print(son, end = ',')
#     son = son + 1

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting:"
# savol+= "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)

# while True:
#     print("01010101", end = ' ')

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)

# sonlar = list(range(1,100))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# ismlar = []
#
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n = 1
# while True:
#     savol = f"{n}-do'stingizni ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob == "ha":
#         n+=1
#         continue
#     else:
#         break
# print(ismlar)

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
#
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# cars = ['lacetti','nexia','tayota','nexia','audio','malibu', 'nexia']
# while'nexia' in cars:
#     cars.remove('nexia')
# print(cars)
#
# talabalar = ['jonibek','husan','olim','botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
#
# print(baholangan_talabalar)







