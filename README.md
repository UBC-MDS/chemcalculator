# chemcalculator


## Overview 

chemcalculator is a python package useful for chemistry for purpose of calculating chemical formular mass in g/mol. The mole allows scientists to calculate the number of elementary entities (usually atoms or molecules) in a certain mass of a given substance. Another property of Avogadro’s number is that the mass of one mole of a substance is equal to that substance’s molecular weight. For example, the mean molecular weight of water is 18.015 atomic mass units (amu), so one mole of water weighs 18.015 grams. This property simplifies many chemical computations. This python package will be helpful to easily calculate the chemical formula mass, convert moles to grams and vice versa, and lastly calculate the percentage mass for the atomic nature of the elements in chemistry.

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

1. Calculate the mass of the atoms or chemical formula for the input chemical formula.
2. Convert moles to grams and convert grams to moles.
3. Calculate percentage mass for the desired atom or molecule.

## Installation

```bash
$ pip install chemcalculator
```

## Usage

- TODO

## Contributors
### Development Lead

|Contributor Name     | GitHub Username|
|---------------------|-----------|
|Kingslin Lv | [Kingslin0810](https://github.com/Kingslin0810)|
|Joyce Wang      | [jo4356](https://github.com/jo4356)     |
|Allyson Stoll       | [datallurgy](https://github.com/datallurgy) |

We welcome and recognize all contributions. Please find the guide for contribution in [Contributing Document](https://github.com/UBC-MDS/chemcalculator/blob/main/CONTRIBUTING.md).

## License

`chemcalculator` was created by Joyce Wang, Kinslin Lv, Allyson Stoll. It is licensed under the terms of the MIT license.

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).