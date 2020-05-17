
def take_input():
    x = float(input("Enter x = "))
    y = float(input("Enter y = "))
    return x, y

def execute():
    from train import read_slope
    select_slope = read_slope()
    from train import read_name
    upper, lower = read_name()
    x, y = take_input()
    slope = y / x
    if slope >= select_slope:
        return upper
    elif slope < select_slope:
        return lower
    else:
        return 'unable to answer'


def display(x):
    print(f"It's  {x}")


def run():
    result = execute()
    display(result)
