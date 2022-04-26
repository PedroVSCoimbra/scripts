#!/usr/bin/env python3
# para_python-V3
# Scrit to plot cp at several locations.

# Releases
# V1 - Plot only on location of cp  for on side of the wing and plot mach.
# V2 - Cleaner and ploting all locations (28/07/2021)
# V3 - Plot upper and lower cp (29/07/2021)
# V4 - Make a simple report in pdf, plot until 95% of the chord. (29/07/2021).

# Next
# Should plot Mach number at several locations.
# Remove comments that do not affect the problem
# Make with "for loop"

#### import the simple module from the paraview
from paraview.simple import *
import numpy
from matplotlib import pyplot as plt
import os
import getpass

username = getpass.getuser()

path = "plots/"
path = "data/"
if not os.path.exists("plots/") or not os.path.exists("data/"):
    os.mkdir("data/")
    os.mkdir("plots/")

#  if not os.path.exists("data/"):
#      os.mkdir("data/")

# create a new 'XML Unstructured Grid Reader'
surface_flowvtu = XMLUnstructuredGridReader(registrationName='surface_flow.vtu', FileName=['surface_flow.vtu'])

#  # Properties modified on surface_flowvtu
#  surface_flowvtu.TimeArray = 'None'

#  UpdatePipeline(time=0.0, proxy=surface_flowvtu)


chord = 16*0.0254 # m
span =  32*0.0254 # m

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=surface_flowvtu)

# Properties modified on clip1.ClipType
#  clip1.ClipType.Origin = [chord*0.98, 0.0, 0.0]
clip1.ClipType.Origin = [chord, 0.0, 0.0]
clip1.ClipType.Normal = [1.0, 0.0, 0.0]

#  UpdatePipeline(time=0.0, proxy=clip1)

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
slice1.SliceType.Origin = [0.0, span*0.30, 0.0]
slice2.SliceType.Origin = [0.0, span*0.45, 0.0]
slice3.SliceType.Origin = [0.0, span*0.60, 0.0]
slice4.SliceType.Origin = [0.0, span*0.75, 0.0]
slice5.SliceType.Origin = [0.0, span*0.85, 0.0]
slice6.SliceType.Origin = [0.0, span*0.95, 0.0]

slice1.SliceType.Normal = [0.0, 1.0, 0.0]
slice2.SliceType.Normal = [0.0, 1.0, 0.0]
slice3.SliceType.Normal = [0.0, 1.0, 0.0]
slice4.SliceType.Normal = [0.0, 1.0, 0.0]
slice5.SliceType.Normal = [0.0, 1.0, 0.0]
slice6.SliceType.Normal = [0.0, 1.0, 0.0]

# save data
#  "Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "Points:0",  "Points:1", "Points:2"
SaveData('data/data_eta30.csv', proxy=slice1, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
SaveData('data/data_eta45.csv', proxy=slice2, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
SaveData('data/data_eta60.csv', proxy=slice3, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
SaveData('data/data_eta75.csv', proxy=slice4, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
SaveData('data/data_eta85.csv', proxy=slice5, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
SaveData('data/data_eta95.csv', proxy=slice6, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])

eta = ['30','45','60','75','85','95']

for i in range(0,6):
    data = 'data' + str(i);
    data = numpy.genfromtxt("data/data_eta%s.csv"%eta[i], skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
    #  data = numpy.genfromtxt("data/data_eta30.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "Points:0",  "Points:1", "Points:2"])
    fig, ax = plt.subplots()
    ax.plot(data['x']/chord, -data['Pressure_Coefficient'], 'o',markersize=2, label="Numerical")
    ax.set_title(r'Cp vs x/c at $\eta=%s$'%eta[i])
    ax.set_xlabel("x/c")
    ax.set_ylabel("Cp")
    ax.legend()
    #  plt.figtext(.8, .5, r'Cp vs x/c para $\alpha=0$ $\lambda=0$ $\eta=%s$ Re = 2.500.000 Ma 0.840'%eta[i])
    plt.savefig('plots/cp%s.pdf'%eta[i])

#  data = numpy.genfromtxt("data/data_eta30.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "Points:0",  "Points:1", "Points:2"])
#  fig1, ax1 = plt.subplots()
#  ax1.plot(data['x']/span, -data['Pressure_Coefficient'], 'o')
#  ax1.set_title("Plot Cp vs x/c eta=0.30")
#  ax1.set_xlabel("x/c")
#  ax1.set_ylabel("Cp")
#  plt.savefig('plots/cp30.pdf')
#
#  data = numpy.genfromtxt("data/data_eta45.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "Points:0",  "Points:1", "Points:2"])
#  fig2, ax2 = plt.subplots()
#  ax2.plot(data['x']/span, -data['Pressure_Coefficient'], 'o')
#  ax2.set_title("Plot Cp vs x/c eta=0.45")
#  ax2.set_xlabel("x/c")
#  ax2.set_ylabel("Cp")
#  plt.savefig('plots/cp45.pdf')
#
#  data = numpy.genfromtxt("data/data_eta60.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
#  fig3, ax3 = plt.subplots()
#  ax3.plot(data['x']/span, -data['Pressure_Coefficient'], 'o')
#  ax3.set_title("Plot Cp vs x/c eta=0.60")
#  ax3.set_xlabel("x/c")
#  ax3.set_ylabel("Cp")
#  plt.savefig('plots/cp60.pdf')
#
#  data = numpy.genfromtxt("data/data_eta75.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
#  fig4, ax4 = plt.subplots()
#  ax4.plot(data['x']/span, -data['Pressure_Coefficient'], 'o')
#  ax4.set_title("Plot Cp vs x/c eta=0.75")
#  ax4.set_xlabel("x/c")
#  ax4.set_ylabel("Cp")
#  plt.savefig('plots/cp75.pdf')
#
#  data = numpy.genfromtxt("data/data_eta85.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
#  fig5, ax5 = plt.subplots()
#  ax5.plot(data['x']/span, -data['Pressure_Coefficient'], 'o')
#  ax5.set_title("Plot Cp vs x/c eta=0.85")
#  ax5.set_xlabel("x/c")
#  ax5.set_ylabel("Cp")
#  plt.savefig('plots/cp85.pdf')
#
#  data = numpy.genfromtxt("data/data_eta95.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
#  fig6, ax6 = plt.subplots()
#  ax6.plot(data['x']/span, -data['Pressure_Coefficient'], 'o')
#  ax6.set_title("Plot Cp vs x/c eta=0.95")
#  ax6.set_xlabel("x/c")
#  ax6.set_ylabel("Cp")
#  plt.savefig('plots/cp95.pdf')

if username == "pedro":
    exp = numpy.genfromtxt("/home/pedro/dados/cfd/su2/aepw_sotck/01_experimental_data_all_cases/case3/Case3_ForcedOscMach85/data_cp_mode_60.csv", delimiter=",", names=["x", "cp_mode"])
if username == "pedrovsc2":
    exp = numpy.genfromtxt("/home/pedrovsc2/cfd/meshing/bscw_mesh/data_cp_mode_60.csv", delimiter=",", names=["x", "cp_mode"])

exp = numpy.genfromtxt("/home/pedro/dados/cfd/su2/aepw_sotck/01_experimental_data_all_cases/case3/Case3_ForcedOscMach85/data_cp_mode_60.csv", delimiter=",", names=["x", "cp_mode"])
data2 = numpy.genfromtxt("data/data_eta60.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
fig, ax = plt.subplots()
ax.plot(exp['x'], -exp['cp_mode'], 'or',markersize=3, label="Experimental")
ax.plot(data2['x']/chord, -data2['Pressure_Coefficient'], 'o',markersize=2, label="Numerical")
ax.set_title(r'Cp vs x/c at $\eta=60$')
ax.set_xlabel("x/c")
ax.set_ylabel("Cp")
ax.legend()
#  plt.figtext(.8, .5, r'Cp vs x/c para $\alpha=0$ $\lambda=0$ $\eta=%s$ Re = 2.500.000 Ma 0.840'%eta[i])
plt.savefig('plots/cp_mode_cfd_exp.pdf')

# Make a pdf of With the plots
os.system('pdfunite plots/*.pdf plots/simple_report.pdf')

# Clean
os.system('mv config_CFD.cfg config_SOL.cfg surface_flow.vtu restart_flow.dat flow.vtu history.dat data/')
