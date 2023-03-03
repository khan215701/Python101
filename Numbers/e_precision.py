""" Find e to the Nth Digit
Enter a number and have the program generate e up to that many decimal places. 
Keep a limit to how far the program will go.
Create by : khan safiq
"""

import math

precision_range = 50
pi_process = True
print("Reminder: Enter 0 to 50 only. Press q anytime to exit.")
precision = input("enter decimal precision: ")

while pi_process:
    try:
        value = int(precision)
    except ValueError:
        if precision == 'q' or precision == 'Q':
            print('Thank You for your. I hope you will see again later')
            break
        
        
    if value > 50 or value <= 0:
        print('Thank You for your time but precision value is not in the range from 0 to {0}'.format(precision_range))
        print("Reminder: Enter 0 to 50 only. Press q anytime to exit.")
        precision = input("enter decimal precision: ")
        pi_process = True
    else:
        print("result={pi:<70.{precision}f}".format(pi=math.e,precision=precision))
        print("Thank you for your. I hape you got your result.")
        print("you want to find more precision values so press y or Y for continue and press n or N for no more")
        precision = input("enter your decision: ")
        
        if precision == 'y' or precision == 'Y':
            precision = input("enter decimal precision: ")
            pi_process = True
        if precision == 'n' or precision == 'N':
            print('Thank You for your. I hope you will see again later')
            break
            
