time = (3,30)
# http://stackoverflow.com/questions/20601427/how-do-i-calculate-the-angle-between-the-hour-and-minutes-hands
def degree_between_handles(hr, mins):
    # in case we have time over 12 hours
    # if hr > 12:
    #     hr -= 12

    #hour handle will also move a little bit in case minute handle is not on a 00 position
    #for example, if the min handle is 30 mins. hour handle will move to half an hour
    # why 30/60*mins? Because 30 degrees is each our, since 360/12 = 30. Deviation per minute would be:
    # 30/60 = 0.5 degrees per minute
    hour_degree = hr*360/12 + mins*30/60
    mins_degree = mins*360/60
    result = abs((hour_degree) - (mins_degree))

    return min(360-result, result)
# print degree_between_handles(15, 30)
# print degree_between_handles(0, 0)
# print degree_between_handles(10, 30)

def clockangles(hour, minute):
    # 3:30
    # 3*30 +30*0.5 - 30*6
    # 90+15-180 = -75
    ans = abs((hour * 360/12 + minute * 0.5) - (minute * 6))
    return min(360-ans,ans)

print degree_between_handles(3, 30)
print clockangles(3,30)