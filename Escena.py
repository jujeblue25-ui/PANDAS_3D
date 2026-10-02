from direct.showbase.ShowBase import ShowBase
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel("models/environment")
        self.model.reparentTo(render)
        self.model.setScale(0.1)
        self.model.setPos(16, -10, 6)
        base.camLens.setFov(100)
game = Game()
game.run()