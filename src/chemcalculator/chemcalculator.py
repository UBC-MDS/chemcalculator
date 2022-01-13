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