from pipeline.engines import engine
import hou 


class HoudiniEngine(engine.Engine):

    def open(self, path):
        hou.hipFile.load(path)
        pass

    def save(self):
        hou.hipFile.save("C:\Users\Asus\Desktop\test.hip")
        pass
    