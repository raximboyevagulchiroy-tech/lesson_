# talaba_0 = {
#     'ism':'Jonibek',
#     'familiya':'Uralov',
#     'yosh':22,
#     'fakultet':'kompyuter injinering',
#     'kurs':2
#     }
#
# print(talaba_0.items())
# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit:{kalit}")
#     print(f"Qiymat:{qiymat} \n")
#

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
#
# print(telefonlar.values())
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ")
# for telefon in telefonlar.values():
#     print(telefon)


#
# # for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")
#
# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':30000,
#     'shaftoli':40000,
#     'anjir':25000
#     }
#
# print(mahsulotlar.keys())
# print("Do\'kondagi mahsulotlar: ")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
#
# bozorlik = ['anor','uzum','non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'
#     }
#
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ")
# for telefon in set(telefonlar.values()):
#     print(telefon)

# thisset ={'apple', 'banana','orange','apple'}
# print(thisset)
#
# thisset ={'apple', 'banana','orange','apple',True,1,2}
# print(thisset)
#
# thisset ={'apple', 'banana','orange','apple',0,True,False}
# print(thisset)
# print(type(thisset))




