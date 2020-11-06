from pipeline.engines import engine
import subprocess, os, platform

class StandaloneEngine(engine.Engine):

    mayabatch = "C:/Program Files/Autodesk/Maya2020/bin/mayabatch.exe"
    abc_export_script = "C:/Users/Asus/Desktop/WorkshopPython/pipeline/abc/abc_export.py"
    hython = "C:/Program Files/Side Effects Software/Houdini 18.0.597/bin/hython.exe"
    houdini_import = "C:/Users/Asus/Desktop/WorkshopPython/pipeline/engines/houdini/houdini_import.py"

    def open(self, path):
        if(platform.system() == "Windows"):
            os.startfile(path)
        pass

    def save(self):
        pass

    def export(self, in_file, directory_out):

        references = open(in_file, 'r')
        namespace_list = []

        for line in references.readlines():
            if "createNode transform -n" in line:
                print(line)
                namespace_list.append(line.split('-n')[1].split(' ')[1].replace(';', '').replace('"', '').replace('\n', ''))

        print(namespace_list)
        str_namespace = ' '.join(namespace_list)
        
        exec_file = "python(\"execfile(\'{}\')\");".format(self.abc_export_script)
        print(exec_file)

        maya_export_query = [self.mayabatch, '-command', exec_file, in_file, directory_out, str_namespace]

        print(' '.join(maya_export_query))

        subprocess.call(maya_export_query, shell=True)

        pass

    def importation(self, directory):

        houdini_import_query = [self.hython, self.houdini_import, directory, directory]
        print(houdini_import_query)
        subprocess.call(houdini_import_query, shell=True)

        pass

