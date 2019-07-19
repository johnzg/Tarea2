import numpy as np
import matplotlib.pylab as plt

#Graficando el momento

plt.figure(figsize=(14,14))

data=np.genfromtxt("euler_dt1.dat")
t=data[:,0]
m=data[:,3]
plt.subplot(3,3,1)
plt.plot(t,m,color="blue")
plt.title("Euler dt = 0.75 yr")
plt.ylabel("momento(Mso*AU*AU/anio)")

data=np.genfromtxt("euler_dt2.dat")
t=data[:,0]
m=data[:,3]
plt.subplot(3,3,2)
plt.plot(t,m,color="blue")
plt.title("Euler dt = 0.01 yr")

data=np.genfromtxt("euler_dt3.dat")
t=data[:,0]
m=data[:,3]
plt.subplot(3,3,3)
plt.plot(t,m,color="blue")
plt.title("Euler dt = 0.001 yr")


data=np.genfromtxt("leapFrog_dt1.dat")
t=data[:,0]
m=data[:,3]
plt.subplot(3,3,4)
plt.plot(t,m,color="red")
plt.title("Leap Frog dt = 0.75 yr")
plt.ylabel("momento(Mso*AU*AU/anio)")

data=np.genfromtxt("leapFrog_dt2.dat")
t=data[:,0]
m=data[:,3]
plt.subplot(3,3,5)
plt.plot(t,m,color="red")
plt.title("Leap Frog dt = 0.01 yr")

data=np.genfromtxt("leapFrog_dt3.dat")
t=data[:,0]
m=data[:,3]
plt.subplot(3,3,6)
plt.plot(t,m,color="red")
plt.title("Leap Frog dt = 0.001 yr")


data=np.genfromtxt("rungeKutta_dt1.dat")
t=data[:,0]
m=data[:,3]
plt.subplot(3,3,7)
plt.plot(t,m,color="green")
plt.title("Runge Kutta dt = 0.75 yr")
plt.xlabel("t(anios)")
plt.ylabel("momento(Mso*AU*AU/anio)")

data=np.genfromtxt("rungeKutta_dt2.dat")
t=data[:,0]
m=data[:,3]
plt.subplot(3,3,8)
plt.plot(t,m,color="green")
plt.title("Runge Kutta dt = 0.01 yr")
plt.xlabel("t(anios)")


data=np.genfromtxt("rungeKutta_dt3.dat")
t=data[:,0]
m=data[:,3]
plt.subplot(3,3,9)
plt.plot(t,m,color="green")
plt.title("Runge Kutta dt = 0.001 yr")
plt.xlabel("t(anios)")


plt.savefig("Mome_met_dt.png")

#Graficando orbitas:

plt.figure(figsize=(14,14))

data=np.genfromtxt("euler_dt1.dat")
x=data[:,1]
y=data[:,2]
plt.subplot(3,3,1)
plt.plot(x,y,color="blue")
plt.title("Euler dt = 0.75 yr")
plt.ylabel("y(AU)")

data=np.genfromtxt("euler_dt2.dat")
x=data[:,1]
y=data[:,2]
plt.subplot(3,3,2)
plt.plot(x,y,color="blue")
plt.title("Euler dt = 0.01 yr")


data=np.genfromtxt("euler_dt3.dat")
x=data[:,1]
y=data[:,2]
plt.subplot(3,3,3)
plt.plot(x,y,color="blue")
plt.title("Euler dt = 0.001 yr")


data=np.genfromtxt("leapFrog_dt1.dat")
x=data[:,1]
y=data[:,2]
plt.subplot(3,3,4)
plt.plot(x,y,color="red")
plt.title("Leap Frog dt = 0.75 yr")
plt.ylabel("y(AU)")

data=np.genfromtxt("leapFrog_dt2.dat")
x=data[:,1]
y=data[:,2]
plt.subplot(3,3,5)
plt.plot(x,y,color="red")
plt.title("Leap Frog dt = 0.01 yr")

data=np.genfromtxt("leapFrog_dt3.dat")
x=data[:,1]
y=data[:,2]
plt.subplot(3,3,6)
plt.plot(x,y,color="red")
plt.title("Leap Frog dt = 0.001 yr")

data=np.genfromtxt("rungeKutta_dt1.dat")
x=data[:,1]
y=data[:,2]
plt.subplot(3,3,7)
plt.plot(x,y,color="green")
plt.title("Runge Kutta dt = 0.75 yr")
plt.xlabel("x(AU)")
plt.ylabel("y(AU)")

data=np.genfromtxt("rungeKutta_dt2.dat")
x=data[:,1]
y=data[:,2]
plt.subplot(3,3,8)
plt.plot(x,y,color="green")
plt.title("Runge Kutta dt = 0.01 yr")
plt.xlabel("x(AU)")


data=np.genfromtxt("rungeKutta_dt3.dat")
x=data[:,1]
y=data[:,2]
plt.subplot(3,3,9)
plt.plot(x,y,color="green")
plt.title("Runge Kutta dt = 0.001 yr")
plt.xlabel("x(AU)")


plt.savefig("XY_met_dt.png")

#Graficando velocidades 

plt.figure(figsize=(14,14))

data=np.genfromtxt("euler_dt1.dat")
xv=data[:,5]
yv=data[:,6]
plt.subplot(3,3,1)
plt.plot(xv,yv,color="blue")
plt.title("Euler dt = 0.75 yr")
plt.ylabel("vy(AU/anio)")

data=np.genfromtxt("euler_dt2.dat")
xv=data[:,5]
yv=data[:,6]
plt.subplot(3,3,2)
plt.plot(xv,yv,color="blue")
plt.title("Euler dt = 0.01 yr")


data=np.genfromtxt("euler_dt3.dat")
xv=data[:,5]
yv=data[:,6]
plt.subplot(3,3,3)
plt.plot(xv,yv,color="blue")
plt.title("Euler dt = 0.001 yr")


data=np.genfromtxt("leapFrog_dt1.dat")
xv=data[:,5]
yv=data[:,6]
plt.subplot(3,3,4)
plt.plot(xv,yv,color="red")
plt.title("Leap Frog dt = 0.75 yr")
plt.ylabel("vy(AU/anio)")

data=np.genfromtxt("leapFrog_dt2.dat")
xv=data[:,5]
yv=data[:,6]
plt.subplot(3,3,5)
plt.plot(xv,yv,color="red")
plt.title("Leap Frog dt = 0.01 yr")

data=np.genfromtxt("leapFrog_dt3.dat")
xv=data[:,5]
yv=data[:,6]
plt.subplot(3,3,6)
plt.plot(xv,yv,color="red")
plt.title("Leap Frog dt = 0.001 yr")

data=np.genfromtxt("rungeKutta_dt1.dat")
xv=data[:,5]
yv=data[:,6]
plt.subplot(3,3,7)
plt.plot(xv,yv,color="green")
plt.title("Runge Kutta dt = 0.75 yr")
plt.xlabel("vx(AU/anio)")
plt.ylabel("vy(AU/anio)")

data=np.genfromtxt("rungeKutta_dt2.dat")
xv=data[:,5]
yv=data[:,6]
plt.subplot(3,3,8)
plt.plot(xv,yv,color="green")
plt.title("Runge Kutta dt = 0.01 yr")
plt.xlabel("vx(AU/anio)")


data=np.genfromtxt("rungeKutta_dt3.dat")
xv=data[:,5]
yv=data[:,6]
plt.subplot(3,3,9)
plt.plot(xv,yv,color="green")
plt.title("Runge Kutta dt = 0.001 yr")
plt.xlabel("vx(AU/anio)")


plt.savefig("VxVy_met_dt.png")

#Graficando energia

plt.figure(figsize=(17,17))

data=np.genfromtxt("euler_dt1.dat")
t=data[:,0]
u=data[:,4]
plt.subplot(3,3,1)
plt.plot(t,u,color="blue")
plt.title("Euler dt = 0.75 yr")
plt.ylabel("energia(Msol*AU*AU/(anio*anio))")

data=np.genfromtxt("euler_dt2.dat")
t=data[:,0]
u=data[:,4]
plt.subplot(3,3,2)
plt.plot(t,u,color="blue")
plt.title("Euler dt = 0.01 yr")


data=np.genfromtxt("euler_dt3.dat")
t=data[:,0]
u=data[:,4]
plt.subplot(3,3,3)
plt.plot(t,u,color="blue")
plt.title("Euler dt = 0.001 yr")


data=np.genfromtxt("leapFrog_dt1.dat")
t=data[:,0]
u=data[:,4]
plt.subplot(3,3,4)
plt.plot(t,u,color="red")
plt.title("Leap Frog dt = 0.75 yr")
plt.ylabel("energia(Msol*AU*AU/(anio*anio))")

data=np.genfromtxt("leapFrog_dt2.dat")
t=data[:,0]
u=data[:,4]
plt.subplot(3,3,5)
plt.plot(t,u,color="red")
plt.title("Leap Frog dt = 0.01 yr")

data=np.genfromtxt("leapFrog_dt3.dat")
t=data[:,0]
u=data[:,4]
plt.subplot(3,3,6)
plt.plot(t,u,color="red")
plt.title("Leap Frog dt = 0.001 yr")

data=np.genfromtxt("rungeKutta_dt1.dat")
t=data[:,0]
u=data[:,4]
plt.subplot(3,3,7)
plt.plot(t,u,color="green")
plt.title("Runge Kutta dt = 0.75 yr")
plt.xlabel("t(anio)")
plt.ylabel("energia(Msol*AU*AU/(anio*anio))")

data=np.genfromtxt("rungeKutta_dt2.dat")
t=data[:,0]
u=data[:,4]
plt.subplot(3,3,8)
plt.plot(t,u,color="green")
plt.title("Runge Kutta dt = 0.01 yr")
plt.xlabel("t(anio)")


data=np.genfromtxt("rungeKutta_dt3.dat")
t=data[:,0]
u=data[:,4]
plt.subplot(3,3,9)
plt.plot(t,u,color="green")
plt.title("Runge Kutta dt = 0.001 yr")
plt.xlabel("t(anio)")


plt.savefig("Ener_met_dt.png")