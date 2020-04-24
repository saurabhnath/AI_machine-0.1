
def size(h1, w1, h2, w2, obj1, obj2):
    sum1 = sum(h1)
    l1 = len(h1)
    x1 = sum1/l1

    sum2 = sum(w1)
    l2 = len(w1)
    y1 = sum2/l2

    slp1 = y1/x1
    slope_obj1 = round(slp1)

    sum3 = sum(h2)
    l3 = len(h2)
    x2 = sum3/l3

    sum4 = sum(w2)
    l4 = len(h2)
    y2 = sum4/l4

    slp2 = y2/y1
    slope_obj2 = round(slp2)

    if slope_obj1 > slope_obj2:
        big = obj1
        small = obj2
    else:
        big = obj2
        small = obj1


    size_list = [big, small]
    return size_list