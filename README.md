[![Build Status](https://travis-ci.org/kbsezginel/lammps_interface.svg?branch=master)](https://travis-ci.org/kbsezginel/lammps_interface)
# LAMMPS Interface
## Authors

-   Peter Boyd
-   Mohamad Moosavi
-   Matthew Witman

## Description
This program was designed for easy interface between the crystallographic
information file (.[cif]) and the Large-scale Atomic Molecular Massively
Parallel Simulator ([Lammps]).

## Installation
Clone the repository, enter the directory and install dependencies by:
```
pip install -r requirements.txt
```

The Python module can be installed globally by:
```
python setup.py install
```

## Usage

### Command line interface
To see the optional arguments type:
```
python lammps_interface.py --help
```
To create [Lammps] simulation files for a given cif file type:
```
python lammps_interface.py cif_file.cif
```
This will create [Lammps] simulation files with UFF parameters.

### Jupyter notebook
In order to implement module to your project check out Jupyter notebooks provided in this repository in `/notebooks` for usage examples.

## Licence
MIT licence (see LICENCE file)

## Citation
The publication associated with this code is found here:

Boyd, P. G., Moosavi, S. M., Witman, M. & Smit, B. Force-Field Prediction of Materials Properties in Metal-Organic Frameworks. J. Phys. Chem. Lett. 8, 357–363 (2017).

dx.doi.org/10.1021/acs.jpclett.6b02532

[Lammps]: http://lammps.sandia.gov/
[cif]: https://en.wikipedia.org/wiki/Crystallographic_Information_File
