def Trainer(obj1, obj2):
    print('Initialize the value for A (selector slope): (Ex. A = .25 )')
    a = float(input('A = '))
    print('Enter the Learning Rate: L ')
    l = float(input('L = '))
    obj1_height = []
    obj1_width = []
    obj2_height = []
    obj2_width = []
    continue_training = True
    count = 1

    print("************* START TO TRAIN ***************")
    while continue_training:
        while True:
            sample = input(f'choose options:  1.({obj1})    and    2.({obj2}):')
            if sample == '1':
                name = obj1
                break
            elif sample == '2':
                name = obj2
                break
            else:
                print('choose the right option: 1 or 2 :')
                continue
        # start training:
        print(f'----------- training {count} -----------')

        #take input x: as height
        x = float(input(f"{name} Height : "))

        # predict width py = a*x
        py = a*x
        #print(py)
        # actual width , y = ?
        y = float(input(f"{name} Width : "))

        # calculate the error while predicting: e = y - py
        e = y - py
        #print(e)
        #learning from the error y to estimate the error in selector slop:
        del_a = l*e/x
        #print(del_a)
        #update the slope a:
        a = a+del_a
        #print(a)

        if sample == '1':
            obj1_height.append(x)
            obj1_width.append(y)
        elif sample == '2':
            obj2_height.append(x)
            obj2_width.append(y)



        print('-----------------------------------')
        t = input('press y to continue training , else press any other letter):')
        if t == 'y':
            continue_training = True
            count = count+1
        else:
            break

    learned = [a, obj1_height, obj1_width, obj2_height, obj2_width, True]
    return learned






