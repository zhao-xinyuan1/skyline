#sky_left = [(0,2.5,2.5),(2.5,5,5),(5,2.5,8),(8,3.75,10),(10,2,12)]
#sky_right = [(1.25,3.5,6),(6,1.25,9),(9,3,11)]

def merge_skyline(sky_left,sky_right):
    sky_left.append((sky_left[-1][2],0))
    sky_right.append((sky_right[-1][2],0))
    current_left, current_right = 0, 0
    previous_left, previous_right = -1, -1
    left_end, right_end = 0, 0
    sky_total = []
    while True:
        if not left_end and not right_end:
            if sky_left[current_left][0] < sky_right[current_right][0]:
                if previous_right >= 0:
                    Right = sky_left[current_left][0]
                    sky_total.append((Left,Height,Right))
                    Left = sky_left[current_left][0]
                    Height = sky_left[current_left][1] if sky_left[current_left][1] > sky_right[previous_right][1] else sky_right[previous_right][1]
                elif previous_left >= 0:
                    Right = sky_left[current_left][0]
                    sky_total.append((Left,Height,Right))
                    Left = sky_left[current_left][0]
                    Height = sky_left[current_left][1]
                else:
                    Left = sky_left[current_left][0]
                    Height = sky_left[current_left][1]
                previous_left = current_left
                current_left = current_left + 1
            else:
                if previous_left >= 0:
                    Right = sky_right[current_right][0]
                    sky_total.append((Left,Height,Right))
                    Left = sky_right[current_right][0]
                    Height = sky_right[current_right][1] if sky_right[current_right][1] > sky_left[previous_left][1] else sky_left[previous_left][1]
                elif previous_right >= 0:
                    Right = sky_left[current_right][0]
                    sky_total.append((Left,Height,Right))
                    Left = sky_left[current_right][0]
                    Height = sky_left[current_right][1]
                else:
                    Left = sky_right[current_right][0]
                    Height = sky_right[current_right][1]
                previous_right = current_right
                current_right = current_right + 1
        elif left_end and not right_end:
            Right = sky_right[current_right][0]
            sky_total.append((Left,Height,Right))
            Left = sky_right[current_right][0]
            Height = sky_right[current_right][1]
            previous_right = current_right
            current_right = current_right + 1
        elif right_end and not left_end:
            Right = sky_left[current_left][0]
            sky_total.append((Left,Height,Right))
            Left = sky_left[current_left][0]
            Height = sky_left[current_left][1]
            previous_left = current_left
            current_left = current_left + 1
        else:
            break
        if (current_right == len(sky_right)):
            right_end = 1
        if (current_left == len(sky_left)):
            left_end = 1
    sky_total_res = []
    sky_total_res.append(sky_total.pop())
    while(sky_total):
        sky_line = sky_total.pop()
        if sky_line[1] == sky_total_res[-1][1]:
            Right = sky_total_res[-1][2]
            sky_total_res.pop()
            sky_total_res.append((sky_line[0], sky_line[1], Right))
        else:
            sky_total_res.append(sky_line)
    sky_total_res.reverse()
    return sky_total_res

#sky_total = merge_skyline(sky_left,sky_right)

def skyline(buildings):
    if (len(buildings) > 1):
        sky_left = skyline(buildings[:len(buildings)//2])
        sky_right =  skyline(buildings[len(buildings)//2:])
        sky_total = merge_skyline(sky_left,sky_right)
        return sky_total
    else:
        return buildings

buildings = [(1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16), (14, 3, 25),
         (19, 18, 22), (23, 13, 29), (24, 4, 28)]
print(skyline(buildings))