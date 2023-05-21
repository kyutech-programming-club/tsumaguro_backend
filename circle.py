# import matplotlib.pyplot as plt
# from matplotlib import patches
import math

# fig, ax = plt.subplots(figsize = (4,4))

# ax.set_xticks([-2,-1,0,1,2])
# ax.set_yticks([-2,-1,0,1,2])


# c = patches.Circle( xy = (0,0), radius= -0.5*math.log(0.9),)

# ax.add_patch(c)

# plt.show()

def point_circle():
    point_circle = [90, 70, 50]
    circle = [-1/2*math.log(i/100) for i in point_circle]
    return circle

print(point_circle())