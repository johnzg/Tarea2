#include <iostream>
#include <fstream>
#include<cmath>
using namespace std;
double M=1.98847*pow(10,30);
double G = 39.478;
double f(double, double, double, double, double);
void leapFrog(double, double, double, double, double, double);

int main()
{
    double anios =20;
    double xini=0.1163;
    double vxini=-6.35;
    double yini=0.9772;
    double vyini=0.606;
    leapFrog(xini,vxini,yini,vyini,0.1,anios);
    return 0;
}
double f(double t, double x, double y, double vx, double vy)
{       
    return -G*(M/(x*x+y*y));
}
void leapFrog(double x0, double xv0, double y0, double yv0, double deltat ,double anios)
{
    int n=(anios/deltat)+1;
    double xvi=-f(0, x0, y0, xv0, yv0)*deltat*0.5+xv0;
    double yvi=-f(0, x0, y0, xv0, yv0)*deltat*0.5+xv0;
    double x[n];
    double y[n];
    double xv[n];
    double yv[n];
    double t[n];
    xv[0]=xvi;
    yv[0]=yvi;
    x[0]=x0;
    y[0]=y0;
    t[0]=0;
    
    for(int i=0;i<n;i++)
    {   
        t[i+1]=t[i]+deltat;
        xv[i+1]=f(t[i], x[i], xv[i], y[i], yv[i])*deltat +xv[i];
        yv[i+1]=f(t[i], x[i], xv[i], y[i], yv[i])*deltat +yv[i];
        x[i+1]=xv[i+1]*deltat + x[i];
        y[i+1]=yv[i+1]*deltat + y[i];       
    }
    
    ofstream outfile;
    outfile.open("leapFrog_"+std::to_string(deltat)+".dat");
    for(int i=0;i<n;i++)
    {
        outfile<<t[i]<<" "<<x[i]<<" "<<y[i]<<endl;
    }
    outfile.close();
       
}