# -*- coding: utf-8 -*-

"""Top-level package for freecad-jupyter."""

__author__ = """Andreas Klostermann"""
__email__ = 'andreasklostermann@gmail.com'
__version__ = '0.1.0'

def init_gui():
    import sys
    kernel_stream = sys.stdout
    import FreeCADGui
    FreeCADGui.showMainWindow()
    sys.stdout = kernel_stream
    sys.stderr = kernel_stream

