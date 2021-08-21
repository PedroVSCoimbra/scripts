# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
import numpy
from matplotlib import pyplot as plt
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
surface_flowvtu = XMLUnstructuredGridReader(registrationName='surface_flow.vtu', FileName=['surface_flow.vtu'])

# Properties modified on surface_flowvtu
surface_flowvtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=surface_flowvtu)

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=surface_flowvtu)

# Properties modified on clip1.ClipType
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

UpdatePipeline(time=0.0, proxy=clip1)

# Definição dos eta para o loop
eta =  [0.30, 0.45, 0.60, 0.75, 0.85, 0.95]
eta_char =  ["slice0.30", "slice0.45", "slice0.60", "slice0.75", "slice0.85", "slice0.95"]


#  UpdatePipeline(time=0.0, proxy=clip1)

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=clip1)
slice2 = Slice(registrationName='Slice2', Input=clip1)
slice3 = Slice(registrationName='Slice3', Input=clip1)
slice4 = Slice(registrationName='Slice4', Input=clip1)
slice5 = Slice(registrationName='Slice5', Input=clip1)
slice6 = Slice(registrationName='Slice6', Input=clip1)

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.8*0.30, 0.0]
slice2.SliceType.Origin = [0.0, 0.8*0.45, 0.0]
slice3.SliceType.Origin = [0.0, 0.8*0.60, 0.0]
slice4.SliceType.Origin = [0.0, 0.8*0.75, 0.0]
slice5.SliceType.Origin = [0.0, 0.8*0.85, 0.0]
slice6.SliceType.Origin = [0.0, 0.8*0.95, 0.0]

slice1.SliceType.Normal = [0.0, 1.0, 0.0]
slice2.SliceType.Normal = [0.0, 1.0, 0.0]
slice3.SliceType.Normal = [0.0, 1.0, 0.0]
slice4.SliceType.Normal = [0.0, 1.0, 0.0]
slice5.SliceType.Normal = [0.0, 1.0, 0.0]
slice6.SliceType.Normal = [0.0, 1.0, 0.0]

# save data
SaveData('data_eta30.csv', proxy=slice1, PointDataArrays=['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Temperature', 'Y_Plus'])
SaveData('data_eta45.csv', proxy=slice2, PointDataArrays=['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Temperature', 'Y_Plus'])
SaveData('data_eta60.csv', proxy=slice3, PointDataArrays=['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Temperature', 'Y_Plus'])
SaveData('data_eta75.csv', proxy=slice4, PointDataArrays=['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Temperature', 'Y_Plus'])
SaveData('data_eta85.csv', proxy=slice5, PointDataArrays=['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Temperature', 'Y_Plus'])
SaveData('data_eta95.csv', proxy=slice6, PointDataArrays=['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Temperature', 'Y_Plus'])

data = numpy.genfromtxt("data_eta30.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
fig1, ax1 = plt.subplots()
ax1.plot(data['x']/0.2, -data['Pressure_Coefficient'], 'o')
ax1.set_title("Plot Cp vs x/c eta=0.30")
ax1.set_xlabel("x/c")
ax1.set_ylabel("Cp")
plt.savefig('cp30.png')

data = numpy.genfromtxt("data_eta45.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
fig2, ax2 = plt.subplots()
ax2.plot(data['x']/0.2, -data['Pressure_Coefficient'], 'o')
ax2.set_title("Plot Cp vs x/c eta=0.45")
ax2.set_xlabel("x/c")
ax2.set_ylabel("Cp")
plt.savefig('cp45.png')

data = numpy.genfromtxt("data_eta60.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
fig3, ax3 = plt.subplots()
ax3.plot(data['x']/0.2, -data['Pressure_Coefficient'], 'o')
ax3.set_title("Plot Cp vs x/c eta=0.60")
ax3.set_xlabel("x/c")
ax3.set_ylabel("Cp")
plt.savefig('cp60.png')

data = numpy.genfromtxt("data_eta75.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
fig4, ax4 = plt.subplots()
ax4.plot(data['x']/0.2, -data['Pressure_Coefficient'], 'o')
ax4.set_title("Plot Cp vs x/c eta=0.75")
ax4.set_xlabel("x/c")
ax4.set_ylabel("Cp")
plt.savefig('cp75.png')

data = numpy.genfromtxt("data_eta85.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
fig5, ax5 = plt.subplots()
ax5.plot(data['x']/0.2, -data['Pressure_Coefficient'], 'o')
ax5.set_title("Plot Cp vs x/c eta=0.85")
ax5.set_xlabel("x/c")
ax5.set_ylabel("Cp")
plt.savefig('cp85.png')

data = numpy.genfromtxt("data_eta95.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
fig6, ax6 = plt.subplots()
ax6.plot(data['x']/0.2, -data['Pressure_Coefficient'], 'o')
ax6.set_title("Plot Cp vs x/c eta=0.95")
ax6.set_xlabel("x/c")
ax6.set_ylabel("Cp")
plt.savefig('cp95.png')
