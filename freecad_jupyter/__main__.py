import sys,pathlib

prefix = pathlib.Path(sys.executable).parent.parent
sys.path.append(str(prefix)+"/")
sys.path.append(str(prefix/"lib")+"/")

from ipykernel import kernelapp as app
app.launch_new_instance()
ipykernel.start_kernel()
