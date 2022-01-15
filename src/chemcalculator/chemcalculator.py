from multiprocessing import Condition


def compute_mass(chemical):
    """Computes the molar mass of the given chemical compound.

    Parameters
    ----------
    chemical : string
        The molecular formula of the given chemical compound given as a string.

    Returns
    -------
    float
        The molar mass of the given formula in g/mol.

    Raises
    ------
    ValueError
        String contains characters that are not allowed.
    ValueError
        String starts with lowercase letter.

    Examples
    --------
    >>> compute_mass("H2O")
    18.01528

    >>> compute_mass("C12H22O11")
    342.3

    >>> compute_mass("Al2(SO4)3")
    342.15
    """

def moles_grams_converter(formula, mass, converter):
    """
    Converts moles to grams or grams to moles

    Parameters
    ----------
    formula: string
        the checmical formula for the conversion
    mass: float
        a float for the mass of molecule that needs to convert in grams or moles
    converter: string
        indicates to convert to either moles or grams

    Returns
    -------
    float
        a float that is converted in either moles or grams

    Examples
    --------
    >>> moles_grams_converter("H2O", 0.05555, moles)
    1.000748804
    >>> moles_grams_converter("H2O", 18.01528, grams)
    1
    """

def percent_mass(compound, element):
    """
    Calculates the percentage mass of an element (or compound) in a compound

    Parameters
    ----------
    compound : string
        the chemical formula of the full compound
    element : string
        the chemical formula of the element or compound of interest

    Returns
    -------
    float
        the percentage mass of the element or compound of interest
    
    Examples
    --------
    >>> percent_mass("H2O", "O")
    88.79
    
    >>> percent_mass("H2O", "H")
    11.19

    >>> percent_mass("NaOH", "OH")
    42.52
    """
    
    perc_mass = compute_mass(element)/compute_mass(compound)*100
    print(f"The percentage mass of {element} in {compound} is: ")
    return perc_mass