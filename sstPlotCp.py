#!/usr/bin/env python3

#### import the simple module from the paraview
from paraview.simple import *
import numpy
from matplotlib import pyplot as plt
import os
import pandas
import getpass


path = "plots/"
path = "data/"
if not os.path.exists("plots/") or not os.path.exists("data/"):
    os.mkdir("data/")
    os.mkdir("plots/")
#  Clean
os.system('mv config_CFD.cfg config_SOL.cfg surface_flow.vtu restart_flow.dat flow.vtu history.dat data/')

#  create a new 'XML Unstructured Grid Reader'
surface_flowvtu = XMLUnstructuredGridReader(registrationName='surface_flow.vtu', FileName=['data/surface_flow.vtu'])

#  # Properties modified on surface_flowvtu
surface_flowvtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=surface_flowvtu)


chord = 16*0.0254 # m
span =  32*0.0254 # m

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=surface_flowvtu)
#  Create a new 'Clip' - Para o intradorso
clip2 = Clip(registrationName='Clip2', Input=surface_flowvtu)

# Properties modified on clip1.ClipType
#  clip1.ClipType.Origin = [chord*0.98, 0.0, 0.0]
clip1.ClipType.Origin = [0.0, 0.0, 0.0]
clip1.ClipType.Normal = [-0.006, 0.0, 1.0]

# Intradorso
clip2.ClipType.Origin = [0.0, 0.0, 0.0]
clip2.ClipType.Normal = [0.006, 0.0, -1.0]

UpdatePipeline(time=0.0, proxy=clip1)

# Definição dos eta para o loop

UpdatePipeline(time=0.0, proxy=clip1)

#  # create a new 'Slice' - Extradorso
#  slice1 = Slice(registrationName='Slice1', Input=clip1)
#  slice2 = Slice(registrationName='Slice2', Input=clip1)
#  slice3 = Slice(registrationName='Slice3', Input=clip1)
#  slice4 = Slice(registrationName='Slice4', Input=clip1)
#  slice5 = Slice(registrationName='Slice5', Input=clip1)
#  slice6 = Slice(registrationName='Slice6', Input=clip1)

#  # create a new 'Slice' - Intradorso
#  slice7 = Slice(registrationName='Slice7', Input=clip2)
#  slice8 = Slice(registrationName='Slice8', Input=clip2)
#  slice9 = Slice(registrationName='Slice9', Input=clip2)
#  slice10 = Slice(registrationName='Slice10', Input=clip2)
#  slice11 = Slice(registrationName='Slice11', Input=clip2)
#  slice12 = Slice(registrationName='Slice12', Input=clip2)

#  # Properties modified on slice1.SliceType - Extradorso
#  slice1.SliceType.Origin = [0.0, span*0.30, 0.0]
#  slice2.SliceType.Origin = [0.0, span*0.45, 0.0]
#  slice3.SliceType.Origin = [0.0, span*0.60, 0.0]
#  slice4.SliceType.Origin = [0.0, span*0.75, 0.0]
#  slice5.SliceType.Origin = [0.0, span*0.85, 0.0]
#  slice6.SliceType.Origin = [0.0, span*0.95, 0.0]
#
#  slice1.SliceType.Normal = [0.0, 1.0, 0.0]
#  slice2.SliceType.Normal = [0.0, 1.0, 0.0]
#  slice3.SliceType.Normal = [0.0, 1.0, 0.0]
#  slice4.SliceType.Normal = [0.0, 1.0, 0.0]
#  slice5.SliceType.Normal = [0.0, 1.0, 0.0]
#  slice6.SliceType.Normal = [0.0, 1.0, 0.0]
#
#  # Properties modified on slice1.SliceType - Extradorso
#  ##Origin
#  slice7.SliceType.Origin = [0.0, span*0.30, 0.0]
#  slice8.SliceType.Origin = [0.0, span*0.45, 0.0]
#  slice9.SliceType.Origin = [0.0, span*0.60, 0.0]
#  slice10.SliceType.Origin = [0.0, span*0.75, 0.0]
#  slice11.SliceType.Origin = [0.0, span*0.85, 0.0]
#  slice12.SliceType.Origin = [0.0, span*0.95, 0.0]
#  ## Normal
#  slice7.SliceType.Normal = [0.0, 1.0, 0.0]
#  slice8.SliceType.Normal = [0.0, 1.0, 0.0]
#  slice9.SliceType.Normal = [0.0, 1.0, 0.0]
#  slice10.SliceType.Normal = [0.0, 1.0, 0.0]
#  slice11.SliceType.Normal = [0.0, 1.0, 0.0]
#  slice12.SliceType.Normal = [0.0, 1.0, 0.0]

#  # save data
#  #  "Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "Points:0",  "Points:1", "Points:2"
# Extradorso
#  for i in range(0,6):
    #  SaveData('data/data_eta%s-Lower.csv'%eta[i], proxy=slice1, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "Points:0",  "Points:1", "Points:2"])
    #  SaveData('data/data_eta%s-Upper.csv'%eta[i], proxy=slice2, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "Points:0",  "Points:1", "Points:2"])

#  SaveData('data/data_eta30-Lower.csv', proxy=slice1, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
#  SaveData('data/data_eta45-Lower.csv', proxy=slice2, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
#  SaveData('data/data_eta60-Lower.csv', proxy=slice3, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
#  SaveData('data/data_eta75-Lower.csv', proxy=slice4, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
#  SaveData('data/data_eta85-Lower.csv', proxy=slice5, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
#  SaveData('data/data_eta95-Lower.csv', proxy=slice6, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
#  # Intradorso
#  SaveData('data/data_eta30-Upper.csv', proxy=slice7, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
#  SaveData('data/data_eta45-Upper.csv', proxy=slice8, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
#  SaveData('data/data_eta60-Upper.csv', proxy=slice9, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
#  SaveData('data/data_eta75-Upper.csv', proxy=slice10, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
#  SaveData('data/data_eta85-Upper.csv', proxy=slice11, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])
#  SaveData('data/data_eta95-Upper.csv', proxy=slice12, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x",  "Points:1", "Points:2"])

#  eta_char =  ["slice0.30", "slice0.45", "slice0.60", "slice0.75", "slice0.85", "slice0.95"]
eta = ['30','45','60','75','85','95']
eta_num =  [0.30, 0.45, 0.60, 0.75, 0.85, 0.95]
for i in range(0,6):
    slice_upper = 'slice_upper' + str(i)
    slice_upper = Slice(registrationName='Slice%s'%eta[i], Input=clip1)
    slice_upper.SliceType.Origin = [0.0, span*eta_num[i], 0.0]
    slice_upper.SliceType.Normal = [0.0, 1.0, 0.0]
    SaveData('data/data_eta%s-Upper.csv'%eta[i], proxy=slice_upper, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "Points:0",  "Points:1", "Points:2"])
    upper = 'upper' + str(i);
    upper = pandas.read_csv("data/data_eta%s-Upper.csv"%eta[i])
    upper.sort_values(["Points:0"], axis=0, ascending=[True], inplace=True)

    slice_lower = 'slice_lower' + str(i)
    slice_lower = Slice(registrationName='Slice%s'%eta[i], Input=clip2)
    slice_lower.SliceType.Origin = [0.0, span*eta_num[i], 0.0]
    slice_lower.SliceType.Normal = [0.0, 1.0, 0.0]
    SaveData('data/data_eta%s-Lower.csv'%eta[i], proxy=slice_lower, PointDataArrays=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Turb_Kin_Energy", "Omega",    "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "Points:0",  "Points:1", "Points:2"])
    lower = 'lower' + str(i);
    lower = pandas.read_csv("data/data_eta%s-Lower.csv"%eta[i])
    lower.sort_values(["Points:0"], axis=0, ascending=[True], inplace=True)

    if i == 2:
        exp_upper = pandas.read_csv("/home/pedro/dados/cfd/su2/aepw_sotck/01_experimental_data_all_cases/case3/Case3_ForcedOscMach85/data_cp_mode_60-upper.csv")
        exp_upper.sort_values(["x"], axis=0, ascending=[True], inplace=True)
        exp_lower = pandas.read_csv("/home/pedro/dados/cfd/su2/aepw_sotck/01_experimental_data_all_cases/case3/Case3_ForcedOscMach85/data_cp_mode_60-lower.csv")
        exp_lower.sort_values(["x"], axis=0, ascending=[True], inplace=True)

        fig, ax = plt.subplots()
        ax.plot(exp_upper['x'], -exp_upper['cp_mode'], 'sg',markersize=3, label="Exp-upper")
        ax.plot(exp_lower['x'], -exp_lower['cp_mode'], 'sr',markersize=3, label="Exp-lower")
        ax.plot(upper['Points:0']/chord, -upper['Pressure_Coefficient'], 'c',markersize=2, label="SU2-Upper")
        ax.plot(lower['Points:0']/chord, -lower['Pressure_Coefficient'], 'm',markersize=2, label="SU2-Lower")
        ax.set_title(r'Cp vs x/c at $\eta=60$')
        ax.set_xlabel("x/c")
        ax.set_ylabel("-Cp")
        ax.legend()
        plt.savefig('plots/cp_mode_cfd_exp.pdf')
    else:
        fig, ax = plt.subplots()
        ax.plot(upper['Points:0']/chord, -upper['Pressure_Coefficient'], 'c',markersize=2, label="SU2-Upper")
        ax.plot(lower['Points:0']/chord, -lower['Pressure_Coefficient'], 'm',markersize=2, label="SU2-Lower")
        ax.set_title(r'Cp vs x/c at $\eta=%s$'%eta[i])
        ax.set_xlabel("x/c")
        ax.set_ylabel("-Cp")
        ax.legend()
        #  plt.figtext(.8, .5, r'Cp vs x/c para $\alpha=0$ $\lambda=0$ $\eta=%s$ Re = 2.500.000 Ma 0.840'%eta[i])
        plt.savefig('plots/cp%s.pdf'%eta[i])

#  username = getpass.getuser()
#  if username == "pedro":
    #  exp_upper = pandas.read_csv("/home/pedro/dados/cfd/su2/aepw_sotck/01_experimental_data_all_cases/case3/Case3_ForcedOscMach85/data_cp_mode_60-upper.csv")
    #  exp_lower = pandas.read_csv("/home/pedro/dados/cfd/su2/aepw_sotck/01_experimental_data_all_cases/case3/Case3_ForcedOscMach85/data_cp_mode_60-lower.csv")
#  if username == "pedrovsc2":
    #  exp = numpy.genfromtxt("/home/pedrovsc2/cfd/meshing/bscw_mesh/data_cp_mode_60.csv", delimiter=",", names=["x", "cp_mode"])


#  Make a pdf of With the plots
os.system('pdfunite plots/*.pdf plots/simple_report.pdf')
