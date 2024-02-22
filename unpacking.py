# a = 10
# b = 10
# c = 10

#multivariable assignment
# a = b = c = 10
# print(a, b, c)

# lilita, Dhara, Quinlan = "Chocolate", "Lime", "Vanilla"

# print(lilita, Dhara, Quinlan)

# movies = ["Remember the Titans", "Juno", "Lucy"]

# caleb, gemma, yolanda = movies

# print(gemma)


# t1, t2, t3 = [100, 200,300,400] #fails with exception

#t1, t2, t3, _ = [100, 200,300,400] # skips the last element
# t1, _ , t2, t3 = [100, 200,300,400] # skips the 200 element
# print(t1, t2, t3)

# # * -> unpacking operator
# t1, t2, *t3 = [100, 200, 300, 400, 60, 40, 30] #all emaining values are in t3 in list form
# print(t1, t2, t3)

# t1, t2, *t3 = (100, 200, 300, 400, 60, 40, 30) #all emaining values are in t3 in list form
# print(t1, t2, t3)

#==========================================================================================
#Origin (0,0) how far the distance is 
#task 3
cordinate = [(5,4), (1,1), (6,10), (9,10)]

dist_center = [round((x**2 + y**2)**(0.5),3) for x,y in cordinate]
print(dist_center)
#==========================================================================================
#task 1
dist =[]
for cords in cordinate:
  dist.append(round((cords[0]**2 + cords[1]**2)**(0.5),3))

print(dist)
#=========================================================================================
#task 2
dist =[]
for x,y in cordinate:
  dist.append(round((x**2 + y**2)**(0.5),3))

print(dist)

#=========================================================================================
t1, t2,*_,t3 = (100, 200, 300, 400, 60, 40, 30)
print(t1,t2,t3)

