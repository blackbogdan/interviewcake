# https://codility.com
# https://codility.com/c/feedback/Z5ZAQ6-8CZ
# https://www.codewars.com/?language=python
# http://paulbourke.net/geometry/circlesphere/
__author__ = 'bkapusta'
from math import sqrt
from time import sleep
A = [(0, 5, 4), (0, 0, -3), (-2, 1, -6), (1, -2, 2), (1, 1, 1), (4, -4, 3)]
def is_point_in_sphere(sphere, point):
    # print "Verifying point {} is located in sphere {}".format(point, sphere)
    # print sphere, point
    distance_squared = ((sphere[0]-point[0])**2+(sphere[1]-point[1])**2+(sphere[2]-point[2])**2)
    sphere_radius_sqared = (sphere[0]**2+sphere[1]**2+sphere[2]**2)
    print "squared distance: {}, current radius_squared: {}. Point in sphere: {}".format(distance_squared, sphere_radius_sqared, distance_squared<=sphere_radius_sqared)
    return distance_squared<sphere_radius_sqared

def solution():

    list_of_radiuses = []
    print len(A)
    for i, item in enumerate(A):
        l = [None]*len(A)
        print "===" * 15
        print " " * 10, "Verifyting sphere number: {}".format(i)
        for point_number, point in enumerate(A[i:]):
            r = is_point_in_sphere(item, point)
            l[point_number] = r
        print l
def solution2(A):
    sq_radiuses = []
    for i in A:
        r = i[0]**2 + i[1]**2 + i[2]**2
        sq_radiuses.append(r)

    # https://math.stackexchange.com/questions/198764/how-to-know-if-a-point-is-inside-a-circle
    # x1, y1, R = sphere. Point = (x2, y2). How to find out if point in sphere?

    # distance = sqrt((x1-x2)**2 + (y1-y2)**2)
    # now distance should be less than radius of the sphere: distance<R ==>yes, we have the point in the circle

    sq_radiuses.sort(reverse=True)
    return set(sq_radiuses)
print solution2(A)




# task number 2
A = [10, 0, 8, 2, -1, 12, 11, 3]
def funk():
    # solution
    # http://fushan.blog.51cto.com/9723472/1673078
    sleep(1)
    A.sort()
    lenght = len(A)
    ans = None
    if lenght == 2:
        return (A[1]-A[0])/2
    for i, value in enumerate(A):

        print "=="*16, i
        if i+1 == lenght:
            break

        print "A[i] {}".format(A[i])
        print "A[i+1] {}".format(A[i+1])
        if (A[i+1]-A[i]>1):
            print "verifying the result"
            ans = max(ans, A[i+1]-A[i])
    print "asdf", range(len(A))
    return ans /2
# print funk()