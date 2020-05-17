from train import Training
from run import run
from graphics import graphics1

graphics1()
while True:
    ip = input("\n\n#################################\nHey enter: \n---> 't' for 'training' \n---> 'r' for 'RUN_AI' "
               "\n---> 'q' for 'quit' "
               "\n choose:")
    if ip == 't':
        Training()
        print('\n\n.......TRAINING IS FINISHED.........\n\n')
    elif ip == 'r':
        run()
    elif ip == 'q':
        quit()
    else:
        continue
