import math


# for Body-Mass-Index , BMI need weight and height
#empty dictionary to input data later
myDict = {

}
# for measurements for body fat for boy, need waist, height, and neck measurements
# for measurements of body fat for girl, need waist, hip , height, neck measurements


# getting all inputs of measurements needed for determining future body measurements
#firstName = input("What is your FIRST name?")
#lastName = input('Hi ' + firstName + '! What is your LAST name?')
#fullName = firstName + ' ' + lastName
#gender = input("Are you male or female?")
#myDict['gender'] = gender
#age = int(input('How old are you ' + firstName + '? Please type a real number with out decimals.'))
#myDict['age'] = age


#code to make sure only kids/teens are using the app, not for others
#if (age > 18):
 #   print('Sorry, this app is meant for kids/teens to learn how to lose weight. If you want to continue, please reload the page, and re-eneter your age as 18.')
#else:
 #   pass

#print('Here are some tips for measuring your waist. Please use a tape measure, and do not tightly or loosely measure your waist. If needed, measure 3 times to get an accurate idea of the correct measurement you have.')


#weight = float(input('Please enter how many pounds you weigh: '))
#myDict['weight'] = weight
#waist = float(input('What is the size of your waist in inches ' + firstName + '? Please type a positive number, if there are decimals, please include them.'))
#myDict['waist'] = waist
#height = float(input('How tall are you in inches ' + firstName + "? Please type a positive number."))
#myDict['height'] = height
#neck = float(input('What is the size of your neck in inches? Please a postive number and round it to the nearest number. Like 5.5 rounds to 6.'))
#myDict['neck'] = neck


#BMI being calculated below
#def BMI(a, b):
 #   return a/(b*b)*703


#BMI = BMI(weight, height)
#BMI = round(BMI, 2)
#print(BMI)

#myDict['BMI'] = BMI

#BASIS OF HOW I AM GOING TO PRINT OUT STUFF
#print('Here is your BMI: ')
#print(BMI)

#def waistToHeight(x, y):
 #   return x/y

#waistToHeight = waistToHeight(waist, height)
#waistToHeight = round(waistToHeight , 2)
#myDict['waistToHeight'] = waistToHeight
#print(waistToHeight)

#print(myDict)








#need to find percentile for BMI, waist to height ratio, and need to tell if they are overweight, obese, normal, underweight, etc! FIX IT SOON

#if(gender == 'female'):
 #   hip = float(input('What is the size of your hip in inches?'))
  #  def percentageOfBodyFat(hip, waist, height, neck):
   #     return 163.205*math.log(waist+hip-neck)-97.684*math.log(height)-78.387
    #percentageOfBodyFat = percentageOfBodyFat(hip, waist, height, neck)
    #round(percentageOfBodyFat, 2)
    #myDict['percentageOfBodyFat'] = percentageOfBodyFat
    #print(myDict.get('percentageOfBodyFat'))

#else:
 #   def percentageOfBodyFat(waist, height, neck):
  #      return 86.010 * math.log(waist-neck)-70.041 * math.log(height)+36.76
   # percentageOfBodyFat = percentageOfBodyFat(waist, height, neck)
   # round(percentageOfBodyFat,2)
   # myDict['percentageOfBodyFat'] = percentageOfBodyFat
   # print(myDict.get('percentageOfBodyFat'))

    # percentage of fat for males being calculated
    #malePercentageOfFat=86.010*math.log(waist-neck)-70.041*math.log(height)+36.76
    #print('Since you identified as a male ' + firstName + ', the percentage of fat in your body is ' + malePercentageOfFat + '.')
    #male waist to height ratio
  #  maleWaistToHeight = waist/height
    #print('Your waist to height ratio is ' + maleWaistToHeight)
#elif(gender == 'female'):





 #   hip = float(input('What is the size of your hip in inches?'))
  #  myDict['hip'] = hip
   #JO femalePercentageOfFat = 163.205*math.log(waist+hip-neck)-97.684*math.log(height)-78.387
   # print('Since you identify as a female, the percentage of fat in your body is ' + femalePercentageOfFat)
   # femaleBMI = weight/(height*height)*703
   # print('Your BMI(Body Mass Index) is ' + femaleBMI)
   # femaleWaistToHeight = waist/height
   # print('Your waist to height ratio is ' + femaleWaistToHeight)


#print(myDict)








