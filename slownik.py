asia = {'imie' : 'Asia' , 'wiek' : 33}
maciek = {'imie' : 'Maciek' , 'wiek' : 33}

uczestnicy = [asia , maciek]
#
# # print(uczestniczka['imie'])
#
# for uczestniczka in uczestnicy:
#     # print(uczestniczka['imie'])
#     print(uczestniczka)
#     for imie, wiek in uczestniczka.items():
#         print(imie, wiek)

print(list(asia.values()))

for value in list(asia.values()):
    print(value)
