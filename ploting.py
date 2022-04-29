import matplotlib.pyplot as plt
import numpy as np

data = np.load('simulation_data.npz')
z = data['z']
ThetaPlot = data['ThetaPlot']
TPlot = data['TPlot']
TaPlot = data['TaPlot']

for j in range(len(TPlot)):
	if j%600 == 0:

		plt.clf()

		plt.subplot(1,2,1)
		scatter = plt.scatter(TPlot[j],z,s=8,label='with water flow')
		scatter = plt.scatter(TaPlot[j],z,s=8,label='constant water content')
		ax = scatter.axes
		ax.invert_yaxis()
		plt.ylabel('Distance (in cm)')
		plt.xlabel('Temperature (in C)')
		plt.legend(loc=4)

		plt.subplot(1,2,2)
		scatter = plt.scatter(ThetaPlot[j],z,s=8)
		ax = scatter.axes
		ax.invert_yaxis()
		plt.xlim(0.1,0.5)
		#plt.ylabel('Distance (in cm)')
		plt.xlabel('Water content')

		plt.suptitle('Time '+ str(round(j/3600,0)) + ' hours')

		plt.pause(0.1)

	else:
		continue

plt.show()