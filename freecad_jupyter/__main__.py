import os, sys, pathlib

base = pathlib.Path(sys.executable)
base = pathlib.Path(base).parent.parent
fp = os.environ.get("FREECAD_PATH", None)
if fp:
    base = pathlib.Path(fp)
sys.path.append(str(base)+"/")
sys.path.append(str(base/"lib")+"/")

from ipykernel import kernelapp as app
import ipykernel
app.launch_new_instance()
ipykernel.start_kernel()
