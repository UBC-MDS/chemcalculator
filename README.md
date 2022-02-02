# chemcalculator

[![Documentation Status](https://readthedocs.org/projects/chemcalculator/badge/?version=latest)](https://chemcalculator.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/UBC-MDS/chemcalculator/branch/main/graph/badge.svg?token=pbmgIww2wM)](https://codecov.io/gh/UBC-MDS/chemcalculator)
[![deploy](https://github.com/UBC-MDS/chemcalculator/actions/workflows/deploy.yml/badge.svg)](https://github.com/UBC-MDS/chemcalculator/actions/workflows/deploy.yml)
## Overview 

chemcalculator is a python package useful for chemistry for the purpose of calculating chemical formular mass in g/mol. The mole allows scientists to calculate the number of elementary entities (usually atoms or molecules) in a certain mass of a given substance. The mass of one mole of a substance is equal to that substance’s molecular weight; as for instance, the mean molecular weight of water is 18.015 atomic mass units (amu), and so one mole of water weighs 18.015 grams. This property simplifies many chemical computations. This python package will be helpful to easily calculate the chemical formula mass, convert moles to grams and vice versa, and lastly calculate the percentage mass for the atomic nature of the elements in chemistry.

This package of basic chemistry calculations is meant to supplement an existing package, [ChemPy](https://github.com/bjodah/chempy), which already handles complex calculations for primarily physical/inorganic/analytical chemistry consisting of, but not limited to, the following:

- Solver for equilibria (including multiphase systems)
- Numerical integration routines for chemical kinetics (ODE solver front-end)
- Integrated rate expressions (and convenience fitting routines)
- Relations in Physical chemistry
- Debye-Hückel expressions
- Arrhenius equation
- Einstein-Smoluchowski equation
- Properties, such as : water density as function of temperature, water permittivity as function of temperature and pressure, and water diffusivity as function of temperature

## Functions

This package contains three functions. Each function will have it's own required and optional arguments.

1. `compute_mass`: Calculate the mass of the atoms or chemical formula for the input chemical formula.
2. `moles_grams_converter`: Convert moles to grams and convert grams to moles.
3. `percent_mass`: Calculate percentage mass for the desired atom or molecule.

## Installation

```bash
$ pip install chemcalculator
```

## Usage

`chemcalculator` can be used as follows:
```bash
from chemcalculator.chemcalculator import compute_mass
compute_mass("H2O")
```
```bash
from chemcalculator.chemcalculator import moles_grams_converter
moles_grams_converter("H2O", 0.05555, "moles")
```
```bash
from chemcalculator.chemcalculator import percent_mass
percent_mass("H2O", "O")
```

## Contributors
### Development Lead

|Contributor Name     | GitHub Username|
|---------------------|-----------|
|Kingslin Lv | [Kingslin0810](https://github.com/Kingslin0810)|
|Joyce Wang      | [jo4356](https://github.com/jo4356)     |
|Allyson Stoll       | [datallurgy](https://github.com/datallurgy) |

We welcome and recognize all contributions. Please find the guide for contribution in [Contributing Document](https://github.com/UBC-MDS/chemcalculator/blob/main/CONTRIBUTING.md).

## License

`chemcalculator` was created by Joyce Wang, Kingslin Lv, Allyson Stoll. It is licensed under the terms of the MIT license.

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
