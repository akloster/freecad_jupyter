# freecad-jupyter

A Kernel and Utilities to control FreeCAD from Jupyter Notebook and Lab

## Table of Content:

- [Intallation](#installation)
- [Usage](#usage)
- [TODO](#todo)
- [Known Issues](#issues)
- [Contributing](#contributing)
- [Credits](#credits)

## Installation

This has only been tested on Ubuntu. You may be able to get this to work on Windows or OSX.

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
  "--gui","qt5",
  "--matplotlib","qt5",
  "-f",
  "{connection_file}"
 ],
 "display_name": "FreeCad(GUI)",
 "language": "python"
}
```
## Usage

Now you can choose the "FreeCAD(GUI)" kernel in Jupyter notebook or lab. The kernel is already running in qt5 mode.

To launch the main window do this:

```python
import FreeCAD
import FreeCADGui
FreeCADGui.showMainWindow()
```

## TODO

- automatic installer for the kernelspec
- create example notebooks
- explore how to use matplotlib better

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
