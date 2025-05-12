from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from panda3d.direct import *
loadPrcFileData('', 'window-type none')
base = ShowBase()                      
ConfigVariableString('window-type', 'none').setValue('none')
base.makeAllPipes()
print(base.pipe.type)

pipe = base.pipe
fbProps = FrameBufferProperties.getDefault()
winProps = WindowProperties.getDefault()
sort_order = 0
bf = base.graphics_engine.makeOutput(pipe, 'def0', sort_order, fbProps, winProps, GraphicsPipe.BFRefuseWindow)
print(bf)
