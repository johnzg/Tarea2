#include <iostream>
#include <fstream>
#include<cmath>
#include <math.h> 
using namespace std;
void euler(double, double, double, double, double, double, int);
void leapFrog(double, double, double, double, double, double, int);
void rungeKutta(double, double, double, double, double, double, int);

int main()
{
    double orbitas =20.0;
    double xini=0.1163;
    double vxini=-6.35;
    double yini=0.9772;
    double vyini=0.606;
    double dt1=0.075;
    double dt2=0.01;
    double dt3=0.001;
    
    leapFrog(xini,vxini,yini,vyini,dt1,orbitas,1);
    euler(xini,vxini,yini,vyini,dt1, orbitas,1);
    rungeKutta(xini,vxini,yini,vyini,dt1, orbitas,1);
    
    leapFrog(xini,vxini,yini,vyini,dt2,orbitas,2);
    euler(xini,vxini,yini,vyini,dt2, orbitas,2);
    rungeKutta(xini,vxini,yini,vyini,dt2, orbitas,2);
    
    leapFrog(xini,vxini,yini,vyini,dt3,orbitas,3);
    euler(xini,vxini,yini,vyini,dt3, orbitas,3);
    rungeKutta(xini,vxini,yini,vyini,dt3, orbitas,3);
    
    return 0;
}

void euler(double x0, double xv0, double y0, double yv0, double deltat ,double anios, int numDeltat)
{
    double M=1.0;
    double m=3.00273*pow(10,-6);
    double G = 39.478;
    int n=(anios/deltat)+1;
    double x[n];
    double y[n];
    double xv[n];
    double yv[n];
    double t[n];
    double momento[n];
    double energia[n];
    xv[0]=xv0;
    yv[0]=yv0;
    x[0]=x0;
    y[0]=y0;
    t[0]=0;
    momento[0]=m*(x[0]*yv[0]-y[0]*xv[0]);
    energia[0]=-G*(m*M)/sqrt(x[0]*x[0]+y[0]*y[0])+0.5*m*(xv[0]*xv[0]+yv[0]*yv[0]);
    
    
    
    for(int i=0;i<n-1;i++)
    {   
        t[i+1]=t[i]+deltat;
        xv[i+1]=-G*(M/pow(sqrt(x[i]*x[i]+y[i]*y[i]),3))*deltat*x[i] +xv[i];
        yv[i+1]=-G*(M/pow(sqrt(x[i]*x[i]+y[i]*y[i]),3))*deltat*y[i] +yv[i];
        
        x[i+1]=xv[i]*deltat + x[i];
        y[i+1]=yv[i]*deltat + y[i]; 
        
        momento[i+1]=m*(x[i+1]*yv[i+1]-y[i+1]*xv[i+1]);
        energia[i+1]=-G*(m*M)/sqrt(x[i+1]*x[i+1]+y[i+1]*y[i+1])+0.5*m*(xv[i+1]*xv[i+1]+yv[i+1]*yv[i+1]);
    }
    
    ofstream outfile;
    outfile.open("euler_dt"+std::to_string(numDeltat)+".dat");
    for(int i=0;i<n;i++)
    {
        outfile<<t[i]<<" "<<x[i]<<" "<<y[i]<<" "<<momento[i]<<" "<<energia[i]<<" "<<xv[i]<<" "<<yv[i]<<endl;
    }
    outfile.close();
       
}
void leapFrog(double x0, double xv0, double y0, double yv0, double deltat ,double anios, int numDeltat)
{
    double M=1.0;
    double m=3.00273*pow(10,-6);

    double G = 39.478;
    int n=(anios/deltat)+1;
    double xvi=G*(M/pow(sqrt(x0*x0+y0*y0),3))*deltat*0.5+xv0;
    double yvi=G*(M/pow(sqrt(x0*x0+y0*y0),3))*deltat*0.5+yv0;
    double x[n];
    double y[n];
    double xv[n];
    double yv[n];
    double t[n];
    double momento[n];
    double energia[n];
    xv[0]=xvi;
    yv[0]=yvi;
    x[0]=x0;
    y[0]=y0;
    t[0]=0;
    momento[0]=m*(x[0]*yv[0]-y[0]*xv[0]);
    energia[0]=-G*(m*M)/sqrt(x[0]*x[0]+y[0]*y[0])+0.5*m*(xv[0]*xv[0]+yv[0]*yv[0]);
    
    for(int i=0;i<n-1;i++)
    {   
        t[i+1]=t[i]+deltat;
        xv[i+1]=-G*(M/pow(sqrt(x[i]*x[i]+y[i]*y[i]),3))*deltat*x[i] +xv[i];
        yv[i+1]=-G*(M/pow(sqrt(x[i]*x[i]+y[i]*y[i]),3))*deltat*y[i] +yv[i];
        x[i+1]=xv[i+1]*deltat + x[i];
        y[i+1]=yv[i+1]*deltat + y[i]; 
        
        momento[i+1]=m*(x[i+1]*yv[i+1]-y[i+1]*xv[i+1]);
        energia[i+1]=-G*(m*M)/sqrt(x[i+1]*x[i+1]+y[i+1]*y[i+1])+0.5*m*(xv[i+1]*xv[i+1]+yv[i+1]*yv[i+1]);
    }
    
    ofstream outfile;
    outfile.open("leapFrog_dt"+std::to_string(numDeltat)+".dat");
    for(int i=0;i<n;i++)
    {
        outfile<<t[i]<<" "<<x[i]<<" "<<y[i]<<" "<<momento[i]<<" "<<energia[i]<<" "<<xv[i]<<" "<<yv[i]<<endl;
    }
    outfile.close();
       
}

void rungeKutta(double x0, double xv0, double y0, double yv0, double deltat ,double anios, int numDeltat)
{
    double M=1.0;
    double m=3.00273*pow(10,-6);

    double G = 39.478;
    int n=(anios/deltat)+1;
    double x[n];
    double y[n];
    double xv[n];
    double yv[n];
    double t[n];
    double momento[n];
    double energia[n];
    xv[0]=xv0;
    yv[0]=yv0;
    x[0]=x0;
    y[0]=y0;
    t[0]=0;
    momento[0]=m*(x[0]*yv[0]-y[0]*xv[0]);
    energia[0]=-G*(m*M)/sqrt(x[0]*x[0]+y[0]*y[0])+0.5*m*(xv[0]*xv[0]+yv[0]*yv[0]);
    
    for(int i=0;i<n-1;i++)
    {   
        double xk1=xv[i];
        double yk1=yv[i];
        
        double xvk1=-G*(M/pow(sqrt(x[i]*x[i]+y[i]*y[i]),3))*x[i];
        double yvk1=-G*(M/pow(sqrt(x[i]*x[i]+y[i]*y[i]),3))*y[i];
        
        //double t1=t[i]+deltat*0.5; innecesario para este caso
        //
        
        double x1=x[i]+deltat*0.5*xk1;
        double y1=y[i]+deltat*0.5*yk1;
        
        double xv1=xv[i]+deltat*0.5*xvk1;
        double yv1=yv[i]+deltat*0.5*yvk1;
        
        double xk2=xv1;
        double yk2=yv1;
        
        double xvk2=-G*(M/pow(sqrt(x1*x1+y1*y1),3))*x1;
        double yvk2=-G*(M/pow(sqrt(x1*x1+y1*y1),3))*y1;
        
        //
        // double t2=t[i]+deltat*0.5; innecesario para este caso
        
        double x2=x[i]+deltat*0.5*xk2;
        double y2=y[i]+deltat*0.5*yk2;
        
        double xv2=xv[i]+deltat*0.5*xvk2;
        double yv2=yv[i]+deltat*0.5*yvk2;
        
        double xk3=xv2;
        double yk3=yv2;
        
        double xvk3=-G*(M/pow(sqrt(x2*x2+y2*y2),3))*x2;
        double yvk3=-G*(M/pow(sqrt(x2*x2+y2*y2),3))*y2;
        
        //
        // double t3=t[i]+deltat*0.5; innecesario para este caso
        
        double x3=x[i]+deltat*xk3;
        double y3=y[i]+deltat*yk3;
        
        double xv3=xv[i]+deltat*xvk3;
        double yv3=yv[i]+deltat*yvk3;
        
        double xk4=xv3;
        double yk4=yv3;     
        
        double xvk4=-G*(M/pow(sqrt(x3*x3+y3*y3),3))*x3;
        double yvk4=-G*(M/pow(sqrt(x3*x3+y3*y3),3))*y3;        
        //
        
        double xpendProm=(xk1 + 2.0*xk2 + 2.0*xk3 + xk4)/6.0;
        double ypendProm=(yk1 + 2.0*yk2 + 2.0*yk3 + yk4)/6.0;
        
        double xvpendProm=(xvk1 + 2.0*xvk2 + 2.0*xvk3 + xvk4)/6.0;
        double yvpendProm=(yvk1 + 2.0*yvk2 + 2.0*yvk3 + yvk4)/6.0;
        
        t[i+1]=t[i]+deltat;
        
        x[i+1]=x[i]+deltat*xpendProm;
        y[i+1]=y[i]+deltat*ypendProm;
        
        xv[i+1]=xv[i]+deltat*xvpendProm;
        yv[i+1]=yv[i]+deltat*yvpendProm;
        
        
        
        momento[i+1]=m*(x[i+1]*yv[i+1]-y[i+1]*xv[i+1]);
        energia[i+1]=-G*(m*M)/sqrt(x[i+1]*x[i+1]+y[i+1]*y[i+1])+0.5*m*(xv[i+1]*xv[i+1]+yv[i+1]*yv[i+1]);
    }
    
    ofstream outfile;
    outfile.open("rungeKutta_dt"+std::to_string(numDeltat)+".dat");
    for(int i=0;i<n;i++)
    {
        outfile<<t[i]<<" "<<x[i]<<" "<<y[i]<<" "<<momento[i]<<" "<<energia[i]<<" "<<xv[i]<<" "<<yv[i]<<endl;
    }
    outfile.close();
       
}