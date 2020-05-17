# global var
global selector_slope


# write data in the data file
def write_data(data, sample):
    if sample == '1':
        with open('sample_1_data.txt', mode='a') as text:
            text.write(data)
            text.write('\n')
    elif sample == '2':
        with open('sample_2_data.txt', mode='a') as text:
            text.write(data)
            text.write('\n')


# Read data from data file
def read_data(sample):
    if sample == '1':
        with open('sample_1_data.txt', mode='r') as text:
            content = text.readlines()
            return content
    elif sample == '2':
        with open('sample_2_data.txt', mode='r') as text:
            content = text.readlines()
            return content


def data_present():
    d1 = read_data('1')
    d2 = read_data('2')
    if len(d1) == 0 or len(d2) == 0:
        return False
    else:
        return True

# Delete all trained data :
def clear_data():
    with open('sample_1_data.txt', mode='w') as text:
        text.write('')
    with open('sample_2_data.txt', mode='w') as text:
        text.write('')

def write_name(name1, name2):
    with open('name.txt', mode='w') as text:
        text.write(name1)
        text.write('\n')
        text.write(name2)
        text.write('\n')


def read_name():
    with open('name.txt', mode='r') as text:
        x = text.readlines()
    while '\n' in x:
        x.remove('\n')
    name1 = x[0]
    l1 = len(name1) - 1
    name2 = x[1]
    l2 = len(name2) - 1
    return name1[:l1], name2[:l2]

def update_cache(cache_slope, name1, name2):
    temp = (cache_slope, name1, name2)
    for i in temp:
        with open('cache.txt', mode='a') as text:
            text.write(i)
            text.write('\n')


def clear_cache():
    with open('cache.txt', mode='w') as text:
        text.write('')


def read_cache():
    with open('cache.txt', mode='r') as text:
        content = text.readlines()
        return content


def read_slope():
    data = read_cache()
    while '\n' in data:
        data.remove('\n')
    s = data[0]
    l = len(s) - 1
    k = s[:l]
    slope = float(k)
    return slope

def read_cache_name():
    x = read_cache()
    while '\n' in x:
        x.remove('\n')
    name1 = x[1]
    l1 = len(name1) - 1
    name2 = x[2]
    l2 = len(name2) - 1
    return name1[:l1], name2[:l2]

def convert_string(d):
    j = d
    s1 = ''
    take_s1 = True
    s2 = ''
    take_s2 = False
    for i in j:
        if i in ('(', ')', ' '):
            continue
        elif i in ('.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9') and take_s1:
            s1 = s1 + i
        elif i == ',':
            take_s1 = False
            take_s2 = True
            continue
        elif i in ('.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9') and take_s2:
            s2 = s2 + i
    x = float(s1)
    y = float(s2)

    return x, y


def str_to_float(data):
    while '\n' in data:
        data.remove('\n')
    new_list = []
    for d in data:
        (x, y) = convert_string(d)
        new_list.append((x, y))
    return new_list


def marge_shuffle(list1, list2):
    data = list1 + list2
    from random import shuffle
    shuffle(data)
    return data


# ************************************ main training part ********************************************
def Training():
    previous = input("Want to continue with PREVIOUS TRAINING ? press 'Y' or press 'N' for new training:")
    cache_slope = '001'
    cache_name1 = 'none'
    cache_name2 = 'none'

    confirmation = input("press '1' to update data, or press 'ENTER' to 'train AI' directly: ")
    if previous == 'y' and confirmation == '1':
        if data_present():
            name1, name2 = read_name()
            want_to_update = True
        else:
            print('error: training data not found !')
            return
    elif confirmation == '1':
        clear_data()
        clear_cache()
        print("\n\n ********** NEW TRAINING **********\n\n")
        name1 = input("1st Object name:")
        name2 = input("2nd Object name:")
        write_name(name1, name2)
        update_cache(cache_slope, cache_name1, cache_name2)
        want_to_update = True
    elif previous == 'y':
        if data_present():
            name1, name2 = read_name()
            want_to_update = False
        else:
            print('error: training data not found !')
            return
    else:
        print('error: training data not found !')
        return
    while want_to_update:
        retaking = True
        while retaking:
            sample = input(f'choose----->  *{name1}* (press 1)   or  *{name2}* (press 2) :')
            if sample == '1' or sample == '2':
                retaking = False
                if sample == '1':
                    data = input(f"{name1}(x,y) : ")
                    write_data(data, sample)
                elif sample == '2':
                    data = input(f"{name2}(x,y) : ")
                    write_data(data, sample)
            else:
                continue
        confirmation = input("press 1 to update again :")
        if confirmation == '1':
            want_to_update = True
        else:
            want_to_update = False
            print("...........data are updated. ")
    else:
        pass

    print('\n\nAI is training')
    from graphics import graphics1, graphics2
    graphics2()
    graphics1()
    # read data from sample_1_data.txt and lear
    sample_1_data = str_to_float(read_data('1'))
    sample_2_data = str_to_float(read_data('2'))

    # merge both samples
    all_data = marge_shuffle(sample_1_data, sample_2_data)

    from learn import learn_slope
    slope = read_slope()
    new_slope = learn_slope(all_data, slope)
    cache_slope = str(new_slope)

    from learn import learn_size
    upper_sample, lower_sample = learn_size(sample_1_data, sample_2_data, name1, name2)

    clear_cache()
    update_cache(cache_slope, upper_sample, lower_sample)
