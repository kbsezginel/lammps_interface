from setuptools import setup, find_packages

setup(
    name="lammps_interface",
    version="0.1",
    description="Automatic generation of LAMMPS input files for molecular dynamics simulations of MOFs",
    install_requires=['numpy',
                      'scipy',
                      'networkx<=1.9',
                      'matplotlib'],
    include_package_data=True,
    packages=find_packages()
)
