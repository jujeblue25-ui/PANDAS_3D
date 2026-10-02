from direct.showbase.ShowBase import ShowBase
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel("panda")
        self.model.reparentTo(render)
        self.model.setScale(0.1)
        self.model.setPos(-2, 25, -3)
        base.camLens.setFov(90)
        New_texture = self.loader.loadTexture("hola-thanos.png")
        self.model.setTexture(New_texture, 1)
game = Game()
game.run()