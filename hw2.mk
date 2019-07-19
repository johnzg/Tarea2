all: FFtIm.pdf ImHybrid.pdf ImProceso.pdf XY_met_dt.pdf VxVy_met_dt.pdf Mome_met_dt.pdf Ener_met_dt.pdf

FFtIm.pdf:Fourier.py
	python Fourier.py
    
ImHybrid.pdf:Fourier.py
	python Fourier.py
    
ImProceso.pdf:Fourier.py
	python Fourier.py

XY_met_dt.pdf:Plots_hw2.py
	python Plots_hw2.py

VxVy_met_dt.pdf:Plots_hw2.py
	python Plots_hw2.py

Mome_met_dt.pdf:Plots_hw2.py
	python Plots_hw2.py
    
Ener_met_dt.pdf:Plots_hw2.py
	python Plots_hw2.py

Plots_hw2.py:euler_dt1.dat euler_dt2.dat euler_dt3.dat leapFrog_dt1.dat leapFrog_dt2.dat leapFrog_dt3.dat rungeKutta_dt1.dat rungeKutta_dt2.dat rungeKutta_dt3.dat
	python Plots_hw2.py

euler_dt1.dat:a.out
	./a.out
euler_dt2.dat:a.out
	./a.out
euler_dt3.dat:a.out
	./a.out
leapFrog_dt1.dat:a.out
	./a.out
leapFrog_dt2.dat:a.out
	./a.out
leapFrog_dt3.dat:a.out
	./a.out
rungeKutta_dt1.dat:a.out
	./a.out
rungeKutta_dt2.dat:a.out
	./a.out
rungeKutta_dt3.dat:a.out
	./a.out

a.out:ODEs.cpp:
	g++ ODEs.cpp


