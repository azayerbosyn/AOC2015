
def day2_part1():
    total_s = 0
    for i in open('day2_input.txt'):
        l, w, h = i.split('x')
        l, w, h = int(l), int(w), int(h)
        S = 2*l*w + 2*w*h + 2*h*l
        min_side = min(l*w, w*h, h*l)
        total_s += S + min_side
    return total_s


def day2_part2():
    total_s = 0
    for i in open('day2_input.txt'):
        l, w, h = i.split('x')
        l, w, h = int(l), int(w), int(h)
        ribbon = 2 * min(l+w, w+h, h+l)
        bow = l*w*h
        total_s += bow + ribbon
    return total_s


print(day2_part1())
print(day2_part2())

