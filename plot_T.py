#!/usr/bin/env python3

# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
import os

argv1 = sys.argv[1]
argv2 = sys.argv[2]
#  argv3 = sys.argv[3]

imageName = argv1 + '-' + argv2# + '-' + argv3
#  print(imageName)

os.system('touch case.foam')

#### disable automatic camera reset on 'Show'
casefoam_1 = OpenFOAMReader(registrationName='case.foam', FileName='case.foam')
paraview.simple._DisableFirstRenderCameraReset()

LoadPalette(paletteName='PrintBackground')

# get active source.
casefoam = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
casefoamDisplay = Show(casefoam, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
casefoamDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0

# set scalar coloring
ColorBy(casefoamDisplay, ('POINTS', 'T'))
tLUT = GetColorTransferFunction('T')
tLUT.ApplyPreset('Blue to Red Rainbow', True)

# rescale color and/or opacity maps used to include current data range
casefoamDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
casefoamDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'T'
tLUT = GetColorTransferFunction('T')

# get opacity transfer function/opacity map for 'T'
tPWF = GetOpacityTransferFunction('T')

# get animation scene
animationScene1 = GetAnimationScene()

# Properties modified on animationScene1
animationScene1.AnimationTime = 1.0

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# get color legend/bar for tLUT in view renderView1
tLUTColorBar = GetScalarBar(tLUT, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# change scalar bar placement
tLUTColorBar.WindowLocation = 'AnyLocation'
tLUTColorBar.Position = [0.625, 0.32]
tLUTColorBar.ScalarBarLength = 0.3300000000000001
tLUTColorBar.TitleFontSize = 28
tLUTColorBar.LabelFontSize = 28
tLUTColorBar.ScalarBarThickness = 28
# Rescale transfer function
tLUT.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
tPWF.RescaleTransferFunction(0.0, 1.0)
#  casefoamDisplay.RescaleTransferFunctionToDataRange(False, True)

# get layout
layout1 = GetLayout()

#  # current camera placement for renderView1
#  renderView1.InteractionMode = '2D'
#  renderView1.CameraPosition = [0.07077729389037203, 0.04790481152032053, 0.27388724585114677]
#  renderView1.CameraFocalPoint = [0.07077729389037203, 0.04790481152032053, 0.0]
#  renderView1.CameraParallelScale = 0.07088723543695315

# change scalar bar placement
#  tLUTColorBar.Position = [0.729245283018868, 0.36206896551724127]

# layout/tab size in pixels
layout1.SetSize(2560, 1080)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.06856522427499831, 0.04802602081431361, 0.27388724585114677]
renderView1.CameraFocalPoint = [0.06856522427499831, 0.04802602081431361, 0.0]
renderView1.CameraParallelScale = 0.05858449209665548

# save screenshot
SaveScreenshot('T.png', renderView1, ImageResolution=[2560, 1080], TransparentBackground=1)
os.system('convert T.png -crop 0x0+625+50 -crop 2560x1080-770-90 +repage  /home/pedro/workshop04_fvm/transiente/imagens_temperatura/%s.png && rm T.png'%imageName)
