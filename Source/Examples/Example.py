from ctypes import cdll

lib = cdll.LoadLibrary('../../Build/libEngine.so')

class Engine(object):

    def __init__(self):
        self.obj = lib.Engine_new()

    def Initialize(self):    
        lib.Engine_Initialize(self.obj)

class Renderer(object):

    def __init__(self):
        self.obj = lib.Renderer_new()

    def Load(self):    
        lib.Renderer_Load(self.obj)

engine = Engine()
renderer = Renderer()

engine.Initialize()
renderer.Load()
renderer.Update()