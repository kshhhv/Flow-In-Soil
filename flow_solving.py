import flow_fun as ff
import numpy as np

L = 30 #length of column
n = 30 #number of steps
dz = L/n #spatial step size

#spatial list
z = np.linspace(dz/2, L-dz/2, n)

t_final = 12*60*60 #time duration
dt = 1 #timestep

# time list
times = np.arange(0,t_final,dt)

#list to store dT/dt
qs = np.empty(n)

Thetas = np.linspace(0.2,0.2,n)

Thetaba = 0.4
Thetabb = Thetas[-1]

T = np.linspace(20,20,n) #initial temperature of column
Ta = np.linspace(20,20,n) #initial temperature of column

Tb1 = 40 #surface boundary condition
Tb2 = 20 #last column boundary condition

#list to store dT/dt
dTdt = np.empty(n)
dTadt = np.empty(n)

TPlot = [T]
TaPlot = [Ta]
ThetaPlot = [Thetas]

print(Thetas)

for j in times:
	if j%3600 ==0:	print(round(j/3600,1), 'hrs done')

	for i in range(1,n-1):

		avgKa = (ff.calK(Thetas[i])+ff.calK(Thetas[i-1]))/2
		psiHa = ff.calPsi(Thetas[i-1])+(i-1)*dz - ff.calPsi(Thetas[i]) - i*dz
		firstq = avgKa*psiHa/dz
		
		avgKb = ((ff.calK(Thetas[i])+ff.calK(Thetas[i+1]))/2)
		psiHb = ff.calPsi(Thetas[i+1])+(i+1)*dz - ff.calPsi(Thetas[i]) - i*dz
		secondq = avgKb*psiHb/dz

		qs[i] = firstq + secondq


		avgCa = (ff.alpha(Thetas[i])+ff.alpha(Thetas[i-1]))/2
		grdTa = T[i-1]-T[i]
		firstt = avgCa*grdTa/dz
 
		avgCb = (ff.alpha(Thetas[i])+ff.alpha(Thetas[i+1]))/2
		grdTb = T[i+1]-T[i]
		secondt = avgCb*grdTb/dz

		dTdt[i] = firstt + secondt

		dTadt[i] = ff.alpha(0.2)*(T[i-1]+T[i+1]-2*T[i])/dz


	avgKa = ((ff.calK(Thetas[0])+ff.calK(Thetaba))/2)
	psiHa = ff.calPsi(Thetaba)+(-1)*dz - ff.calPsi(Thetas[0])
	firstq = avgKa*psiHa/dz
	
	avgKb = ((ff.calK(Thetas[0])+ff.calK(Thetas[1]))/2)
	psiHb = ff.calPsi(Thetas[1])+(1)*dz - ff.calPsi(Thetas[0])
	secondq = avgKb*psiHb/dz

	qs[0] = firstq + secondq

	avgCa = (ff.alpha(Thetas[0])+ff.alpha(Thetaba))/2
	grdTa = Tb1-T[0]
	firstt = avgCa*grdTa/dz

	avgCb = (ff.alpha(Thetas[0])+ff.alpha(Thetas[1]))/2
	grdTb = T[1]-T[0]
	secondt = avgCb*grdTb/dz

	dTdt[0] = firstt + secondt

	dTadt[0] = ff.alpha(0.2)*(Tb1+T[1]-2*T[0])/dz


	Thetas = Thetas + qs*dt

	#update the temperature profile
	T = T + dTdt*dt
	Ta = Ta +dTadt*dt

	# print(dTadt[0],Ta[0])


	ThetaPlot.append(Thetas)
	TPlot.append(T)
	TaPlot.append(Ta)

np.savez('simulation_data', z = z, ThetaPlot = ThetaPlot, TPlot = TPlot, TaPlot = TaPlot)
# np.save('Thetas', ThetaPlot,z)
# np.save('Temp_flow', TPlot)
# np.save('Temp_wf', TaPlot)

