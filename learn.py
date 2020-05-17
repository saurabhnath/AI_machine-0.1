


def learn_slope(training_data, a):
    l = 0.5
    for (x, y) in training_data:
        # predict width py = a*x
        py = a * x
        # calculate the error while predicting: e = y - py
        e = y - py
        # print(e)
        # learning from the error y to estimate the error in selector slop:
        del_a = l * e / x
        # print(del_a)
        # update the slope a:
        a = a + del_a
    return a

def learn_size(sample1, sample2, obj1, obj2):

    h1 = []
    w1 = []
    h2 = []
    w2 = []
    for (x, y) in sample1:
        h1.append(x)
        w1.append(y)
    for (x, y) in sample2:
        h2.append(x)
        w2.append(y)

    sum1 = sum(h1)
    l1 = len(h1)
    x1 = sum1 / l1

    sum2 = sum(w1)
    l2 = len(w1)
    y1 = sum2 / l2

    slp1 = y1 / x1

    sum3 = sum(h2)
    l3 = len(h2)
    x2 = sum3 / l3

    sum4 = sum(w2)
    l4 = len(h2)
    y2 = sum4 / l4

    slp2 = y2 / x2

    if slp1 > slp2:
        big = obj1
        small = obj2
    else:
        big = obj2
        small = obj1

    return big, small