import math

myDict = {

}

#creating/ defining variables


firstName = input('What is your first name? ')
myDict['firstName'] = firstName
lastName = input('What is your last name ' + firstName + '?')
myDict['lastName'] = lastName
age = int(input('How old are you ' + firstName + '?'))
myDict['age'] = age
gender = input('What gender do you identify as? ')
myDict['gender'] = gender

#weight, waist, height , neck , hip(if female)


print(myDict)
hasTape = input('If you have a measuring tape, type yes, or else say no. You will require the use of a measuring tape for the below to get a full report. At the very least, you need an accurate height and weight measurement. ')


if(hasTape == 'yes'):
    print('You are good to go! Measure yourself in inches based on the body part specified. ')
   # metric = input('You are good to go! Type metric if all the measurements you have are in centimeters/kilograms. ')
else:
    print('At the very least, you need an accurate measurement of your height in inches and weight in pounds.')
   # metric = input('At the very least, you need an accurate measurement of your height in inches and weight in pounds. If you have height and other measurements in centimeters, and weight in kilograms, type metric accurately.')


waist = float(input('How large is your waist in inches(tape has to go over your belly button)? '))
height = float(input('How tall are you in inches? '))
neck = float(input('How large is your neck? '))
weight = float(input('How much do you weight? '))

if (gender == 'female'):
    hip = float(input('How many inches is your hip? '))
    myDict['hip'] = hip
else:
    pass

#BMI being calculated below
def BMI( a, b):
    return a/(b*b)*703


BMI = BMI(weight, height)
BMI = round(BMI, 2)
myDict['BMI'] = BMI
print('Your BMI is: ')
print(BMI)


def waistToHeight(x, y):
    return x/y

waistToHeight = waistToHeight(waist, height)
waistToHeight = round(waistToHeight , 2)
myDict['waistToHeight'] = waistToHeight
print('Your waist to height ratio is: ')
print(waistToHeight)

if(gender == 'female'):
    def percentageOfBodyFat(hip, waist, height, neck):
        return 163.205 * math.log10(waist + hip - neck) - 97.684 * math.log10(height) - 78.387
        #163.205 * math.log10(waist + hip - neck) - 97.684 * math.log10(height) - 78.387
    percentageOfBodyFat = percentageOfBodyFat(hip, waist, height, neck)
    round(percentageOfBodyFat, 2)
    myDict['percentageOfBodyFat'] = percentageOfBodyFat
    print('Your body percentage of fat is: ')
    print(myDict.get('percentageOfBodyFat'))
else:
    def percentageOfBodyFat(waist, height, neck):
        return 86.010 * math.log10(waist - neck) - 70.041 * math.log10(height) + 36.76
    percentageOfBodyFat = percentageOfBodyFat(waist, height, neck)
    round(percentageOfBodyFat,2)
    myDict['percentageOfBodyFat'] = percentageOfBodyFat
    print('Your body percentage of fat is: ')
    print(myDict.get('percentageOfBodyFat'))

#ranking body into groups
if(BMI<18.5):
    print('You are underweight. This product does not apply to you, only to people who are overweight or obese. Please go see a medical professional to see how you can be in a healthy weight range.')
elif(18.5<=BMI<=24.9):
    print('You are at a healthy/average weight for a human. This app does not apply to you, but only to people who are overweight or obese. If you would like to get more fit, please go see a medical professional/fitness trainer. ')
elif(25<=BMI<=29.9):
    print('You are overweight. Please continue to find ways to get to a healthy, yet reachable goal weight/body measurement.\n NOTE: THIS IS NOT GUIDANCE FROM A MEDICAL PROFESSIONAL. IF ANYTHING HAPPENS TO YOU, THIS CREATORS OF THE APP ARE NOT AT FAULT.')
else:
    print('You are obese, it is highly suggested for you to reach a healthy weight to prevent various diseases you are likely to attain. Please continue to see more ways to lose weight.\n NOTE: THIS IS NOT GUIDANCE FROM A MEDICAL PROFESSIONAL. IF ANYTHING HAPPENS TO YOU, THE CREATORS OF THIS APP ARE NOT AT FAULT.')

#classifying waistToHeight ratio for men and woman(is different for them), so creating if-statement within if-statement

if(gender == 'female'):
    if(waistToHeight<=0.34):
        print('You are classified as extremely slim for your waist to height ratio. Please seek guidance of a medical professional to see how to bring yourself to a healthy weight. This app is NOT for you, so do not use the app.')
    elif(0.35<=waistToHeight<=0.41):
        print('You are classified as slim for your waist to height ratio. Please seek guidance of a medical professional to see how to bring yourself to a healthy weight. This app is NOT for you, so do not use the app.')
    elif(0.42<=waistToHeight<0.48):
        print('You are classified as healthy/average for your waist to height ratio. This app is NOT meant for you. If you plan on getting more fit, please seek the guidance of a medical/fitness professional. THIS WILL NOT BENEFIT YOU.')
    elif(0.49<=waistToHeight<=0.53):
        print('You are classified as overweight for your waist to height ratio. Please continue with the app to bring yourself to a healthy weight. NOTE: THIS IS NOT GUIDANCE FROM A MEDICAL PROFESSIONAL. PROCEED WITH YOUR OWN RISK.')
    elif(0.54<=waistToHeight<=0.57):
        print('You are classified as highly overweight for your waist to height ratio. Please continue with the app to bring yourself to a healthy weight. NOTE: THIS IS NOT GUIDANCE FROM A MEDICAL PROFESSIONAL. PROCEED WITH YOUR OWN RISK.')
    else:
        print('You are classified as morbidly obese for your waist to height ratio. Please continue with the app to bring yourself to a healthy weight. NOTE: THIS IS NOT GUIDANCE FROM A MEDICAL PROFESSIONAL. PROCEED WITH YOUR OWN RISK.')
else:
    if(waistToHeight<=0.34):
        print('You are classified as extremely slim for your waist to height ratio. Please seek guidance of a medical professional to see how to bring yourself to a healthy weight. \n This app is NOT for you, so do not use the app.')
    elif(0.35<=waistToHeight<=0.42):
        print('You are classified as slim for your waist to height ratio. Please seek guidance of a medical professional to see how to bring yourself to a healthy weight. \n This app is NOT for you, so do not use the app.')
    elif(0.43<waistToHeight<=0.52):
        print('You are classified as healthy/average for your waist to height ratio. This app is NOT meant for you. \nIf you plan on getting more fit, please seek the guidance of a medical/fitness professional. THIS WILL NOT BENEFIT YOU.')
    elif(0.53<=waistToHeight<=0.57):
        print('You are classified as overweight for your waist to height ratio. Please continue with the app to bring yourself to a healthy weight. \n NOTE: THIS IS NOT GUIDANCE FROM A MEDICAL PROFESSIONAL. PROCEED WITH YOUR OWN RISK.')
    elif(0.58<=waistToHeight<=0.62):
        print('You are classified as highly overweight for your waist to height ratio. Please continue with the app to bring yourself to a healthy weight.\n NOTE: THIS IS NOT GUIDANCE FROM A MEDICAL PROFESSIONAL. PROCEED WITH YOUR OWN RISK.')
    else:
        print('You are classified as morbidly obese for your waist to height ratio. Please continue with the app to bring yourself to a healthy weight.\n NOTE: THIS IS NOT GUIDANCE FROM A MEDICAL PROFESSIONAL. PROCEED WITH YOUR OWN RISK.')


if(BMI>=25.0 and waistToHeight>0.52):
    print('You are classified as overweight or obese. NOTE: Not advice from a medical professional')
elif(BMI>=25.0 and waistToHeight<0.52):
    print("You are likely not overweight or obese. Please check with a medical professional to get a full examination to determine your health.")
elif(BMI<25.0 and waistToHeight<=0.52):
    print('You are healthy or slim, please check with a medical professional for a thorough examination.')


#trying to give calories intake to people
if (gender == 'female'):
    BMR = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    exerciseLevel = input('How active are you? Type in the letter. \n a. sedentary(little to no exercise) \n b. light exercise(1-3 times per week) \n c. moderate exercise(3-5 times per week) \n d. very active(6-7 times per week) \n e. extra active(do twice normal exercise everytime. Work in fitness industry. Very hard exercise.) ')
    if(exerciseLevel == 'a' or exerciseLevel =='A'):
        exerciseLevel == 'sedentary'
    elif(exerciseLevel == 'c' or exerciseLevel == 'C'):
        exerciseLevel == 'moderateExercise'
    elif(exerciseLevel == 'd' or exerciseLevel == 'D'):
        exerciseLevel == 'veryActive'
    elif(exerciseLevel == 'e' or exerciseLevel == 'E'):
        exerciseLevel == 'extraActive'
    else:
        exerciseLevel == 'lightExercise'
    if(exerciseLevel == 'sedentary'):
        BMR = BMR*1.2
    elif(exerciseLevel == 'moderateExercise'):
        BMR = BMR * 1.55
    elif(exerciseLevel == 'veryActive'):
        BMR = BMR*1.725
    elif(exerciseLevel == 'extraActive'):
        BMR = BMR*1.9
    else:
        BMR = BMR * 1.375
else:
    BMR = 66 + (6.3 * weight) + (12.9 * height) - (6.8 *age)
    exerciseLevel = input('How active are you? Type in the letter. \n a. sedentary(little to no exercise) \n b. light exercise(1-3 times per week) \n c. moderate exercise(3-5 times per week) \n d. very active(6-7 times per week) \n e. extra active(do twice normal exercise everytime. Work in fitness industry. Very hard exercise.) ')
    if(exerciseLevel == 'a' or exerciseLevel =='A'):
        exerciseLevel == 'sedentary'
    elif(exerciseLevel == 'c' or exerciseLevel == 'C'):
        exerciseLevel == 'moderateExercise'
    elif(exerciseLevel == 'd' or exerciseLevel == 'D'):
        exerciseLevel == 'veryActive'
    elif(exerciseLevel == 'e' or exerciseLevel == 'E'):
        exerciseLevel == 'extraActive'
    else:
        exerciseLevel == 'lightExercise'
    if(exerciseLevel == 'sedentary'):
        BMR = BMR*1.2
    elif(exerciseLevel == 'moderateExercise'):
        BMR = BMR * 1.55
    elif(exerciseLevel == 'veryActive'):
        BMR = BMR*1.725
    elif(exerciseLevel == 'extraActive'):
        BMR = BMR*1.9
    else:
        BMR = BMR * 1.375

round(BMR, 2)
myDict['BMR'] = BMR
print('The amount of calories you should have in a day are: ')
print(BMR)











  #  print('e. extra active(do twice normal exercise everytime. Work in fitness industry. Very hard exercise.)')

 #   print('Your BMR(Basal Metabolic Rate) ')
#Adult male: 66 + (6.3 x body weight in lbs.) + (12.9 x height in inches) - (6.8 x age in years) = BMR
#Adult female: 655 + (4.3 x weight in lbs.) + (4.7 x height in inches) - (4.7 x age in years) = BMR





#for people if they have the measurements in centimeters/kilograms to help with conversion, basically copy of previous code, just that it converts into US Customary system and uses same formulas
#if(metric == 'metric'):
 #   metricHeight = input('How many centimeters tall are you? ')
  #  metricWaist = input('How many centimeters are your waist? ')
   # metricNeck = input('How many centimeters is your neck? ')
   # metricWeight = input('How many kilograms do you weight? ')
    #if(gender=='female'):
     #   metricHip = input('How many centimeters is your hip')
      #  hip = metricHip/2.54
    #waist = metricWaist/2.54
    #neck = metricNeck/2.54
    #weight = metricWeight*2.205
    #if(gender == 'female'):
     #   percentageOfBodyFat = percentageOfBodyFat(hip, waist, height, neck)
      #  round(percentageOfBodyFat, 2)
       # myDict['percentageOfBodyFat'] = percentageOfBodyFat
        #print('Your body percentage of fat is: ')
        #print(myDict.get('percentageOfBodyFat'))







#basicsRequired = input('To create a diagnosis(not from a medical professional but from popular tools physicians use), \n you require a measuring tape. At the very least, you need an accurate measurement of your height and weight in inches and pounds, respectively. \n If you have these measurements in metric system, please type metric. For the following, a tape measure is suggested to computate your body fat percentage, BMI, and waist to height ratio.')
#if (basicsRequired == 'metric'):












#waist = float(input('How many inches is your waist? '))
#myDict['waist'] = waist
#height = float(input('How tall are you inches? '))
#myDict['height'] = height





