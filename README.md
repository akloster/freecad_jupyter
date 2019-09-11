# freecad-jupyter

A Kernel and Utilities to control FreeCAD from Jupyter Notebook and Lab

## Table of Content:

- [Intallation](#installation)
- [Usage](#usage)
- [TODO](#todo)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [Credits](#credits)

## Installation

This has only been tested on Ubuntu. You may be able to get this to work on Windows or OSX.

### Using Conda

First you need to have FreeCAD installed in a Conda environment as shown here: https://github.com/FreeCAD/FreeCAD_Conda

```batch

    $ pip install git+https://github.com/akloster/freecad_jupyter
```

You will also need to install a kernelspec. Kernels are stored for example at `~/.local/share/jupyter/kernels`. Make a new directory there, for example called "freecad". The name doesn't matter.

Put the following `kernel.json` file there, and replace the first "argv" entry to find the right Python executable:

```json
{
 "argv": [
  "my-conda-envs/freecad2/bin/python3",
  "-m",
  "freecad_jupyter",
  "-f",
  "{connection_file}"
 ],
 "display_name": "FreeCad(GUI)",
 "language": "python"
}
```

### System Python 3.7 and self-built FreeCAD Daily

I had the best results os far with building FreeCAD myself and using the system Python.

```bash
$ /usr/bin/pip3 install --user ipykernel
$ cd ~/freecad_jupyter
$ /usr/bin/pip3 install --user -e .
```

You need a kernelspec like the following:

```json
{
 "argv": [
  "/usr/bin/python3.7",
  "-m",
  "freecad_jupyter",
  "-f",
  "{connection_file}"
 ],
 "env":{"FREECAD_PATH":"/home/myself/freecad-build"},
 "display_name": "Freecad(GUI)",
 "language": "python"
}
```

## Usage

Now you can choose the "FreeCAD(GUI)" kernel in Jupyter notebook or lab. 

To launch the main window do this:

```python
import FreeCAD
import FreeCADGui
%gui qt5
FreeCADGui.showMainWindow()
```

It's important to set up the qt5 gui integration (`%gui qt5`) after importing FreeCADGui,
because otherwise the IPython kernel will initialize PyQT5 instead of PySide and FreeCAD will get confused!

You may also only import `FreeCAD` if you don't need the GUI.


## TODO

- [ ] automatic installer for the kernelspec
- [ ] create example notebooks
- [ ] explore how to use matplotlib better

## Known Issues

- matplotlib "inline" backend doesn't work
- Python-Shell inside FreeCAD doesn't work when running the kernel
- the Conda recipes for FreeCAD seem to use PyQT and not PySide


## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

For more info please click [here](./CONTRIBUTING.md)


## Credits

This package was created with Cookiecutter and the `oldani/cookiecutter-simple-pypackage` project template.

- [Cookiecutter](https://github.com/audreyr/cookiecutter)
- [oldani/cookiecutter-simple-pypackage](https://github.com/oldani/cookiecutter-simple-pypackage)
