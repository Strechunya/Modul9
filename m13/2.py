col_b=int(input("Введите количество билетов"))
stoimost=0
S=0
for i in range(1,col_b+1):
    vozrast=int(input("Введите возраст посетителя: "))
    if vozrast<=17:
        stoimost=0
    elif 18<=vozrast<25:
        stoimost=990
    else:
         stoimost=1390
    S=S+stoimost
    print("Общая стоимость: ",S)
if col_b>3:
    S=S-(S*0.1)
    print("Стоимость со скидкой: ",S)








