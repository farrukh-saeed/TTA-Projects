marks = input("What are your grades in exams : ")
if marks >= '90':
    print(" You got A* grade")
elif marks >= '80':
    print("You got A grade ")
elif marks >= '70':
    print("You got B grade")
elif marks >= '60':
    print(" you got C grade")
else:
    print("Unfortunately! you have failed the exam, Have another go")
    print()
    print(' Calculate your Exam results ')
    print()

resultPython = input('Enter your Python score : ')
resultHTML = input ('Enter your HTML score : ')
TotalResult =  int(resultPython) + int(resultHTML)
print('Your final result is : ', TotalResult)