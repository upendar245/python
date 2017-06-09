#!/python3/bin/python3
def rectangle_123( length, breadth):
    area=length*breadth
    print(area)
    permiter=2*(length+breadth)
    print(permiter)
    return(area)
    
print("enter length")
l=int(input())
print("enter breadth")
b=int(input())
rectangle_123(l,b)
