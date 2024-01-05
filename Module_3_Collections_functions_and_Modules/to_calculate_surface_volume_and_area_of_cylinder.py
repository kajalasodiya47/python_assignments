# pi value
pi = 22/7
# enter height
height = float(input("Enter height : "))
# enter radius
radius = float(input("Enter radius : "))
# formula for calculate the volume
volume = pi * radius * radius * height
# formula for calculate the surface value
surface_area = ((2*pi*radius)*height) + ((pi*radius*radius)*2)
print("Volume is : ",volume)
print("Surface area is : ",surface_area)
