import json
import csv

received_data=''#assuimg this variable will hold all datas
received_data=json.load(received_data)

#Write the header of csv result file
with open('result.csv','w', newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['HeightCm','WeightKg','BMI','BMI category','Risk catageory'])

#based on given data of BMI and Health risk , i created dictionary using BMI as key and Health risk as value
bmi_risk={'under_weigh':'Malnutrition ','normal_Weight':'Low risk','over_weight':'Enhanced risk',
'moderately_obese':'Medium risk','severely_obese':'High risk','very_severely_obese':'Very high risk'}

#HeightCm,WeightKg
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
    elif BMI>=25 and BMI<=29.9:
        bmi_category='Overweight'
    elif BMI>=30 and BMI<=34.9:
        bmi_category='Moderately obese'
    elif BMI>=35 and BMI<=39.9:
        bmi_category='Severely obese'
    else:
        bmi_category='Very severely obese'
    health_risk=bmi_ris[bmi_category]
    with open('result.csv','a', newline='') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow([height,weight,BMI,bmi_category,health_risk])

