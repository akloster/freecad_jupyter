import os
import sys
import pathlib

def run_kernel():
    from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
        QVBoxLayout, QDialog)
    import ipykernel
    from ipykernel import kernelapp as app
    from traitlets.config import Config
    c = Config()
    c.IPKernelApp.gui="qt5"
    c.IPKernelApp.code_to_run="""
    from IPython.core.magic import register_line_magic
            

    @register_line_magic
    def init_freecad(line):
        global _notebook_stdout, _notebook_stderr
        args = line.split()
        import sys
        from pathlib import Path
        p = sys.base_exec_prefix+"/"
        print(p)
        sys.path += [p+"Ext", p+"lib", p+"libexec"]

        import FreeCAD as app
        from IPython.external.qt_loaders import ImportDenier
        if isinstance(sys.meta_path[0], ImportDenier):
            del(sys.meta_path[0])
        ipython = get_ipython()
        if "gui" in args:
            import FreeCADGui as Gui
            #ipython.user_global_ns["Gui"]= Gui
            _notebook_stdout, _notebook_stderr = sys.stdout, sys.stderr
            Gui.showMainWindow()
            ipython.user_global_ns["App"]= App
            ipython.user_global_ns["Gui"]= Gui
            import asyncio
            async def restore_comms():
                sys.stdout, sys.stderr = _notebook_stdout, _notebook_stderr
            asyncio.Task(restore_comms())
            return "FreeCAD initialized. 'App' and 'Gui' added to global namespace."
        else:
            ipython.user_global_ns["App"]= App
            return "FreeCAD initialized. 'App' added to global namespace."
    """
    app.launch_new_instance(config=c)
if __name__=="__main__":
    run_kernel()
