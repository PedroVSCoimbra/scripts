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

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=surface_flowvtu)

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.2*0.95, 0.0, 0.0]
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
SaveData('data/data_eta30.csv', proxy=slice1, PointDataArrays=['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Temperature', 'Y_Plus'])
SaveData('data/data_eta45.csv', proxy=slice2, PointDataArrays=['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Temperature', 'Y_Plus'])
SaveData('data/data_eta60.csv', proxy=slice3, PointDataArrays=['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Temperature', 'Y_Plus'])
SaveData('data/data_eta75.csv', proxy=slice4, PointDataArrays=['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Temperature', 'Y_Plus'])
SaveData('data/data_eta85.csv', proxy=slice5, PointDataArrays=['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Temperature', 'Y_Plus'])
SaveData('data/data_eta95.csv', proxy=slice6, PointDataArrays=['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Temperature', 'Y_Plus'])

data = numpy.genfromtxt("data/data_eta30.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
fig1, ax1 = plt.subplots()
ax1.plot(data['x']/0.19, -data['Pressure_Coefficient'], 'o')
ax1.set_title("Plot Cp vs x/c eta=0.30")
ax1.set_xlabel("x/c")
ax1.set_ylabel("Cp")
plt.savefig('plots/cp30.pdf')

data = numpy.genfromtxt("data/data_eta45.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
fig2, ax2 = plt.subplots()
ax2.plot(data['x']/0.19, -data['Pressure_Coefficient'], 'o')
ax2.set_title("Plot Cp vs x/c eta=0.45")
ax2.set_xlabel("x/c")
ax2.set_ylabel("Cp")
plt.savefig('plots/cp45.pdf')

data = numpy.genfromtxt("data/data_eta60.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
fig3, ax3 = plt.subplots()
ax3.plot(data['x']/0.19, -data['Pressure_Coefficient'], 'o')
ax3.set_title("Plot Cp vs x/c eta=0.60")
ax3.set_xlabel("x/c")
ax3.set_ylabel("Cp")
plt.savefig('plots/cp60.pdf')

data = numpy.genfromtxt("data/data_eta75.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
fig4, ax4 = plt.subplots()
ax4.plot(data['x']/0.19, -data['Pressure_Coefficient'], 'o')
ax4.set_title("Plot Cp vs x/c eta=0.75")
ax4.set_xlabel("x/c")
ax4.set_ylabel("Cp")
plt.savefig('plots/cp75.pdf')

data = numpy.genfromtxt("data/data_eta85.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
fig5, ax5 = plt.subplots()
ax5.plot(data['x']/0.19, -data['Pressure_Coefficient'], 'o')
ax5.set_title("Plot Cp vs x/c eta=0.85")
ax5.set_xlabel("x/c")
ax5.set_ylabel("Cp")
plt.savefig('plots/cp85.pdf')

data = numpy.genfromtxt("data/data_eta95.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])
fig6, ax6 = plt.subplots()
ax6.plot(data['x']/0.19, -data['Pressure_Coefficient'], 'o')
ax6.set_title("Plot Cp vs x/c eta=0.95")
ax6.set_xlabel("x/c")
ax6.set_ylabel("Cp")
plt.savefig('plots/cp95.pdf')

# Make a pdf of With the plots
os.system('pdfunite plots/*.pdf plots/simple_report.pdf')

# Clean
os.system('mv config_CFD.cfg config_SOL.cfg surface_flow.vtu restart_flow.dat flow.vtu history.dat data/')

#usar uma entrada pra dizer se plota ou não o mach
#  if sys.argv[0] == yes:
#      continue
#  else:
#     exit script
#  import sys
#  print sys.argv[0] # prints python_script.py

#  # trace generated using paraview version 5.9.1
#
#  #### import the simple module from the paraview
#  from paraview.simple import *
#  #### disable automatic camera reset on 'Show'
#  paraview.simple._DisableFirstRenderCameraReset()
#
#  # create a new 'XML Unstructured Grid Reader'
#  flowvtu = XMLUnstructuredGridReader(registrationName='flow.vtu', FileName=['/home/pedro/dados/cfd/su2/validation/onera_afv/02_RANS/medium/salome/AOA2/flow.vtu'])
#  flowvtu.CellArrayStatus = []
#  flowvtu.PointArrayStatus = ['Density', 'Momentum', 'Energy', 'Nu_Tilde', 'Pressure', 'Temperature', 'Mach', 'Pressure_Coefficient', 'Laminar_Viscosity', 'Skin_Friction_Coefficient', 'Heat_Flux', 'Y_Plus', 'Eddy_Viscosity']
#  flowvtu.TimeArray = 'TimeValue'
#
#  # Properties modified on flowvtu
#  flowvtu.TimeArray = 'None'
#
#  # get active view
#  renderView1 = GetActiveViewOrCreate('RenderView')
#
#  # show data in view
#  flowvtuDisplay = Show(flowvtu, renderView1, 'UnstructuredGridRepresentation')
#
#  # trace defaults for the display properties.
#  flowvtuDisplay.Selection = None
#  flowvtuDisplay.Representation = 'Surface'
#  flowvtuDisplay.ColorArrayName = [None, '']
#  flowvtuDisplay.LookupTable = None
#  flowvtuDisplay.MapScalars = 1
#  flowvtuDisplay.MultiComponentsMapping = 0
#  flowvtuDisplay.InterpolateScalarsBeforeMapping = 1
#  flowvtuDisplay.Opacity = 1.0
#  flowvtuDisplay.PointSize = 2.0
#  flowvtuDisplay.LineWidth = 1.0
#  flowvtuDisplay.RenderLinesAsTubes = 0
#  flowvtuDisplay.RenderPointsAsSpheres = 0
#  flowvtuDisplay.Interpolation = 'Gouraud'
#  flowvtuDisplay.Specular = 0.0
#  flowvtuDisplay.SpecularColor = [1.0, 1.0, 1.0]
#  flowvtuDisplay.SpecularPower = 100.0
#  flowvtuDisplay.Luminosity = 0.0
#  flowvtuDisplay.Ambient = 0.0
#  flowvtuDisplay.Diffuse = 1.0
#  flowvtuDisplay.Roughness = 0.3
#  flowvtuDisplay.Metallic = 0.0
#  flowvtuDisplay.EdgeTint = [1.0, 1.0, 1.0]
#  flowvtuDisplay.SelectTCoordArray = 'None'
#  flowvtuDisplay.SelectNormalArray = 'None'
#  flowvtuDisplay.SelectTangentArray = 'None'
#  flowvtuDisplay.Texture = None
#  flowvtuDisplay.RepeatTextures = 1
#  flowvtuDisplay.InterpolateTextures = 0
#  flowvtuDisplay.SeamlessU = 0
#  flowvtuDisplay.SeamlessV = 0
#  flowvtuDisplay.UseMipmapTextures = 0
#  flowvtuDisplay.BaseColorTexture = None
#  flowvtuDisplay.NormalTexture = None
#  flowvtuDisplay.NormalScale = 1.0
#  flowvtuDisplay.MaterialTexture = None
#  flowvtuDisplay.OcclusionStrength = 1.0
#  flowvtuDisplay.EmissiveTexture = None
#  flowvtuDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
#  flowvtuDisplay.FlipTextures = 0
#  flowvtuDisplay.BackfaceRepresentation = 'Follow Frontface'
#  flowvtuDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
#  flowvtuDisplay.BackfaceOpacity = 1.0
#  flowvtuDisplay.Position = [0.0, 0.0, 0.0]
#  flowvtuDisplay.Scale = [1.0, 1.0, 1.0]
#  flowvtuDisplay.Orientation = [0.0, 0.0, 0.0]
#  flowvtuDisplay.Origin = [0.0, 0.0, 0.0]
#  flowvtuDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
#  flowvtuDisplay.Pickable = 1
#  flowvtuDisplay.Triangulate = 0
#  flowvtuDisplay.UseShaderReplacements = 0
#  flowvtuDisplay.ShaderReplacements = ''
#  flowvtuDisplay.NonlinearSubdivisionLevel = 1
#  flowvtuDisplay.UseDataPartitions = 0
#  flowvtuDisplay.OSPRayUseScaleArray = 'All Approximate'
#  flowvtuDisplay.OSPRayScaleArray = 'Density'
#  flowvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
#  flowvtuDisplay.OSPRayMaterial = 'None'
#  flowvtuDisplay.Orient = 0
#  flowvtuDisplay.OrientationMode = 'Direction'
#  flowvtuDisplay.SelectOrientationVectors = 'Momentum'
#  flowvtuDisplay.Scaling = 0
#  flowvtuDisplay.ScaleMode = 'No Data Scaling Off'
#  flowvtuDisplay.ScaleFactor = 0.8
#  flowvtuDisplay.SelectScaleArray = 'Density'
#  flowvtuDisplay.GlyphType = 'Arrow'
#  flowvtuDisplay.UseGlyphTable = 0
#  flowvtuDisplay.GlyphTableIndexArray = 'Density'
#  flowvtuDisplay.UseCompositeGlyphTable = 0
#  flowvtuDisplay.UseGlyphCullingAndLOD = 0
#  flowvtuDisplay.LODValues = []
#  flowvtuDisplay.ColorByLODIndex = 0
#  flowvtuDisplay.GaussianRadius = 0.04
#  flowvtuDisplay.ShaderPreset = 'Sphere'
#  flowvtuDisplay.CustomTriangleScale = 3
#  flowvtuDisplay.CustomShader = """ // This custom shader code define a gaussian blur
#   // Please take a look into vtkSMPointGaussianRepresentation.cxx
#   // for other custom shader examples
#   //VTK::Color::Impl
#     float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
#     float gaussian = exp(-0.5*dist2);
#     opacity = opacity*gaussian;
#  """
#  flowvtuDisplay.Emissive = 0
#  flowvtuDisplay.ScaleByArray = 0
#  flowvtuDisplay.SetScaleArray = ['POINTS', 'Density']
#  flowvtuDisplay.ScaleArrayComponent = ''
#  flowvtuDisplay.UseScaleFunction = 1
#  flowvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
#  flowvtuDisplay.OpacityByArray = 0
#  flowvtuDisplay.OpacityArray = ['POINTS', 'Density']
#  flowvtuDisplay.OpacityArrayComponent = ''
#  flowvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
#  flowvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
#  flowvtuDisplay.SelectionCellLabelBold = 0
#  flowvtuDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
#  flowvtuDisplay.SelectionCellLabelFontFamily = 'Arial'
#  flowvtuDisplay.SelectionCellLabelFontFile = ''
#  flowvtuDisplay.SelectionCellLabelFontSize = 18
#  flowvtuDisplay.SelectionCellLabelItalic = 0
#  flowvtuDisplay.SelectionCellLabelJustification = 'Left'
#  flowvtuDisplay.SelectionCellLabelOpacity = 1.0
#  flowvtuDisplay.SelectionCellLabelShadow = 0
#  flowvtuDisplay.SelectionPointLabelBold = 0
#  flowvtuDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
#  flowvtuDisplay.SelectionPointLabelFontFamily = 'Arial'
#  flowvtuDisplay.SelectionPointLabelFontFile = ''
#  flowvtuDisplay.SelectionPointLabelFontSize = 18
#  flowvtuDisplay.SelectionPointLabelItalic = 0
#  flowvtuDisplay.SelectionPointLabelJustification = 'Left'
#  flowvtuDisplay.SelectionPointLabelOpacity = 1.0
#  flowvtuDisplay.SelectionPointLabelShadow = 0
#  flowvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
#  flowvtuDisplay.ScalarOpacityFunction = None
#  flowvtuDisplay.ScalarOpacityUnitDistance = 0.12066261076095527
#  flowvtuDisplay.UseSeparateOpacityArray = 0
#  flowvtuDisplay.OpacityArrayName = ['POINTS', 'Density']
#  flowvtuDisplay.OpacityComponent = ''
#  flowvtuDisplay.ExtractedBlockIndex = 0
#  flowvtuDisplay.SelectMapper = 'Projected tetra'
#  flowvtuDisplay.SamplingDimensions = [128, 128, 128]
#  flowvtuDisplay.UseFloatingPointFrameBuffer = 1
#
#  # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
#  flowvtuDisplay.OSPRayScaleFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.84853982925415, 1.0, 0.5, 0.0]
#  flowvtuDisplay.OSPRayScaleFunction.UseLogScale = 0
#
#  # init the 'Arrow' selected for 'GlyphType'
#  flowvtuDisplay.GlyphType.TipResolution = 6
#  flowvtuDisplay.GlyphType.TipRadius = 0.1
#  flowvtuDisplay.GlyphType.TipLength = 0.35
#  flowvtuDisplay.GlyphType.ShaftResolution = 6
#  flowvtuDisplay.GlyphType.ShaftRadius = 0.03
#  flowvtuDisplay.GlyphType.Invert = 0
#
#  # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
#  flowvtuDisplay.ScaleTransferFunction.Points = [0.49876439571380615, 0.0, 0.5, 0.0, 1.2797436714172363, 1.0, 0.5, 0.0]
#  flowvtuDisplay.ScaleTransferFunction.UseLogScale = 0
#
#  # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
#  flowvtuDisplay.OpacityTransferFunction.Points = [0.49876439571380615, 0.0, 0.5, 0.0, 1.2797436714172363, 1.0, 0.5, 0.0]
#  flowvtuDisplay.OpacityTransferFunction.UseLogScale = 0
#
#  # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
#  flowvtuDisplay.DataAxesGrid.XTitle = 'X Axis'
#  flowvtuDisplay.DataAxesGrid.YTitle = 'Y Axis'
#  flowvtuDisplay.DataAxesGrid.ZTitle = 'Z Axis'
#  flowvtuDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
#  flowvtuDisplay.DataAxesGrid.XTitleFontFile = ''
#  flowvtuDisplay.DataAxesGrid.XTitleBold = 0
#  flowvtuDisplay.DataAxesGrid.XTitleItalic = 0
#  flowvtuDisplay.DataAxesGrid.XTitleFontSize = 12
#  flowvtuDisplay.DataAxesGrid.XTitleShadow = 0
#  flowvtuDisplay.DataAxesGrid.XTitleOpacity = 1.0
#  flowvtuDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
#  flowvtuDisplay.DataAxesGrid.YTitleFontFile = ''
#  flowvtuDisplay.DataAxesGrid.YTitleBold = 0
#  flowvtuDisplay.DataAxesGrid.YTitleItalic = 0
#  flowvtuDisplay.DataAxesGrid.YTitleFontSize = 12
#  flowvtuDisplay.DataAxesGrid.YTitleShadow = 0
#  flowvtuDisplay.DataAxesGrid.YTitleOpacity = 1.0
#  flowvtuDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
#  flowvtuDisplay.DataAxesGrid.ZTitleFontFile = ''
#  flowvtuDisplay.DataAxesGrid.ZTitleBold = 0
#  flowvtuDisplay.DataAxesGrid.ZTitleItalic = 0
#  flowvtuDisplay.DataAxesGrid.ZTitleFontSize = 12
#  flowvtuDisplay.DataAxesGrid.ZTitleShadow = 0
#  flowvtuDisplay.DataAxesGrid.ZTitleOpacity = 1.0
#  flowvtuDisplay.DataAxesGrid.FacesToRender = 63
#  flowvtuDisplay.DataAxesGrid.CullBackface = 0
#  flowvtuDisplay.DataAxesGrid.CullFrontface = 1
#  flowvtuDisplay.DataAxesGrid.ShowGrid = 0
#  flowvtuDisplay.DataAxesGrid.ShowEdges = 1
#  flowvtuDisplay.DataAxesGrid.ShowTicks = 1
#  flowvtuDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
#  flowvtuDisplay.DataAxesGrid.AxesToLabel = 63
#  flowvtuDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
#  flowvtuDisplay.DataAxesGrid.XLabelFontFile = ''
#  flowvtuDisplay.DataAxesGrid.XLabelBold = 0
#  flowvtuDisplay.DataAxesGrid.XLabelItalic = 0
#  flowvtuDisplay.DataAxesGrid.XLabelFontSize = 12
#  flowvtuDisplay.DataAxesGrid.XLabelShadow = 0
#  flowvtuDisplay.DataAxesGrid.XLabelOpacity = 1.0
#  flowvtuDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
#  flowvtuDisplay.DataAxesGrid.YLabelFontFile = ''
#  flowvtuDisplay.DataAxesGrid.YLabelBold = 0
#  flowvtuDisplay.DataAxesGrid.YLabelItalic = 0
#  flowvtuDisplay.DataAxesGrid.YLabelFontSize = 12
#  flowvtuDisplay.DataAxesGrid.YLabelShadow = 0
#  flowvtuDisplay.DataAxesGrid.YLabelOpacity = 1.0
#  flowvtuDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
#  flowvtuDisplay.DataAxesGrid.ZLabelFontFile = ''
#  flowvtuDisplay.DataAxesGrid.ZLabelBold = 0
#  flowvtuDisplay.DataAxesGrid.ZLabelItalic = 0
#  flowvtuDisplay.DataAxesGrid.ZLabelFontSize = 12
#  flowvtuDisplay.DataAxesGrid.ZLabelShadow = 0
#  flowvtuDisplay.DataAxesGrid.ZLabelOpacity = 1.0
#  flowvtuDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
#  flowvtuDisplay.DataAxesGrid.XAxisPrecision = 2
#  flowvtuDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
#  flowvtuDisplay.DataAxesGrid.XAxisLabels = []
#  flowvtuDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
#  flowvtuDisplay.DataAxesGrid.YAxisPrecision = 2
#  flowvtuDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
#  flowvtuDisplay.DataAxesGrid.YAxisLabels = []
#  flowvtuDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
#  flowvtuDisplay.DataAxesGrid.ZAxisPrecision = 2
#  flowvtuDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
#  flowvtuDisplay.DataAxesGrid.ZAxisLabels = []
#  flowvtuDisplay.DataAxesGrid.UseCustomBounds = 0
#  flowvtuDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
#
#  # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
#  flowvtuDisplay.PolarAxes.Visibility = 0
#  flowvtuDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
#  flowvtuDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
#  flowvtuDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
#  flowvtuDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
#  flowvtuDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
#  flowvtuDisplay.PolarAxes.EnableCustomRange = 0
#  flowvtuDisplay.PolarAxes.CustomRange = [0.0, 1.0]
#  flowvtuDisplay.PolarAxes.PolarAxisVisibility = 1
#  flowvtuDisplay.PolarAxes.RadialAxesVisibility = 1
#  flowvtuDisplay.PolarAxes.DrawRadialGridlines = 1
#  flowvtuDisplay.PolarAxes.PolarArcsVisibility = 1
#  flowvtuDisplay.PolarAxes.DrawPolarArcsGridlines = 1
#  flowvtuDisplay.PolarAxes.NumberOfRadialAxes = 0
#  flowvtuDisplay.PolarAxes.AutoSubdividePolarAxis = 1
#  flowvtuDisplay.PolarAxes.NumberOfPolarAxis = 0
#  flowvtuDisplay.PolarAxes.MinimumRadius = 0.0
#  flowvtuDisplay.PolarAxes.MinimumAngle = 0.0
#  flowvtuDisplay.PolarAxes.MaximumAngle = 90.0
#  flowvtuDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
#  flowvtuDisplay.PolarAxes.Ratio = 1.0
#  flowvtuDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
#  flowvtuDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
#  flowvtuDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
#  flowvtuDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
#  flowvtuDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
#  flowvtuDisplay.PolarAxes.PolarAxisTitleVisibility = 1
#  flowvtuDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
#  flowvtuDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
#  flowvtuDisplay.PolarAxes.PolarLabelVisibility = 1
#  flowvtuDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
#  flowvtuDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
#  flowvtuDisplay.PolarAxes.RadialLabelVisibility = 1
#  flowvtuDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
#  flowvtuDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
#  flowvtuDisplay.PolarAxes.RadialUnitsVisibility = 1
#  flowvtuDisplay.PolarAxes.ScreenSize = 10.0
#  flowvtuDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
#  flowvtuDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
#  flowvtuDisplay.PolarAxes.PolarAxisTitleFontFile = ''
#  flowvtuDisplay.PolarAxes.PolarAxisTitleBold = 0
#  flowvtuDisplay.PolarAxes.PolarAxisTitleItalic = 0
#  flowvtuDisplay.PolarAxes.PolarAxisTitleShadow = 0
#  flowvtuDisplay.PolarAxes.PolarAxisTitleFontSize = 12
#  flowvtuDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
#  flowvtuDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
#  flowvtuDisplay.PolarAxes.PolarAxisLabelFontFile = ''
#  flowvtuDisplay.PolarAxes.PolarAxisLabelBold = 0
#  flowvtuDisplay.PolarAxes.PolarAxisLabelItalic = 0
#  flowvtuDisplay.PolarAxes.PolarAxisLabelShadow = 0
#  flowvtuDisplay.PolarAxes.PolarAxisLabelFontSize = 12
#  flowvtuDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
#  flowvtuDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
#  flowvtuDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
#  flowvtuDisplay.PolarAxes.LastRadialAxisTextBold = 0
#  flowvtuDisplay.PolarAxes.LastRadialAxisTextItalic = 0
#  flowvtuDisplay.PolarAxes.LastRadialAxisTextShadow = 0
#  flowvtuDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
#  flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
#  flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
#  flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
#  flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
#  flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
#  flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
#  flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
#  flowvtuDisplay.PolarAxes.EnableDistanceLOD = 1
#  flowvtuDisplay.PolarAxes.DistanceLODThreshold = 0.7
#  flowvtuDisplay.PolarAxes.EnableViewAngleLOD = 1
#  flowvtuDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
#  flowvtuDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
#  flowvtuDisplay.PolarAxes.PolarTicksVisibility = 1
#  flowvtuDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
#  flowvtuDisplay.PolarAxes.TickLocation = 'Both'
#  flowvtuDisplay.PolarAxes.AxisTickVisibility = 1
#  flowvtuDisplay.PolarAxes.AxisMinorTickVisibility = 0
#  flowvtuDisplay.PolarAxes.ArcTickVisibility = 1
#  flowvtuDisplay.PolarAxes.ArcMinorTickVisibility = 0
#  flowvtuDisplay.PolarAxes.DeltaAngleMajor = 10.0
#  flowvtuDisplay.PolarAxes.DeltaAngleMinor = 5.0
#  flowvtuDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
#  flowvtuDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
#  flowvtuDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
#  flowvtuDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
#  flowvtuDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
#  flowvtuDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
#  flowvtuDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
#  flowvtuDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
#  flowvtuDisplay.PolarAxes.ArcMajorTickSize = 0.0
#  flowvtuDisplay.PolarAxes.ArcTickRatioSize = 0.3
#  flowvtuDisplay.PolarAxes.ArcMajorTickThickness = 1.0
#  flowvtuDisplay.PolarAxes.ArcTickRatioThickness = 0.5
#  flowvtuDisplay.PolarAxes.Use2DMode = 0
#  flowvtuDisplay.PolarAxes.UseLogAxis = 0
#
#  # reset view to fit data
#  renderView1.ResetCamera()
#
#  # get the material library
#  materialLibrary1 = GetMaterialLibrary()
#
#  # update the view to ensure updated data information
#  renderView1.Update()
#
#  # create a new 'Clip'
#  clip1 = Clip(registrationName='Clip1', Input=flowvtu)
#  clip1.ClipType = 'Plane'
#  clip1.HyperTreeGridClipper = 'Plane'
#  clip1.Scalars = ['POINTS', 'Density']
#  clip1.Value = 0.8892540335655212
#  clip1.Invert = 1
#  clip1.Crinkleclip = 0
#  clip1.Exact = 0
#
#  # init the 'Plane' selected for 'ClipType'
#  clip1.ClipType.Origin = [0.0, 1.9999999999999598, 0.0]
#  clip1.ClipType.Normal = [1.0, 0.0, 0.0]
#  clip1.ClipType.Offset = 0.0
#
#  # init the 'Plane' selected for 'HyperTreeGridClipper'
#  clip1.HyperTreeGridClipper.Origin = [0.0, 1.9999999999999598, 0.0]
#  clip1.HyperTreeGridClipper.Normal = [1.0, 0.0, 0.0]
#  clip1.HyperTreeGridClipper.Offset = 0.0
#
#  # Properties modified on clip1.ClipType
#  clip1.ClipType.Origin = [0.0, 0.32, 0.0]
#  clip1.ClipType.Normal = [0.0, 1.0, 0.0]
#
#  # show data in view
#  clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')
#
#  # trace defaults for the display properties.
#  clip1Display.Selection = None
#  clip1Display.Representation = 'Surface'
#  clip1Display.ColorArrayName = [None, '']
#  clip1Display.LookupTable = None
#  clip1Display.MapScalars = 1
#  clip1Display.MultiComponentsMapping = 0
#  clip1Display.InterpolateScalarsBeforeMapping = 1
#  clip1Display.Opacity = 1.0
#  clip1Display.PointSize = 2.0
#  clip1Display.LineWidth = 1.0
#  clip1Display.RenderLinesAsTubes = 0
#  clip1Display.RenderPointsAsSpheres = 0
#  clip1Display.Interpolation = 'Gouraud'
#  clip1Display.Specular = 0.0
#  clip1Display.SpecularColor = [1.0, 1.0, 1.0]
#  clip1Display.SpecularPower = 100.0
#  clip1Display.Luminosity = 0.0
#  clip1Display.Ambient = 0.0
#  clip1Display.Diffuse = 1.0
#  clip1Display.Roughness = 0.3
#  clip1Display.Metallic = 0.0
#  clip1Display.EdgeTint = [1.0, 1.0, 1.0]
#  clip1Display.SelectTCoordArray = 'None'
#  clip1Display.SelectNormalArray = 'None'
#  clip1Display.SelectTangentArray = 'None'
#  clip1Display.Texture = None
#  clip1Display.RepeatTextures = 1
#  clip1Display.InterpolateTextures = 0
#  clip1Display.SeamlessU = 0
#  clip1Display.SeamlessV = 0
#  clip1Display.UseMipmapTextures = 0
#  clip1Display.BaseColorTexture = None
#  clip1Display.NormalTexture = None
#  clip1Display.NormalScale = 1.0
#  clip1Display.MaterialTexture = None
#  clip1Display.OcclusionStrength = 1.0
#  clip1Display.EmissiveTexture = None
#  clip1Display.EmissiveFactor = [1.0, 1.0, 1.0]
#  clip1Display.FlipTextures = 0
#  clip1Display.BackfaceRepresentation = 'Follow Frontface'
#  clip1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
#  clip1Display.BackfaceOpacity = 1.0
#  clip1Display.Position = [0.0, 0.0, 0.0]
#  clip1Display.Scale = [1.0, 1.0, 1.0]
#  clip1Display.Orientation = [0.0, 0.0, 0.0]
#  clip1Display.Origin = [0.0, 0.0, 0.0]
#  clip1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
#  clip1Display.Pickable = 1
#  clip1Display.Triangulate = 0
#  clip1Display.UseShaderReplacements = 0
#  clip1Display.ShaderReplacements = ''
#  clip1Display.NonlinearSubdivisionLevel = 1
#  clip1Display.UseDataPartitions = 0
#  clip1Display.OSPRayUseScaleArray = 'All Approximate'
#  clip1Display.OSPRayScaleArray = 'Density'
#  clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
#  clip1Display.OSPRayMaterial = 'None'
#  clip1Display.Orient = 0
#  clip1Display.OrientationMode = 'Direction'
#  clip1Display.SelectOrientationVectors = 'Momentum'
#  clip1Display.Scaling = 0
#  clip1Display.ScaleMode = 'No Data Scaling Off'
#  clip1Display.ScaleFactor = 0.8
#  clip1Display.SelectScaleArray = 'Density'
#  clip1Display.GlyphType = 'Arrow'
#  clip1Display.UseGlyphTable = 0
#  clip1Display.GlyphTableIndexArray = 'Density'
#  clip1Display.UseCompositeGlyphTable = 0
#  clip1Display.UseGlyphCullingAndLOD = 0
#  clip1Display.LODValues = []
#  clip1Display.ColorByLODIndex = 0
#  clip1Display.GaussianRadius = 0.04
#  clip1Display.ShaderPreset = 'Sphere'
#  clip1Display.CustomTriangleScale = 3
#  clip1Display.CustomShader = """ // This custom shader code define a gaussian blur
#   // Please take a look into vtkSMPointGaussianRepresentation.cxx
#   // for other custom shader examples
#   //VTK::Color::Impl
#     float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
#     float gaussian = exp(-0.5*dist2);
#     opacity = opacity*gaussian;
#  """
#  clip1Display.Emissive = 0
#  clip1Display.ScaleByArray = 0
#  clip1Display.SetScaleArray = ['POINTS', 'Density']
#  clip1Display.ScaleArrayComponent = ''
#  clip1Display.UseScaleFunction = 1
#  clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
#  clip1Display.OpacityByArray = 0
#  clip1Display.OpacityArray = ['POINTS', 'Density']
#  clip1Display.OpacityArrayComponent = ''
#  clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
#  clip1Display.DataAxesGrid = 'GridAxesRepresentation'
#  clip1Display.SelectionCellLabelBold = 0
#  clip1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
#  clip1Display.SelectionCellLabelFontFamily = 'Arial'
#  clip1Display.SelectionCellLabelFontFile = ''
#  clip1Display.SelectionCellLabelFontSize = 18
#  clip1Display.SelectionCellLabelItalic = 0
#  clip1Display.SelectionCellLabelJustification = 'Left'
#  clip1Display.SelectionCellLabelOpacity = 1.0
#  clip1Display.SelectionCellLabelShadow = 0
#  clip1Display.SelectionPointLabelBold = 0
#  clip1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
#  clip1Display.SelectionPointLabelFontFamily = 'Arial'
#  clip1Display.SelectionPointLabelFontFile = ''
#  clip1Display.SelectionPointLabelFontSize = 18
#  clip1Display.SelectionPointLabelItalic = 0
#  clip1Display.SelectionPointLabelJustification = 'Left'
#  clip1Display.SelectionPointLabelOpacity = 1.0
#  clip1Display.SelectionPointLabelShadow = 0
#  clip1Display.PolarAxes = 'PolarAxesRepresentation'
#  clip1Display.ScalarOpacityFunction = None
#  clip1Display.ScalarOpacityUnitDistance = 0.1548061554008519
#  clip1Display.UseSeparateOpacityArray = 0
#  clip1Display.OpacityArrayName = ['POINTS', 'Density']
#  clip1Display.OpacityComponent = ''
#  clip1Display.ExtractedBlockIndex = 0
#  clip1Display.SelectMapper = 'Projected tetra'
#  clip1Display.SamplingDimensions = [128, 128, 128]
#  clip1Display.UseFloatingPointFrameBuffer = 1
#
#  # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
#  clip1Display.OSPRayScaleFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.84853982925415, 1.0, 0.5, 0.0]
#  clip1Display.OSPRayScaleFunction.UseLogScale = 0
#
#  # init the 'Arrow' selected for 'GlyphType'
#  clip1Display.GlyphType.TipResolution = 6
#  clip1Display.GlyphType.TipRadius = 0.1
#  clip1Display.GlyphType.TipLength = 0.35
#  clip1Display.GlyphType.ShaftResolution = 6
#  clip1Display.GlyphType.ShaftRadius = 0.03
#  clip1Display.GlyphType.Invert = 0
#
#  # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
#  clip1Display.ScaleTransferFunction.Points = [0.5637519359588623, 0.0, 0.5, 0.0, 1.2747952938079834, 1.0, 0.5, 0.0]
#  clip1Display.ScaleTransferFunction.UseLogScale = 0
#
#  # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
#  clip1Display.OpacityTransferFunction.Points = [0.5637519359588623, 0.0, 0.5, 0.0, 1.2747952938079834, 1.0, 0.5, 0.0]
#  clip1Display.OpacityTransferFunction.UseLogScale = 0
#
#  # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
#  clip1Display.DataAxesGrid.XTitle = 'X Axis'
#  clip1Display.DataAxesGrid.YTitle = 'Y Axis'
#  clip1Display.DataAxesGrid.ZTitle = 'Z Axis'
#  clip1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
#  clip1Display.DataAxesGrid.XTitleFontFile = ''
#  clip1Display.DataAxesGrid.XTitleBold = 0
#  clip1Display.DataAxesGrid.XTitleItalic = 0
#  clip1Display.DataAxesGrid.XTitleFontSize = 12
#  clip1Display.DataAxesGrid.XTitleShadow = 0
#  clip1Display.DataAxesGrid.XTitleOpacity = 1.0
#  clip1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
#  clip1Display.DataAxesGrid.YTitleFontFile = ''
#  clip1Display.DataAxesGrid.YTitleBold = 0
#  clip1Display.DataAxesGrid.YTitleItalic = 0
#  clip1Display.DataAxesGrid.YTitleFontSize = 12
#  clip1Display.DataAxesGrid.YTitleShadow = 0
#  clip1Display.DataAxesGrid.YTitleOpacity = 1.0
#  clip1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
#  clip1Display.DataAxesGrid.ZTitleFontFile = ''
#  clip1Display.DataAxesGrid.ZTitleBold = 0
#  clip1Display.DataAxesGrid.ZTitleItalic = 0
#  clip1Display.DataAxesGrid.ZTitleFontSize = 12
#  clip1Display.DataAxesGrid.ZTitleShadow = 0
#  clip1Display.DataAxesGrid.ZTitleOpacity = 1.0
#  clip1Display.DataAxesGrid.FacesToRender = 63
#  clip1Display.DataAxesGrid.CullBackface = 0
#  clip1Display.DataAxesGrid.CullFrontface = 1
#  clip1Display.DataAxesGrid.ShowGrid = 0
#  clip1Display.DataAxesGrid.ShowEdges = 1
#  clip1Display.DataAxesGrid.ShowTicks = 1
#  clip1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
#  clip1Display.DataAxesGrid.AxesToLabel = 63
#  clip1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
#  clip1Display.DataAxesGrid.XLabelFontFile = ''
#  clip1Display.DataAxesGrid.XLabelBold = 0
#  clip1Display.DataAxesGrid.XLabelItalic = 0
#  clip1Display.DataAxesGrid.XLabelFontSize = 12
#  clip1Display.DataAxesGrid.XLabelShadow = 0
#  clip1Display.DataAxesGrid.XLabelOpacity = 1.0
#  clip1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
#  clip1Display.DataAxesGrid.YLabelFontFile = ''
#  clip1Display.DataAxesGrid.YLabelBold = 0
#  clip1Display.DataAxesGrid.YLabelItalic = 0
#  clip1Display.DataAxesGrid.YLabelFontSize = 12
#  clip1Display.DataAxesGrid.YLabelShadow = 0
#  clip1Display.DataAxesGrid.YLabelOpacity = 1.0
#  clip1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
#  clip1Display.DataAxesGrid.ZLabelFontFile = ''
#  clip1Display.DataAxesGrid.ZLabelBold = 0
#  clip1Display.DataAxesGrid.ZLabelItalic = 0
#  clip1Display.DataAxesGrid.ZLabelFontSize = 12
#  clip1Display.DataAxesGrid.ZLabelShadow = 0
#  clip1Display.DataAxesGrid.ZLabelOpacity = 1.0
#  clip1Display.DataAxesGrid.XAxisNotation = 'Mixed'
#  clip1Display.DataAxesGrid.XAxisPrecision = 2
#  clip1Display.DataAxesGrid.XAxisUseCustomLabels = 0
#  clip1Display.DataAxesGrid.XAxisLabels = []
#  clip1Display.DataAxesGrid.YAxisNotation = 'Mixed'
#  clip1Display.DataAxesGrid.YAxisPrecision = 2
#  clip1Display.DataAxesGrid.YAxisUseCustomLabels = 0
#  clip1Display.DataAxesGrid.YAxisLabels = []
#  clip1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
#  clip1Display.DataAxesGrid.ZAxisPrecision = 2
#  clip1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
#  clip1Display.DataAxesGrid.ZAxisLabels = []
#  clip1Display.DataAxesGrid.UseCustomBounds = 0
#  clip1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
#
#  # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
#  clip1Display.PolarAxes.Visibility = 0
#  clip1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
#  clip1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
#  clip1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
#  clip1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
#  clip1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
#  clip1Display.PolarAxes.EnableCustomRange = 0
#  clip1Display.PolarAxes.CustomRange = [0.0, 1.0]
#  clip1Display.PolarAxes.PolarAxisVisibility = 1
#  clip1Display.PolarAxes.RadialAxesVisibility = 1
#  clip1Display.PolarAxes.DrawRadialGridlines = 1
#  clip1Display.PolarAxes.PolarArcsVisibility = 1
#  clip1Display.PolarAxes.DrawPolarArcsGridlines = 1
#  clip1Display.PolarAxes.NumberOfRadialAxes = 0
#  clip1Display.PolarAxes.AutoSubdividePolarAxis = 1
#  clip1Display.PolarAxes.NumberOfPolarAxis = 0
#  clip1Display.PolarAxes.MinimumRadius = 0.0
#  clip1Display.PolarAxes.MinimumAngle = 0.0
#  clip1Display.PolarAxes.MaximumAngle = 90.0
#  clip1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
#  clip1Display.PolarAxes.Ratio = 1.0
#  clip1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
#  clip1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
#  clip1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
#  clip1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
#  clip1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
#  clip1Display.PolarAxes.PolarAxisTitleVisibility = 1
#  clip1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
#  clip1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
#  clip1Display.PolarAxes.PolarLabelVisibility = 1
#  clip1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
#  clip1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
#  clip1Display.PolarAxes.RadialLabelVisibility = 1
#  clip1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
#  clip1Display.PolarAxes.RadialLabelLocation = 'Bottom'
#  clip1Display.PolarAxes.RadialUnitsVisibility = 1
#  clip1Display.PolarAxes.ScreenSize = 10.0
#  clip1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
#  clip1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
#  clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
#  clip1Display.PolarAxes.PolarAxisTitleBold = 0
#  clip1Display.PolarAxes.PolarAxisTitleItalic = 0
#  clip1Display.PolarAxes.PolarAxisTitleShadow = 0
#  clip1Display.PolarAxes.PolarAxisTitleFontSize = 12
#  clip1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
#  clip1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
#  clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
#  clip1Display.PolarAxes.PolarAxisLabelBold = 0
#  clip1Display.PolarAxes.PolarAxisLabelItalic = 0
#  clip1Display.PolarAxes.PolarAxisLabelShadow = 0
#  clip1Display.PolarAxes.PolarAxisLabelFontSize = 12
#  clip1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
#  clip1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
#  clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
#  clip1Display.PolarAxes.LastRadialAxisTextBold = 0
#  clip1Display.PolarAxes.LastRadialAxisTextItalic = 0
#  clip1Display.PolarAxes.LastRadialAxisTextShadow = 0
#  clip1Display.PolarAxes.LastRadialAxisTextFontSize = 12
#  clip1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
#  clip1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
#  clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
#  clip1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
#  clip1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
#  clip1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
#  clip1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
#  clip1Display.PolarAxes.EnableDistanceLOD = 1
#  clip1Display.PolarAxes.DistanceLODThreshold = 0.7
#  clip1Display.PolarAxes.EnableViewAngleLOD = 1
#  clip1Display.PolarAxes.ViewAngleLODThreshold = 0.7
#  clip1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
#  clip1Display.PolarAxes.PolarTicksVisibility = 1
#  clip1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
#  clip1Display.PolarAxes.TickLocation = 'Both'
#  clip1Display.PolarAxes.AxisTickVisibility = 1
#  clip1Display.PolarAxes.AxisMinorTickVisibility = 0
#  clip1Display.PolarAxes.ArcTickVisibility = 1
#  clip1Display.PolarAxes.ArcMinorTickVisibility = 0
#  clip1Display.PolarAxes.DeltaAngleMajor = 10.0
#  clip1Display.PolarAxes.DeltaAngleMinor = 5.0
#  clip1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
#  clip1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
#  clip1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
#  clip1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
#  clip1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
#  clip1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
#  clip1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
#  clip1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
#  clip1Display.PolarAxes.ArcMajorTickSize = 0.0
#  clip1Display.PolarAxes.ArcTickRatioSize = 0.3
#  clip1Display.PolarAxes.ArcMajorTickThickness = 1.0
#  clip1Display.PolarAxes.ArcTickRatioThickness = 0.5
#  clip1Display.PolarAxes.Use2DMode = 0
#  clip1Display.PolarAxes.UseLogAxis = 0
#
#  # hide data in view
#  Hide(flowvtu, renderView1)
#
#  # update the view to ensure updated data information
#  renderView1.Update()
#
#  # set scalar coloring
#  ColorBy(clip1Display, ('POINTS', 'Mach'))
#
#  # rescale color and/or opacity maps used to include current data range
#  clip1Display.RescaleTransferFunctionToDataRange(True, False)
#
#  # show color bar/color legend
#  clip1Display.SetScalarBarVisibility(renderView1, True)
#
#  # get color transfer function/color map for 'Mach'
#  machLUT = GetColorTransferFunction('Mach')
#
#  # get opacity transfer function/opacity map for 'Mach'
#  machPWF = GetOpacityTransferFunction('Mach')
#
#  # set active source
#  SetActiveSource(flowvtu)
#
#  # toggle 3D widget visibility (only when running from the GUI)
#  Hide3DWidgets(proxy=clip1.ClipType)
#
#  # get layout
#  layout1 = GetLayout()
#
#  # layout/tab size in pixels
#  layout1.SetSize(995, 885)
#
#  # current camera placement for renderView1
#  renderView1.CameraPosition = [0.11657403249203291, -0.8478423647304723, 0.015071849763023452]
#  renderView1.CameraFocalPoint = [0.11657403249203291, 1.9999999999999598, 0.015071849763023452]
#  renderView1.CameraViewUp = [0.0, 0.0, 1.0]
#  renderView1.CameraParallelScale = 6.000000000000013
#
#  # save screenshot
#  SaveScreenshot('/home/pedro/dados/cfd/su2/validation/onera_afv/02_RANS/medium/salome/AOA2/plots/mach30.png', renderView1, ImageResolution=[995, 885],
#      FontScaling='Scale fonts proportionally',
#      OverrideColorPalette='',
#      StereoMode='No change',
#      TransparentBackground=0,
#      # PNG options
#      CompressionLevel='5')
