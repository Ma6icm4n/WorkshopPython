import sys 

class Engine(object):

    def open(self, path):
        pass

    def save(self):
        pass

    def export(self, in_file, directory_out):
        pass

    def importation(self, directory):
        pass


def get_current():

    engine = Engine()

    if 'maya' in sys.executable:
        from pipeline.engines.maya import maya_engine
        engine = maya_engine.MayaEngine()
        return engine

    if 'houdini' in sys.executable:
        from pipeline.engines.houdini import houdini_engine
        engine = houdini_engine.HoudiniEngine()
        return engine

    
    from pipeline.engines.standalone import standalone_engine
    engine = standalone_engine.StandaloneEngine()
    return engine

    