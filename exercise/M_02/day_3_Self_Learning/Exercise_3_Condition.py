mark_exam = int(input('Input yout mark: '))

if mark_exam >= 90:
    print('Your grade is A')
elif mark_exam >= 80 and mark_exam < 90:
    print('Your grade is B')
elif mark_exam >= 70 and mark_exam < 80:
    print('Your grade is C')
elif mark_exam >= 60 and mark_exam < 70:
    print('Your greade is D')
else:
    print('Your grade is F')
