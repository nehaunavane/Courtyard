#!/usr/bin/python


def bmi_cal(name, ht_m, wt_kg):
    bmi = wt_kg / (ht_m ** 2)   
    print("bmi : ")
    print(bmi)
    if bmi < 25:
        return name + "  is not overwight"
    else:
        return name + " is overwight" 
a = bmi_cal("Tom", 2, 49)
b = bmi_cal("Jerry", 1.5, 50)
print(a)
print(b)

