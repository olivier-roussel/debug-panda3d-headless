from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from panda3d.direct import *

loadPrcFileData("",
"""
    gl-debug true
    audio-library-name null
    window-type offscreen
    notify-level-glgsg debug
    notify-level-display debug
    notify-level-egldisplay spam
    load-display p3tinydisplay
""")

base = ShowBase(windowType='offscreen')

model = loader.loadModel('environment')
model.reparentTo(base.render)

base.graphicsEngine.renderFrame()
base.graphicsEngine.renderFrame()
base.graphicsEngine.renderFrame()
base.graphicsEngine.renderFrame()

base.screenshot('test.jpg', defaultFilename=False)