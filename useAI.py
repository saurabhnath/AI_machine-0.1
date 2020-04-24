
def answerAI(height, width, upper, lower, select):
    x = height
    y = width
    s = y/x
    slope = round(s, 2)
    sel = select
    up = upper
    low = lower
    if slope >= sel:
        return up
    else:
        return low