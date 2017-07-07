list3 = [3,12,99,42,67,5,37,84]

def getbiggernumber(list3):
    maximum = list3[0]
    for c in list3:
        if maximum<c:
            maximum=c
    print (maximum)

getbiggernumber(list3)
