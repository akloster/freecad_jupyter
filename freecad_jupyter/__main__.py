import os, sys, pathlib

base = pathlib.Path(sys.executable)
base = pathlib.Path(base).parent.parent
fp = os.environ.get("FREECAD_PATH", None)
if fp:
    base = pathlib.Path(fp)
sys.path.append(str(base)+"/")
sys.path.append(str(base/"lib")+"/")

from ipykernel import kernelapp as app
from traitlets.config import Config
c = Config()
c.IPKernelApp.gui="qt5"

c.IPKernelApp.code_to_run="""
from freecad_jupyter import init_gui
init_gui()

"""
print(c)
#@register_line_magic
#def freecad_gui(line):
#    print("hello World")
#    return line
app.launch_new_instance(config=c)
