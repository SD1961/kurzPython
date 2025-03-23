#zaverzovano GIT /c//Projects/projektPython/sd (master)
#zmena 1
from pip._internal.cli.cmdoptions import python


numbers = [1, 2, 4, -6, 7, 8, 100, -125, 11, 123]
names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
random_codes = ["1-okdsdsaaaTTT", "0-nFnlddXX", "0-AA", "0-uwqqq", "2-ZSTh", "0-RKOcsxxx", "1-LwWtss", "0-cdKiddd", "2-KpAAaa", "3-sOdSxhcds"]

# 1. pomocí cyklu for vypište čísla ze seznamu numbers, ale přeskočte záporná čísla.
for x in numbers:
    if x >= 0:
        print(x)
print('konec')

# 2. pomocí cyklu while vypište všechna jména, pokud narazíš na jméno 'Alice' cyklus ukonči
ii = 0
new_list = []
while ii < len(names):
   if names[ii] not in 'Alice':
       new_list.append(names[ii])
   else:
       break
   ii += 1
print(new_list)

# 3. pomocí list comprehension vytvoř nový list, který bude obsahovat pouze prvky z 'random_codes', které obsahují 0
new_list = [x for x in random_codes if "0" in x  ]
print(new_list)
# Dobrovolny ukol pro pokrocile (nebude bodovan): Vypis všechny pod-seznamy s alespoň třemi po sobě jdoucími stejnými znaky v seznamu 'random_codes'
#new_list_3 = [x for x in random_codes if "0" in x  ]
import re
result =[]
final_result = []
for item in random_codes:
    result =  re.findall(r'(\w)\1', item) #dva stejne znaky za sebou
    #print(result)
    if result != []:
        for res in result:
            strX = str(res)+ str(res) + str(res)
            if item.find(strX) > 0:
                final_result.append(item)
final_result = set(final_result)
print(final_result)
print('konec')



result =[]
final_result = []
for item in random_codes:
    print(item)

final_result = set(final_result)
print(final_result)
print('konec')



