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