# car0 = {
#     'model':'lacetti',
#     'rangi':'oq',
#     'yil':2018,
#     'km':50000,
#     'narh':15000,
#     'karobka':'avtomat'
#     }
# car1 = {
#     'model':'bmw',
#     'rangi':'qora',
#     'yil':2018,
#     'km':500000,
#     'narh': 200000,
#     'karobka':'avtomat'
#     }
# car2 = {
#     'model':'gentra',
#     'rangi':'qora',
#     'yil':2018,
#     'km':20000,
#     'narh':20000,
#     'karobka':'mexanika'
#     }
#
# cars = [car0,car1,car2]
# for car in cars:
#     print(f"{car['model'].title()},"
#           f"{car['rangi']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$")
#
# print(cars[0])
# print(cars[0]['model'])

#
# malibus = []
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':None,
#         'yil':2020,
#         'narh':None,
#         'km':0,
#         'karobka':'avto'
#         }
#     malibus.append(new_car)
#
# print(malibus)

# for malibu  in malibus[:3]:
#     malibu['rang']='qizil'
#
# for malibu in malibus[3:6]:
#     malibu['rang']='qora'
# for malibu in malibus
#
# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#      'vali':{'familiya':'aliyev',
#            'tyil':2001,
#            'malumot':"o'rta maxsus",
#            'tillar':['html','c++']
#            },
#      'hasan':{'familiya':'husanov',
#            'tyil':1999,
#            'malumot':'maxsus',
#            'tillar':['python','php']}
#      }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()},"
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}.\n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())