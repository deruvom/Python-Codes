import math
class Point(object):
    """ Represents a point in 2D space"""
    


def distance_between_points(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    distance = math.sqrt(dx**2+dy**2)
    return distance

def main():
    blank = Point() # object is an instance of the class Point

    print blank # prints the class the object it belongs and where it is stored in memory
    
    blank.x = 3.0  #assigning attributes - go to the object blank refers to (Point) and get the value of x.
    blank.y = 4.0
    
    grosse = Point()
    grosse.x = 5.0 
    grosse.y = 3.0

    dist = distance_between_points(grosse,blank)
    print dist
    
if __name__ == '__main__':
    main()