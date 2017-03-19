'''A crack team of love scientists from OkEros (a hot new dating site) have devised
a way to represent dating profiles as rectangles on a two-dimensional plane.
They need help writing an algorithm to find the intersection of two users' love rectangles.
They suspect finding that intersection is the key to a matching algorithm so powerful it
will cause an immediate acquisition by Google or Facebook or Obama or something.

Two rectangles overlapping a little. It must be love.
Write a function to find the rectangular intersection of two given love rectangles.

As with the example above, love rectangles are always "straight" and never "diagonal."
More rigorously: each side is parallel with either the x-axis or the y-axis.'''

rect1 = {

    # coordinates of bottom-left corner
    'left_x': 2,
    'bottom_y': 1,

    # width and height
    'width': 4,
    'height': 3,

}
rect2 = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 3,

    # width and height
    'width': 3,
    'height': 3,

}
rect3 = {

    # coordinates of bottom-left corner
    'left_x': 5,
    'bottom_y': 1,

    # width and height
    'width': 3,
    'height': 2,

}
rect4 = {

    # coordinates of bottom-left corner
    'left_x': 7,
    'bottom_y': 1,

    # width and height
    'width': 1,
    'height': 5,

}


def find_overlap_range(point1, length1, point2, length2):
    highest_start_point = max(point1, point2)
    # print highest_start_point
    lowest_end_point = min(point1+length1, point2 + length2)
    # print lowest_end_point
    if lowest_end_point <= highest_start_point:
        return None

    overlap_length = lowest_end_point - highest_start_point

    return (highest_start_point, overlap_length)


def find_total_overlap(rect1, rect2):
    left_x, width = find_overlap_range(rect1["left_x"], rect1["width"], rect2["left_x"], rect2["width"])

    bottom_y, height = find_overlap_range(rect1["bottom_y"], rect1["height"], rect2["bottom_y"], rect2["height"])

    return {"left_x": left_x,
            "bottom_y": bottom_y,
            "width": width,
            "height": height}

print find_total_overlap(rect1, rect2)

list_of_rect = [rect1, rect2, rect3, rect4]
def find_list_overlap(rect_list):
    result = []
    for position, rectangular in enumerate(rect_list):
        # print position, rectangular
        while position + 1< len(rect_list):
            print "Verifying overlap of 2 rectangulars:"
            print rectangular, position
            print rect_list[position+1], position+1
            result = find_total_overlap(rectangular, rect_list[position+1])
            print "overlap resulting", result
            position +=1
            print "--"*6
    print "==========" * 6
    return result

        # if position+1<len(rect_list):
        #     pass

        # print
        # while position != len(list_of_rect) - 1:
        #     print position, rectangular, rect_list[position +1]
        #     position +=1
        # print find_list_overlap(rectangular, rect_list[position + 1])
        # rect1, rect2
        # rect1, rect3
        # rect1, rect4
        # rect2, rect3
        # rect2, rect4
        # rect3, rect4
find_list_overlap(list_of_rect)