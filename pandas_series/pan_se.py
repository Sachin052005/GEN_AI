import pandas as pd
bikes=pd.Series(["Royal Enfield","Bajaj Pulsar","TVS","Yamaha","Honda"])
print(bikes)
print("\ntype :" ,type(bikes))


print("\nEXTRINSIC INDEX")
brand=pd.Series(["Royal Enfield","Bajaj Pulsar","TVS","Yamaha","Honda"],
                index=["Classic 350","N160","Apache RTR","MT-15","SP 125"])
print(brand)



print("\nSHORTED_BY_INDEX")
models=pd.Series(["Royal Enfield","Royal Enfield Hunter","Bajaj Pulsar","TVS","Yamaha","Honda","Yamaha R15"],
                index=["Classic 350","Classic 350","N160","Apache RTR","MT-15","SP 125","MT-15"])
print('only print Royal Enfield :\n',models['Classic 350'])


print("\nDEPARTMENT_DETAILS")
student_dep=pd.Series({'sachin':'CSBS','arul':'IT','joshua':'cse','infant':'MECH'})
print(student_dep)


print("\nPRINT SPECIFIC SET OF ROW FROM START")
student_dep_short=pd.Series({'sachin':'CSBS','arul':'IT','joshua':'cse','infant':'MECH'})
print(student_dep_short.head(2))


print("\nPRINT SPECIFIC SET OF ROW FROM END")
student_dep_short_end=pd.Series({'sachin':'CSBS','arul':'IT','joshua':'cse','infant':'MECH'})
print(student_dep_short_end.tail(3))


print("\nDETAILS")
models_details=pd.Series(["Royal Enfield","Royal Enfield Hunter","Bajaj Pulsar","TVS","Yamaha","Honda","Yamaha R15"],
                index=["Classic 350","Classic 350","N160","Apache RTR","MT-15","SP 125","MT-15"])
print(models_details.describe())


print("\nSLICING")
models_slicing=pd.Series(["Royal Enfield","Royal Enfield Hunter","Bajaj Pulsar","TVS","Yamaha","Honda","Yamaha R15"])
print(models_slicing[1:3])
print("\nREVERSED")
print(models_slicing[::-1])
print("\nSLICE BY JUMPING")
print(models_slicing[0:7:2])
