#include <iostream>
#include <fstream>
#include<cmath>
using namespace std;
double M=1.98847*pow(10,30);
double G = 39.478;
double f(double, double, double, double, double);
double *leapFrog2Ord(double, double, double, double, int);

int main()
{
    /*int n =10000;
    double h=(5.0)/(n-1);
    double *l=leapFrog2Ord(0.0,5.0,0.1,0.0,n);
    for(int i=0;i<n;i++)
    {
        cout<<h*i<<" "<<*l<<endl;
        l++;
    }*/
    return 0;
}
double f(double t, double x, double y, double vx, double vy)
{
    double *a=new double[2];
    a[0]=-G*(M/(x*x+y*y))
        
    return -G*(M/(x*x+y*y));
}
double *leapFrog2Ord(double Ti, double Tf, double X0, double V0, int N)
{
    double deltat=(Tf-Ti)/(N-1);
    double Vi=-f(Ti, X0, V0)*deltat*0.5+V0;
    double *x= new double[N];
    double v[N];
    double t[N];
    v[0]=Vi;
    x[0]=X0;
    t[0]=Ti;
    
    for(int i=0;i<N;i++)
    {   
        t[i+1]=t[i]+deltat;
        v[i+1]=f(t[i], x[i], v[i])*deltat +v[i];
        x[i+1]=v[i+1]*deltat + x[i];
       
    }
        
    return x; 
}