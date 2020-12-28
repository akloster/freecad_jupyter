# freecad-jupyter

A Kernel and Utilities to control FreeCAD from Jupyter Notebook and Lab

## Table of Content:

- [Intallation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Credits](#credits)

## Installation

This has only been tested on Ubuntu. You may be able to get this to work on Windows or OSX.

The main issue, in the belief of this package's author, is that FreeCAD is extremely clumsy, messy and particular about importing its various python modules and C extensions. According to the documentation it should be just
as easy as adding one directory to the library path and "import FreeCAD",
but it isn't, and the behavior of those modules changed somewhat even since
the author has been experimenting with it.

### Conda

Conda is a package manager for Python and other programming languages. You need to download and install that first.

> conda create --name fcenv-dev --channel conda-forge --channel freecad/label/dev freecad
> pip install git+https://github.com/akloster/freecad_jupyter

This worked at the time of this writing. It sometimes brakes. The solution often is to search for and install the latest working build:

> conda search -channel conda-forge --channel freecad/label/dev freecad
> conda create --name fcenv-dev --channel conda-forge --channel freecad/label/dev freecad=0.19_pre=py19__etc

That's the price you pay for cutting edge builds.

Now the next step is to install the kernel.

Create a file at ~/.local/share/jupyter/kernels/freecad-conda/kernels.json with the following content:

```
{
 "argv": [
  "{your-anaconda-environment}/bin/python3",
  "-m",
  "freecad_jupyter",
  "-f",
  "{connection_file}"
 ],
 "display_name": "FreeCad (conda,dev)",
 "language": "python"
}
```      

You have to replace {your-anaconda-environment} with the directory of your anaconda environment.

## Usage

Most FreeCAD Functionality should work as expected. Some Addons don't.

You need to initialize FreeCAD in your notebook with 

>%init_freecad gui

That will modify the Pythonpath, configure the QT Event loop, import FreeCAD and open the main window.

Check the version of Freecad you installed through the "about" dialog. If it is a lot older than you expect, then you should try creating a brand new conda environment and make sure to use the command written in the above installation instructions. Otherwise you might get an older build or one for an older version of Python.

## More Details

The Jupyter server allows you to connect to many different kernels, which can offer different environments and programming languages. They can run locally on the same machine as the server or even remotely over a network.

What this package here simply does is to wrap the usual "IPython" kernel application such that it works nicely with FreeCAD. To do this, it is important to put the Kernel in QT mode, and import the Pyside2 libraries before anything else has the opportunity to mess this up.

This has only been tested on Ubuntu, not on other Linux systems or even Windows. Technically it should be possible to make it work, but there will be differences in how to make sure the right Python libraries talk to the right FreeCAD libraries the right way. 

## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

For more info please click [here](./CONTRIBUTING.md)


## Credits

This package was created with Cookiecutter and the `oldani/cookiecutter-simple-pypackage` project template.

- [Cookiecutter](https://github.com/audreyr/cookiecutter)
- [oldani/cookiecutter-simple-pypackage](https://github.com/oldani/cookiecutter-simple-pypackage)
