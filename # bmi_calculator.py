# bmi_calculator
name1      = "taha"                         
weight_kg1 = 90.00000000            #infomations about person number 1
height_m1  = 200.00000000

name2      = "taha brother1"
weight_kg2 =  80.00000000           #information about person number 2
height_m2  =  190.00000000

name3      = "taha brother3"
weight_kg3 = 60.00000000            #infomation about person number 3
height_m3  = 182.00000000

def bmi_calculator(name,height_m, weight_kg) :
    bmi = (weight_kg / (height_m**2)) * 10000                           #formula of bmi_calculator
    print("{}'s BMI: {:.2f}".format(name, bmi))                         #I choose this methode because its easy
    if bmi < 25:
        return name + (" not overweight")
    else:
        return name + ("is overweight ")

result1 = bmi_calculator(name1,height_m1,weight_kg1)
result2 = bmi_calculator(name2,height_m2,weight_kg2)
result3 = bmi_calculator(name3,height_m3,weight_kg3)
print(result1)
print(result2)                                                          #result (ready for run)
print(result3)