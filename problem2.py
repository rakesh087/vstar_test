import json

received_data=''#assuimg this variable will hold all datas
received_data=json.load(received_data)
over_weight_count=0
for each in received_data:
    each=json.load(each)
    height=each['HeightCm']
    weight=each['WeightKg']
    BMI=weight/(height/100)
    bmi_category=''
    health_risk=''
    if BMI<=18.4:
        bmi_category='Underweight'
    elif BMI>=18.5 and BMI<=24.9:
        bmi_category='Normal Weight'
    else:
        bmi_category='Over Weight'
        over_weight_count+=1

print('Number of over weight people are: ',over_weight_count)
