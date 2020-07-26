print('Since you are either overweight or obese, some fitness plans are given. You can follow them, or modify them to suit your needs.')

whyThisWay = "Below you will see how the workouts are structured. Each workout has a day full of intense exercises, and another where it much lighter. \n This is done to allow muscles grow, instead of overwork and rip."



fitnessPlanOne = 'Day 1:\n 3 sets of 12 squats(increase by 1 each week until reach 15) \n 10 crunches(increase by 1 each week until reach 15) \n 12 Russian twists(increase by 1 until reach 15) \n 5 sets of 10 pushups \n Note: Between each set, have a break no more than 30 seconds. \n Note: Perform each exercise as perfect as possible. \n Look at ways to perform these exercises perfectly, and if you do it wrong, repeat it, or else you may injure yourself, and note develop the required muscles. \n Day 2: \n 30-45 minute jog(or complete 2.5-3 miles run)'

fitnessPlanTwo = 'Fitness plan 2 is a H.I.I.T(High Intensity Interal Training) workout, which is for people who want to exercise in a short time It is like a sprint of exercises done. \n Day 1: \n 3 sets of burpees with mountain climbers \n lay down on back, bring legs up 20 times(you should feel your abdomen hurt), do this for 3 sets \n Day 2: \n sprint 1.5 miles in 15 minutes or less \n 50 jumping jacks'

fitnessPlanThree = 'This an exercise to remember, I call it the 20-20 Workout! \n Day 1: \n 20 burpees \n 20 jumping jacks \n 20 squats \n 20 push-ups \n 1 minute plank \n 20 crunches \n Day 2: \n 20 minute light jog'

stretches = 'Do these stretches after any workout, and do all these stretches for 15 seconds each. \n Stretches: \n hamstring stretch \n quadricep stretch \n groin stretch \n low-back stretch \n tricep stretch \n Hip-flexor stretch \n glute stretch \n calve stretch \n chest stretch \n arm & shoulder stretch'

ready = input('Are you reading to get started? Say yes.')

if(ready == 'yes'):
    pass
else:
    while(ready != 'yes'):
        ready = input('Are you ready to get started? Say yes: ')

print(fitnessPlanOne)


readyTwo = input('Are you reading to get started? Say yes.')

if(readyTwo == 'yes'):
    pass
else:
    while(readyTwo != 'yes'):
        readyTwo = input('Are you ready to get started? Say yes: ')

print(fitnessPlanTwo)


readyThree = input('Are you ready to get started? Say yes: ')
if(readyThree == 'yes'):
    pass
else:
    while(readyThree != 'yes'):
        readyThree = input('Are you ready to get started? Say yes: ')

print(fitnessPlanThree)

readyFour = input('Are you ready to continue? Say yes: ')
if(readyFour == 'yes'):
    pass
else:
    while(readyFour != 'yes'):
        readyFour = input('Are you ready to get started? Say yes: ')

print('Thank you for trying the app. You can follow the workout plans I gave, or modify it to your liking. \n Just keep in mind that you need a balance of cardio and muscle exercises. \n Use the calorie intake calculator given(keeep in mind it may not be 100% accurate) to portion your calories per meal. \n As the general audience of this app are kids/teens, it is not highly recommended to reduce the foot you eat, \n as you need it for growing different parts of your body. \n Many doctors would recommend exercising a lot, and eating the same. \n As long as you maintain your weight, or lose weight slowly(do not do crash diets), you are good to go. ')
print('To stay motivated to meet your fitness goals, below is a listed fitness generator. ')

