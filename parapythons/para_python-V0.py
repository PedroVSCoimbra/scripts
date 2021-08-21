 #!/usr/bin/env pvbatch
# trace generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
import numpy
from matplotlib import pyplot as plt
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
flowvtu = XMLUnstructuredGridReader(registrationName='flow.vtu', FileName=['flow.vtu'])
flowvtu.CellArrayStatus = []
flowvtu.PointArrayStatus = ['Density', 'Momentum', 'Energy', 'Nu_Tilde', 'Pressure', 'Temperature', 'Mach', 'Pressure_Coefficient', 'Laminar_Viscosity', 'Skin_Friction_Coefficient', 'Heat_Flux', 'Y_Plus', 'Eddy_Viscosity']
flowvtu.TimeArray = 'TimeValue'

# Properties modified on flowvtu
flowvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
flowvtuDisplay = Show(flowvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
flowvtuDisplay.Selection = None
flowvtuDisplay.Representation = 'Surface'
flowvtuDisplay.ColorArrayName = [None, '']
flowvtuDisplay.LookupTable = None
flowvtuDisplay.MapScalars = 1
flowvtuDisplay.MultiComponentsMapping = 0
flowvtuDisplay.InterpolateScalarsBeforeMapping = 1
flowvtuDisplay.Opacity = 1.0
flowvtuDisplay.PointSize = 2.0
flowvtuDisplay.LineWidth = 1.0
flowvtuDisplay.RenderLinesAsTubes = 0
flowvtuDisplay.RenderPointsAsSpheres = 0
flowvtuDisplay.Interpolation = 'Gouraud'
flowvtuDisplay.Specular = 0.0
flowvtuDisplay.SpecularColor = [1.0, 1.0, 1.0]
flowvtuDisplay.SpecularPower = 100.0
flowvtuDisplay.Luminosity = 0.0
flowvtuDisplay.Ambient = 0.0
flowvtuDisplay.Diffuse = 1.0
flowvtuDisplay.Roughness = 0.3
flowvtuDisplay.Metallic = 0.0
flowvtuDisplay.EdgeTint = [1.0, 1.0, 1.0]
flowvtuDisplay.SelectTCoordArray = 'None'
flowvtuDisplay.SelectNormalArray = 'None'
flowvtuDisplay.SelectTangentArray = 'None'
flowvtuDisplay.Texture = None
flowvtuDisplay.RepeatTextures = 1
flowvtuDisplay.InterpolateTextures = 0
flowvtuDisplay.SeamlessU = 0
flowvtuDisplay.SeamlessV = 0
flowvtuDisplay.UseMipmapTextures = 0
flowvtuDisplay.BaseColorTexture = None
flowvtuDisplay.NormalTexture = None
flowvtuDisplay.NormalScale = 1.0
flowvtuDisplay.MaterialTexture = None
flowvtuDisplay.OcclusionStrength = 1.0
flowvtuDisplay.EmissiveTexture = None
flowvtuDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
flowvtuDisplay.FlipTextures = 0
flowvtuDisplay.BackfaceRepresentation = 'Follow Frontface'
flowvtuDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
flowvtuDisplay.BackfaceOpacity = 1.0
flowvtuDisplay.Position = [0.0, 0.0, 0.0]
flowvtuDisplay.Scale = [1.0, 1.0, 1.0]
flowvtuDisplay.Orientation = [0.0, 0.0, 0.0]
flowvtuDisplay.Origin = [0.0, 0.0, 0.0]
flowvtuDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
flowvtuDisplay.Pickable = 1
flowvtuDisplay.Triangulate = 0
flowvtuDisplay.UseShaderReplacements = 0
flowvtuDisplay.ShaderReplacements = ''
flowvtuDisplay.NonlinearSubdivisionLevel = 1
flowvtuDisplay.UseDataPartitions = 0
flowvtuDisplay.OSPRayUseScaleArray = 'All Approximate'
flowvtuDisplay.OSPRayScaleArray = 'Density'
flowvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
flowvtuDisplay.OSPRayMaterial = 'None'
flowvtuDisplay.Orient = 0
flowvtuDisplay.OrientationMode = 'Direction'
flowvtuDisplay.SelectOrientationVectors = 'Momentum'
flowvtuDisplay.Scaling = 0
flowvtuDisplay.ScaleMode = 'No Data Scaling Off'
flowvtuDisplay.ScaleFactor = 0.8
flowvtuDisplay.SelectScaleArray = 'Density'
flowvtuDisplay.GlyphType = 'Arrow'
flowvtuDisplay.UseGlyphTable = 0
flowvtuDisplay.GlyphTableIndexArray = 'Density'
flowvtuDisplay.UseCompositeGlyphTable = 0
flowvtuDisplay.UseGlyphCullingAndLOD = 0
flowvtuDisplay.LODValues = []
flowvtuDisplay.ColorByLODIndex = 0
flowvtuDisplay.GaussianRadius = 0.04
flowvtuDisplay.ShaderPreset = 'Sphere'
flowvtuDisplay.CustomTriangleScale = 3
flowvtuDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
flowvtuDisplay.Emissive = 0
flowvtuDisplay.ScaleByArray = 0
flowvtuDisplay.SetScaleArray = ['POINTS', 'Density']
flowvtuDisplay.ScaleArrayComponent = ''
flowvtuDisplay.UseScaleFunction = 1
flowvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
flowvtuDisplay.OpacityByArray = 0
flowvtuDisplay.OpacityArray = ['POINTS', 'Density']
flowvtuDisplay.OpacityArrayComponent = ''
flowvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
flowvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
flowvtuDisplay.SelectionCellLabelBold = 0
flowvtuDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
flowvtuDisplay.SelectionCellLabelFontFamily = 'Arial'
flowvtuDisplay.SelectionCellLabelFontFile = ''
flowvtuDisplay.SelectionCellLabelFontSize = 18
flowvtuDisplay.SelectionCellLabelItalic = 0
flowvtuDisplay.SelectionCellLabelJustification = 'Left'
flowvtuDisplay.SelectionCellLabelOpacity = 1.0
flowvtuDisplay.SelectionCellLabelShadow = 0
flowvtuDisplay.SelectionPointLabelBold = 0
flowvtuDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
flowvtuDisplay.SelectionPointLabelFontFamily = 'Arial'
flowvtuDisplay.SelectionPointLabelFontFile = ''
flowvtuDisplay.SelectionPointLabelFontSize = 18
flowvtuDisplay.SelectionPointLabelItalic = 0
flowvtuDisplay.SelectionPointLabelJustification = 'Left'
flowvtuDisplay.SelectionPointLabelOpacity = 1.0
flowvtuDisplay.SelectionPointLabelShadow = 0
flowvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
flowvtuDisplay.ScalarOpacityFunction = None
flowvtuDisplay.ScalarOpacityUnitDistance = 0.06445693046365307
flowvtuDisplay.UseSeparateOpacityArray = 0
flowvtuDisplay.OpacityArrayName = ['POINTS', 'Density']
flowvtuDisplay.OpacityComponent = ''
flowvtuDisplay.ExtractedBlockIndex = 0
flowvtuDisplay.SelectMapper = 'Projected tetra'
flowvtuDisplay.SamplingDimensions = [128, 128, 128]
flowvtuDisplay.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
flowvtuDisplay.OSPRayScaleFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.84853982925415, 1.0, 0.5, 0.0]
flowvtuDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
flowvtuDisplay.GlyphType.TipResolution = 6
flowvtuDisplay.GlyphType.TipRadius = 0.1
flowvtuDisplay.GlyphType.TipLength = 0.35
flowvtuDisplay.GlyphType.ShaftResolution = 6
flowvtuDisplay.GlyphType.ShaftRadius = 0.03
flowvtuDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
flowvtuDisplay.ScaleTransferFunction.Points = [0.4285181164741516, 0.0, 0.5, 0.0, 3.4053807258605957, 1.0, 0.5, 0.0]
flowvtuDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
flowvtuDisplay.OpacityTransferFunction.Points = [0.4285181164741516, 0.0, 0.5, 0.0, 3.4053807258605957, 1.0, 0.5, 0.0]
flowvtuDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
flowvtuDisplay.DataAxesGrid.XTitle = 'X Axis'
flowvtuDisplay.DataAxesGrid.YTitle = 'Y Axis'
flowvtuDisplay.DataAxesGrid.ZTitle = 'Z Axis'
flowvtuDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
flowvtuDisplay.DataAxesGrid.XTitleFontFile = ''
flowvtuDisplay.DataAxesGrid.XTitleBold = 0
flowvtuDisplay.DataAxesGrid.XTitleItalic = 0
flowvtuDisplay.DataAxesGrid.XTitleFontSize = 12
flowvtuDisplay.DataAxesGrid.XTitleShadow = 0
flowvtuDisplay.DataAxesGrid.XTitleOpacity = 1.0
flowvtuDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
flowvtuDisplay.DataAxesGrid.YTitleFontFile = ''
flowvtuDisplay.DataAxesGrid.YTitleBold = 0
flowvtuDisplay.DataAxesGrid.YTitleItalic = 0
flowvtuDisplay.DataAxesGrid.YTitleFontSize = 12
flowvtuDisplay.DataAxesGrid.YTitleShadow = 0
flowvtuDisplay.DataAxesGrid.YTitleOpacity = 1.0
flowvtuDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
flowvtuDisplay.DataAxesGrid.ZTitleFontFile = ''
flowvtuDisplay.DataAxesGrid.ZTitleBold = 0
flowvtuDisplay.DataAxesGrid.ZTitleItalic = 0
flowvtuDisplay.DataAxesGrid.ZTitleFontSize = 12
flowvtuDisplay.DataAxesGrid.ZTitleShadow = 0
flowvtuDisplay.DataAxesGrid.ZTitleOpacity = 1.0
flowvtuDisplay.DataAxesGrid.FacesToRender = 63
flowvtuDisplay.DataAxesGrid.CullBackface = 0
flowvtuDisplay.DataAxesGrid.CullFrontface = 1
flowvtuDisplay.DataAxesGrid.ShowGrid = 0
flowvtuDisplay.DataAxesGrid.ShowEdges = 1
flowvtuDisplay.DataAxesGrid.ShowTicks = 1
flowvtuDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
flowvtuDisplay.DataAxesGrid.AxesToLabel = 63
flowvtuDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
flowvtuDisplay.DataAxesGrid.XLabelFontFile = ''
flowvtuDisplay.DataAxesGrid.XLabelBold = 0
flowvtuDisplay.DataAxesGrid.XLabelItalic = 0
flowvtuDisplay.DataAxesGrid.XLabelFontSize = 12
flowvtuDisplay.DataAxesGrid.XLabelShadow = 0
flowvtuDisplay.DataAxesGrid.XLabelOpacity = 1.0
flowvtuDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
flowvtuDisplay.DataAxesGrid.YLabelFontFile = ''
flowvtuDisplay.DataAxesGrid.YLabelBold = 0
flowvtuDisplay.DataAxesGrid.YLabelItalic = 0
flowvtuDisplay.DataAxesGrid.YLabelFontSize = 12
flowvtuDisplay.DataAxesGrid.YLabelShadow = 0
flowvtuDisplay.DataAxesGrid.YLabelOpacity = 1.0
flowvtuDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
flowvtuDisplay.DataAxesGrid.ZLabelFontFile = ''
flowvtuDisplay.DataAxesGrid.ZLabelBold = 0
flowvtuDisplay.DataAxesGrid.ZLabelItalic = 0
flowvtuDisplay.DataAxesGrid.ZLabelFontSize = 12
flowvtuDisplay.DataAxesGrid.ZLabelShadow = 0
flowvtuDisplay.DataAxesGrid.ZLabelOpacity = 1.0
flowvtuDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
flowvtuDisplay.DataAxesGrid.XAxisPrecision = 2
flowvtuDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
flowvtuDisplay.DataAxesGrid.XAxisLabels = []
flowvtuDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
flowvtuDisplay.DataAxesGrid.YAxisPrecision = 2
flowvtuDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
flowvtuDisplay.DataAxesGrid.YAxisLabels = []
flowvtuDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
flowvtuDisplay.DataAxesGrid.ZAxisPrecision = 2
flowvtuDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
flowvtuDisplay.DataAxesGrid.ZAxisLabels = []
flowvtuDisplay.DataAxesGrid.UseCustomBounds = 0
flowvtuDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
flowvtuDisplay.PolarAxes.Visibility = 0
flowvtuDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
flowvtuDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
flowvtuDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
flowvtuDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
flowvtuDisplay.PolarAxes.EnableCustomRange = 0
flowvtuDisplay.PolarAxes.CustomRange = [0.0, 1.0]
flowvtuDisplay.PolarAxes.PolarAxisVisibility = 1
flowvtuDisplay.PolarAxes.RadialAxesVisibility = 1
flowvtuDisplay.PolarAxes.DrawRadialGridlines = 1
flowvtuDisplay.PolarAxes.PolarArcsVisibility = 1
flowvtuDisplay.PolarAxes.DrawPolarArcsGridlines = 1
flowvtuDisplay.PolarAxes.NumberOfRadialAxes = 0
flowvtuDisplay.PolarAxes.AutoSubdividePolarAxis = 1
flowvtuDisplay.PolarAxes.NumberOfPolarAxis = 0
flowvtuDisplay.PolarAxes.MinimumRadius = 0.0
flowvtuDisplay.PolarAxes.MinimumAngle = 0.0
flowvtuDisplay.PolarAxes.MaximumAngle = 90.0
flowvtuDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
flowvtuDisplay.PolarAxes.Ratio = 1.0
flowvtuDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.PolarAxisTitleVisibility = 1
flowvtuDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
flowvtuDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
flowvtuDisplay.PolarAxes.PolarLabelVisibility = 1
flowvtuDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
flowvtuDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
flowvtuDisplay.PolarAxes.RadialLabelVisibility = 1
flowvtuDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
flowvtuDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
flowvtuDisplay.PolarAxes.RadialUnitsVisibility = 1
flowvtuDisplay.PolarAxes.ScreenSize = 10.0
flowvtuDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
flowvtuDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
flowvtuDisplay.PolarAxes.PolarAxisTitleFontFile = ''
flowvtuDisplay.PolarAxes.PolarAxisTitleBold = 0
flowvtuDisplay.PolarAxes.PolarAxisTitleItalic = 0
flowvtuDisplay.PolarAxes.PolarAxisTitleShadow = 0
flowvtuDisplay.PolarAxes.PolarAxisTitleFontSize = 12
flowvtuDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
flowvtuDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
flowvtuDisplay.PolarAxes.PolarAxisLabelFontFile = ''
flowvtuDisplay.PolarAxes.PolarAxisLabelBold = 0
flowvtuDisplay.PolarAxes.PolarAxisLabelItalic = 0
flowvtuDisplay.PolarAxes.PolarAxisLabelShadow = 0
flowvtuDisplay.PolarAxes.PolarAxisLabelFontSize = 12
flowvtuDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
flowvtuDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
flowvtuDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
flowvtuDisplay.PolarAxes.LastRadialAxisTextBold = 0
flowvtuDisplay.PolarAxes.LastRadialAxisTextItalic = 0
flowvtuDisplay.PolarAxes.LastRadialAxisTextShadow = 0
flowvtuDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
flowvtuDisplay.PolarAxes.EnableDistanceLOD = 1
flowvtuDisplay.PolarAxes.DistanceLODThreshold = 0.7
flowvtuDisplay.PolarAxes.EnableViewAngleLOD = 1
flowvtuDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
flowvtuDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
flowvtuDisplay.PolarAxes.PolarTicksVisibility = 1
flowvtuDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
flowvtuDisplay.PolarAxes.TickLocation = 'Both'
flowvtuDisplay.PolarAxes.AxisTickVisibility = 1
flowvtuDisplay.PolarAxes.AxisMinorTickVisibility = 0
flowvtuDisplay.PolarAxes.ArcTickVisibility = 1
flowvtuDisplay.PolarAxes.ArcMinorTickVisibility = 0
flowvtuDisplay.PolarAxes.DeltaAngleMajor = 10.0
flowvtuDisplay.PolarAxes.DeltaAngleMinor = 5.0
flowvtuDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
flowvtuDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
flowvtuDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
flowvtuDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
flowvtuDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
flowvtuDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
flowvtuDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
flowvtuDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
flowvtuDisplay.PolarAxes.ArcMajorTickSize = 0.0
flowvtuDisplay.PolarAxes.ArcTickRatioSize = 0.3
flowvtuDisplay.PolarAxes.ArcMajorTickThickness = 1.0
flowvtuDisplay.PolarAxes.ArcTickRatioThickness = 0.5
flowvtuDisplay.PolarAxes.Use2DMode = 0
flowvtuDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(2240, 869)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, -21.18221983093764, 0.0]
renderView1.CameraFocalPoint = [0.023397480901081735, -2.2118221983093758, -0.05264433202743386]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraViewAngle = 1.9285714285714286
renderView1.CameraParallelScale = 6.0

# get active source.
flowvtu = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
flowvtuDisplay = GetDisplayProperties(flowvtu, view=renderView1)

# set scalar coloring
ColorBy(flowvtuDisplay, ('POINTS', 'Mach'))

# rescale color and/or opacity maps used to include current data range
flowvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
flowvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Mach'
machLUT = GetColorTransferFunction('Mach')
machLUT.RGBPoints = [0.0, 0.0, 0.0, 1.0, 2.1264488697052, 1.0, 0.0, 0.0]
machLUT.ColorSpace = 'HSV'
machLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
machLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Mach'
machPWF = GetOpacityTransferFunction('Mach')
machPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.1264488697052, 1.0, 0.5, 0.0]
machPWF.ScalarRangeInitialized = 1

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1920, 1080)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-3.5974469823878126, -11.41891447894513, -0.064384382801326]
renderView1.CameraFocalPoint = [-0.36304394402882767, -1.210728328490714, -0.07886880653234314]
renderView1.CameraViewUp = [-0.007955715093820722, 0.003939567854077691, 0.9999605924247561]
renderView1.CameraViewAngle = 1.9285714285714286
renderView1.CameraParallelScale = 6.0

SaveScreenshot('Mach.png', renderView1)

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Cp calculation
# create a new 'XML Unstructured Grid Reader'
surface_flowvtu = XMLUnstructuredGridReader(registrationName='surface_flow.vtu', FileName=['surface_flow.vtu'])
surface_flowvtu.PointArrayStatus = ['Density', 'Momentum', 'Energy', 'Nu_Tilde', 'Pressure', 'Temperature', 'Mach', 'Pressure_Coefficient', 'Laminar_Viscosity', 'Skin_Friction_Coefficient', 'Heat_Flux', 'Y_Plus', 'Eddy_Viscosity']

# find source
flowvtu = FindSource('flow.vtu')

# Properties modified on surface_flowvtu
surface_flowvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
surface_flowvtuDisplay = Show(surface_flowvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
surface_flowvtuDisplay.Representation = 'Surface'
surface_flowvtuDisplay.ColorArrayName = [None, '']
surface_flowvtuDisplay.SelectTCoordArray = 'None'
surface_flowvtuDisplay.SelectNormalArray = 'None'
surface_flowvtuDisplay.SelectTangentArray = 'None'
surface_flowvtuDisplay.OSPRayScaleArray = 'Density'
surface_flowvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
surface_flowvtuDisplay.SelectOrientationVectors = 'Momentum'
surface_flowvtuDisplay.ScaleFactor = 0.0800000011920929
surface_flowvtuDisplay.SelectScaleArray = 'Density'
surface_flowvtuDisplay.GlyphType = 'Arrow'
surface_flowvtuDisplay.GlyphTableIndexArray = 'Density'
surface_flowvtuDisplay.GaussianRadius = 0.004000000059604645
surface_flowvtuDisplay.SetScaleArray = ['POINTS', 'Density']
surface_flowvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
surface_flowvtuDisplay.OpacityArray = ['POINTS', 'Density']
surface_flowvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
surface_flowvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
surface_flowvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
surface_flowvtuDisplay.ScalarOpacityUnitDistance = 0.02455672540831468
surface_flowvtuDisplay.OpacityArrayName = ['POINTS', 'Density']

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
surface_flowvtuDisplay.OSPRayScaleFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.84853982925415, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
surface_flowvtuDisplay.ScaleTransferFunction.Points = [0.4285181164741516, 0.0, 0.5, 0.0, 1.433653473854065, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
surface_flowvtuDisplay.OpacityTransferFunction.Points = [0.4285181164741516, 0.0, 0.5, 0.0, 1.433653473854065, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=surface_flowvtu)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'Density']
clip1.Value = 0.9310857951641083

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.1000099206039522, 0.4000000059604645, -5.122274160385132e-09]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [0.1000099206039522, 0.4000000059604645, -5.122274160385132e-09]

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = [None, '']
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'Density'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'Momentum'
clip1Display.ScaleFactor = 0.0800000011920929
clip1Display.SelectScaleArray = 'Density'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'Density'
clip1Display.GaussianRadius = 0.004000000059604645
clip1Display.SetScaleArray = ['POINTS', 'Density']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'Density']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityUnitDistance = 0.028707062697049895
clip1Display.OpacityArrayName = ['POINTS', 'Density']

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip1Display.OSPRayScaleFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.84853982925415, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [0.4285181164741516, 0.0, 0.5, 0.0, 1.3337230682373047, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [0.4285181164741516, 0.0, 0.5, 0.0, 1.3337230682373047, 1.0, 0.5, 0.0]

# hide data in view
Hide(surface_flowvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on clip1.ClipType
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, 0.4000000059604645, -5.122274160385132e-09]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, 0.4000000059604645, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on clip1.ClipType
clip1.ClipType.Normal = [0.0, 0.0, -1.0]

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=clip1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.10001023954919219, 0.4000000059604645, 0.005239203572273254]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.10001023954919219, 0.4000000059604645, 0.005239203572273254]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = [None, '']
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'Density'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'Momentum'
slice1Display.ScaleFactor = 0.0800000011920929
slice1Display.SelectScaleArray = 'Density'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'Density'
slice1Display.GaussianRadius = 0.004000000059604645
slice1Display.SetScaleArray = ['POINTS', 'Density']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'Density']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice1Display.OSPRayScaleFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.84853982925415, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.7648636698722839, 0.0, 0.5, 0.0, 0.9889446496963501, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.7648636698722839, 0.0, 0.5, 0.0, 0.9889446496963501, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.10001023954919219, 0.32, 0.005239203572273254]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.10001023954919219, 0.32, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.32, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData('data_eta60.csv', proxy=slice1, PointDataArrays=['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Temperature', 'Y_Plus'])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(2240, 623)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-1.2483816948989992, 0.657932865163394, 0.8091650569620238]
renderView1.CameraFocalPoint = [0.10000992060395222, 0.4000000059604644, -5.122274179060639e-09]
renderView1.CameraViewUp = [0.08915495639534121, 0.9823289731406115, -0.16456361164806937]
renderView1.CameraParallelScale = 0.4124439968804902

# find source
surface_flowvtu = FindSource('surface_flow.vtu')

# set active source
SetActiveSource(surface_flowvtu)

# find source
flowvtu = FindSource('flow.vtu')

# find source
clip1 = FindSource('Clip1')

# find source
slice1 = FindSource('Slice1')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# hide data in view
Hide(slice1, renderView1)

# set active source
SetActiveSource(surface_flowvtu)

# show data in view
surface_flowvtuDisplay = Show(surface_flowvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
surface_flowvtuDisplay.Representation = 'Surface'
surface_flowvtuDisplay.ColorArrayName = [None, '']
surface_flowvtuDisplay.SelectTCoordArray = 'None'
surface_flowvtuDisplay.SelectNormalArray = 'None'
surface_flowvtuDisplay.SelectTangentArray = 'None'
surface_flowvtuDisplay.OSPRayScaleArray = 'Density'
surface_flowvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
surface_flowvtuDisplay.SelectOrientationVectors = 'Momentum'
surface_flowvtuDisplay.ScaleFactor = 0.0800000011920929
surface_flowvtuDisplay.SelectScaleArray = 'Density'
surface_flowvtuDisplay.GlyphType = 'Arrow'
surface_flowvtuDisplay.GlyphTableIndexArray = 'Density'
surface_flowvtuDisplay.GaussianRadius = 0.004000000059604645
surface_flowvtuDisplay.SetScaleArray = ['POINTS', 'Density']
surface_flowvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
surface_flowvtuDisplay.OpacityArray = ['POINTS', 'Density']
surface_flowvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
surface_flowvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
surface_flowvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
surface_flowvtuDisplay.ScalarOpacityUnitDistance = 0.02455672540831468
surface_flowvtuDisplay.OpacityArrayName = ['POINTS', 'Density']

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
surface_flowvtuDisplay.OSPRayScaleFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.84853982925415, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
surface_flowvtuDisplay.ScaleTransferFunction.Points = [0.4285181164741516, 0.0, 0.5, 0.0, 1.433653473854065, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
surface_flowvtuDisplay.OpacityTransferFunction.Points = [0.4285181164741516, 0.0, 0.5, 0.0, 1.433653473854065, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=surface_flowvtu)
clip2.ClipType = 'Plane'
clip2.HyperTreeGridClipper = 'Plane'
clip2.Scalars = ['POINTS', 'Density']
clip2.Value = 0.9310857951641083

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [0.1000099206039522, 0.4000000059604645, -5.122274160385132e-09]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip2.HyperTreeGridClipper.Origin = [0.1000099206039522, 0.4000000059604645, -5.122274160385132e-09]

# show data in view
clip2Display = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'
clip2Display.ColorArrayName = [None, '']
clip2Display.SelectTCoordArray = 'None'
clip2Display.SelectNormalArray = 'None'
clip2Display.SelectTangentArray = 'None'
clip2Display.OSPRayScaleArray = 'Density'
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.SelectOrientationVectors = 'Momentum'
clip2Display.ScaleFactor = 0.0800000011920929
clip2Display.SelectScaleArray = 'Density'
clip2Display.GlyphType = 'Arrow'
clip2Display.GlyphTableIndexArray = 'Density'
clip2Display.GaussianRadius = 0.004000000059604645
clip2Display.SetScaleArray = ['POINTS', 'Density']
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityArray = ['POINTS', 'Density']
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display.DataAxesGrid = 'GridAxesRepresentation'
clip2Display.PolarAxes = 'PolarAxesRepresentation'
clip2Display.ScalarOpacityUnitDistance = 0.028707062697049895
clip2Display.OpacityArrayName = ['POINTS', 'Density']

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip2Display.OSPRayScaleFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.84853982925415, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip2Display.ScaleTransferFunction.Points = [0.4285181164741516, 0.0, 0.5, 0.0, 1.3337230682373047, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip2Display.OpacityTransferFunction.Points = [0.4285181164741516, 0.0, 0.5, 0.0, 1.3337230682373047, 1.0, 0.5, 0.0]

# hide data in view
Hide(surface_flowvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [0.1000099206039522, 0.4000000059604645, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [0.1000099206039522, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [0.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on clip2.ClipType
clip2.ClipType.Normal = [1.0, 0.0, 1.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on clip2.ClipType
clip2.ClipType.Normal = [0.0, 0.0, 1.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(clip1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip2.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(clip2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip2.ClipType)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(clip1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip2.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = [None, '']
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'Density'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'Momentum'
clip1Display.ScaleFactor = 0.0800000011920929
clip1Display.SelectScaleArray = 'Density'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'Density'
clip1Display.GaussianRadius = 0.004000000059604645
clip1Display.SetScaleArray = ['POINTS', 'Density']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'Density']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityUnitDistance = 0.028707062697049895
clip1Display.OpacityArrayName = ['POINTS', 'Density']

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip1Display.OSPRayScaleFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.84853982925415, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [0.4285181164741516, 0.0, 0.5, 0.0, 1.3337230682373047, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [0.4285181164741516, 0.0, 0.5, 0.0, 1.3337230682373047, 1.0, 0.5, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(clip1, renderView1)

# set active source
SetActiveSource(clip2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip2.ClipType)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice2 = Slice(registrationName='Slice2', Input=clip2)
slice2.SliceType = 'Plane'
slice2.HyperTreeGridSlicer = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [0.1000099206039522, 0.4000000059604645, -0.005239208694547415]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice2.HyperTreeGridSlicer.Origin = [0.1000099206039522, 0.4000000059604645, -0.005239208694547415]

# show data in view
slice2Display = Show(slice2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = [None, '']
slice2Display.SelectTCoordArray = 'None'
slice2Display.SelectNormalArray = 'None'
slice2Display.SelectTangentArray = 'None'
slice2Display.OSPRayScaleArray = 'Density'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'Momentum'
slice2Display.ScaleFactor = 0.0800000011920929
slice2Display.SelectScaleArray = 'Density'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'Density'
slice2Display.GaussianRadius = 0.004000000059604645
slice2Display.SetScaleArray = ['POINTS', 'Density']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'Density']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice2Display.OSPRayScaleFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.84853982925415, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [0.7733232378959656, 0.0, 0.5, 0.0, 0.9867987036705017, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [0.7733232378959656, 0.0, 0.5, 0.0, 0.9867987036705017, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip2, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [0.1000099206039522, 0.32, -0.005239208694547415]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [0.1000099206039522, 0.32, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [0.0, 0.32, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice2.SliceType
slice2.SliceType.Normal = [0.0, 1.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData('data_eta30.csv', proxy=slice2, PointDataArrays=['Density', 'Eddy_Viscosity', 'Energy', 'Heat_Flux', 'Laminar_Viscosity', 'Mach', 'Momentum', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Temperature', 'Y_Plus'])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(2236, 619)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-2.2887480781481147, 0.8569437999428741, 1.4334852614288722]
renderView1.CameraFocalPoint = [0.1000099206039522, 0.4000000059604645, -5.122274160385132e-09]
renderView1.CameraViewUp = [0.08915495639534121, 0.9823289731406115, -0.16456361164806937]
renderView1.CameraParallelScale = 0.4124439968804902

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

data = numpy.genfromtxt("data_eta30.csv", skip_header=1, skip_footer=1, delimiter=",", names=["Density", "Momentum:0", "Momentum:1", "Momentum:2", "Energy", "Nu_Tilde", "Pressure", "Temperature", "Mach", "Pressure_Coefficient", "Laminar_Viscosity", "Skin_Friction_Coefficient:0", "Skin_Friction_Coefficient:1", "Skin_Friction_Coefficient:2", "Heat_Flux", "Y_Plus", "Eddy_Viscosity", "x", "Points:1", "Points:2"])

plt.plot(data['x']/0.2, -data['Pressure_Coefficient'], 'o')
plt.title("Plot Cp vs x/c eta=0.30")
plt.xlabel("x/c")
plt.ylabel("Cp")
plt.savefig('cp30.png')
#  plt.show()
