class area():
    def circle(self,rad):
        print("The area of the given circle is : ",(3.14)*rad*rad)
        Measure()
    def square(self,side):
        print("The area of the given square is :",(side*side))
        Measure()
    def rectangle(self,length,width):
        print("The area of the given rectangle is :",length*width)
        Measure()
    def cube(self,side):
        print("The Total surface area of the given cube is :",4*side*side)
        Measure()
    def cuboid(self,length,width,height):
        print("The Total surface area of the given cuboid is :",2*((length*width)+(width*height)+(height*length)))
        Measure()
    def cone(self,rad,height):
        print("The Total surface area of the given cone is :",(3.1415*rad)*(height+rad))
        Measure()
    def cylinder(self,rad,height):
        print("The Total surface area of the given cylinder is :",(2*3.1415*rad)*(rad+height))
        Measure()
    def sphere(self,rad):
        print("The Total surface area of the given sphere is :",(4*3.1415*rad*rad))
        Measure()



class volume():
    def cuboid(self,length,width,height):
        print("The volume of cuboid is :",length*width*height)
        Measure()
    def cube(self,side):
        print("The volume of the given cube is :",side*side*side)
        Measure()
    def cylinder(self,rad,height):
        print("The volume of the given cylinder is :",3.1415*rad*rad*height)
        Measure()
    def cone(self,rad,height):
        print("The volume of the given cone is :",(3.1415*rad*rad*height)/3)
        Measure()
    def sphere(self,rad):
        print("The volume of the given sphere is :",(3.1415*rad*rad*rad*4)/3)
        Measure()




class perimeter():
    def circle(self,rad):
        print("The perimeter of the given circle is :",2*3.1415*rad)
        Measure()
    def square(self,side):
        print("The perimeter of the given shape is :",4*side)
        Measure()
    def rectangle(self,length,width):
        print("The perimeter of the given shape is :",2*(length+width))
        Measure()
    def triangle(self,base,side1,side2):
        print("The perimeter of the given triangle is :",base+side1+side2)
        Measure()

def Measure():
    print("1)Perimeter\n2)Area\n3)Volume\n4)Exit")
    user=int(input("Choose option from the given list :"))
    if (user==1):
        shape=int(input("select one shape to measure perimeter:\n0)Exit\n1.Circle\n2.Square\n3.rectangle\n4.Parallelogram\n5.Rhombus"))
        if (shape==0):
            print("Thank you")

        elif (shape==1):
            rad=int(input("Enter radius : "))
            per=perimeter()
            per.circle(rad)
        elif(shape==2) or (shape==5):
            side=int(input("Enter length of edge :"))
            per=perimeter()
            per.square(side)
        elif(shape==3) or (shape==4):
            length,width=map(int,input("Enter length and width with space separating them :").split(" "))
            per=perimeter()
            per.rectangle(length,width)
        else:
            print("choose from the given list")
    elif(user==2):
            shape=int(input("select one shape to measure perimeter:\n0)Exit\n1.Circle\n2.Square\n3.rectangle\n4.cube\n5.cuboid\n6.cylinder\n7.cone\n8.sphere\n"))
            if shape == 0:
                print("Thank you!!")

            if (shape==1):
                rad = int(input("Enter radius : "))
                Area=area()
                Area.circle(rad)
            elif (shape==2):
                side = int(input("Enter length of edge :"))
                Area=area()
                Area.square(side)
            elif(shape==3):
                length,width=map(int,input("Enter length and width:").split(" "))
                Area=area()
                Area.rectangle(length,width)
            elif (shape==4):
                side=int(input("Enter the length of the edge"))
                Area=area()
                area.cube(side)
            elif(shape==5):
                length, width ,height= map(int,input().split(" "))
                Area=area()
                Area.cuboid(length,width,height)
            elif(shape==6):
                rad,height=map(int,input("Enter radius and height of the cylinder :").split(" "))
                Area=area()
                Area.cylinder(rad,height)
            elif (shape==7):
                rad, height = map(int, input("Enter radius and height of the cylinder :").split(" "))
                Area=area()
                Area.cone(rad,height)
            elif (shape==8):
                rad=int(input("Enter the radius of sphere :"))
                Area=area()
                Area.sphere(rad)
            else:
                print("choose from the given list")
    elif (user==3):
        shape=int(input("select one shape to measure perimeter:\n0)Exit\n1.Cuboid\n2.Cube\n3.Cylinder\n4.Cone\n5.Sphere"))
        if shape==0:
            print("Thank You!!")
        elif shape==1:
            length, width, height = map(int, input("Enter length,width,height of the cuboid :").split(" "))
            v=volume()
            v.cuboid(length, width, height)
        elif(shape==2):
            side=int(input("Enter the length of the edge :"))
            v=volume()
            v.cube(side)
        elif(shape==3):
            rad, height = map(int, input("Enter radius and height of the cylinder :").split(" "))
            v=volume()
            v.cylinder(rad,height)
        elif(shape==4):
            rad, height = map(int, input("Enter radius and height of the cone :").split(" "))
            v=volume()
            v.cone(rad,height)
        elif(shape==5):
            rad=int(input("Enter the radius : "))
            v=volume()
            v.sphere(rad)
        else:
            print("choose from the given list")

    elif (user==4):
        print("Thank You!!")


Measure()