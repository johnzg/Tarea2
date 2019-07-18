import numpy as np
import matplotlib.pylab as plt

data=np.genfromtxt("euler_dt1.dat")
x=data[:,1]
y=data[:,2]
plt.figure()
plt.plot(x,y,color="black")
plt.title("Euler dt = 0.1 yr")
plt.xlabel("x(AU)")
plt.ylabel("y(AU)")
plt.savefig("Euler_0.1.png")

data=np.genfromtxt("leapFrog_dt1.dat")
x=data[:,1]
y=data[:,2]
plt.figure()
plt.plot(x,y,color="red")
plt.title("Leap Frog dt = 0.1 yr")
plt.xlabel("x(AU)")
plt.ylabel("y(AU)")
plt.savefig("leapFrog_0.1.png")

