import sys, os
import hou

in_directory = sys.argv[1]
out_directory = sys.argv[2]

final_file = os.path.join(out_directory, 'test.hipnc')
print(final_file)

hou.hipFile.save(final_file)
hou.hipFile.load(final_file)

node = hou.node("/obj")
node.createNode("geo")

for file in os.listdir(in_directory):
    if file.endswith(".abc"):
        filename = os.path.join(in_directory, file)
        print(filename)
        base_node = hou.node("/obj/geo1")
        node = base_node.createNode("alembic")
        node.parm('fileName').set(filename)

hou.hipFile.save(final_file)
print("import finished")
