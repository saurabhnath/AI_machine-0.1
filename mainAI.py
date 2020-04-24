#Aim_Of_The_Project:  To identification between two objects when the height and the width are given:

#obj1 = 'Rose_leaf'
#obj2 = 'Neem_leaf'
from typing import Any, Union


print("Enter the object1:")
obj1 = input()
print("enter the object2:")
obj2 = input()



#train the machine :
trained = False
if not trained:
    from TrainAI import Trainer
    learned = Trainer(obj1, obj2)
    trained = learned[-1]
    print("\n\n\nTraining is finished.  (remember the more you train, the machine will be more intelligent)\n\n\n")

select = round(learned[0], 2)

obj1_height = learned[1]
obj1_width = learned[2]
obj2_height = learned[3]
obj2_width = learned[4]

from Size import size
s = size(obj1_height, obj1_width, obj2_height, obj2_width, obj1, obj2)
print(s)
upper = s[0]
lower = s[1]


print("****** NOW YOUR ARTIFICIAL INTELLIGENCE  IS READY FOR PREDICT THE OBJECT *******")
# run AI for work:
run = True
while run:
    print('**********************************************************\n')
    print('Enter the Object Height and Width: (in cm up to 2 decimal:)')
    height = float(input('Height = '))
    width = float(input('Width = '))
    from useAI import answerAI

    answer = answerAI(height, width, upper, lower, select)
    print(f"\nIt's ** {answer} ** , right ?.\n")

    again = input("Do you want me to predict another one ? press 'Y' if yes, else press 'N' for exit : ")
    if again == 'y':
        run = True
    else:
        run = False


print('$$$$____AI is Terminated____$$$$')


