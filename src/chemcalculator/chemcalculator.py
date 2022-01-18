import re
import pandas as pd
from multiprocessing import Condition
from collections import Counter

# read in periodic table and create dictionary
periodic_table = pd.read_csv('Periodic Table of Elements.csv', skiprows = 2)
periodic_table.set_index('Symbol', drop=True, inplace=True)
periodic_table = periodic_table.to_dict(orient="index")

# gather atomic mass from the periodic table
periodic_table_mass={}
for element in periodic_table:
    periodic_table_mass[element] = periodic_table[element]['AtomicMass']

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
        Entered value is not a string.
    ValueError
        String contains characters that are not allowed.
    ValueError
        String or subcomponent starts with lowercase letter.

    Examples
    --------
    >>> compute_mass("H2O")
    18.01528

    >>> compute_mass("C12H22O11")
    342.3

    >>> compute_mass("Al2(SO4)3")
    342.15
    """
    allowed_characters = r'[^\(\)A-Za-z0-9]'
    not_allowed_lowercase = r'^[a-z]|\([a-z]'
    
    if isinstance(chemical, str): break
    else:
        raise ValueError:
            print('Entered value is not a string')
            
    if re.search(allowed_characters, chemical):
        raise ValueError:
            print('String contains characters that are not allowed.')
    else: break
    
    if re.search(not_allowed_lowercase, chemical):
        raise ValueError:
            print('String or subcomponent starts with a lowercase letter.')
    else: break
    
    primary_list = []
    temp_primary_list = []
    compound_list = []
    simplified_compounds_list = []
    raw_element_list = []
    
    def decompose_elements(string):
        temp_list = re.findall(r'(\(.*?\)\d+)|([A-Z][^A-Z|(]*)', string)
        temp_list = [item for sublist in temp_list for item in sublist]
        temp_list = list(filter(None, temp_list))
        return temp_list
    
    # split major components of the given chemical
    primary_list = decompose_elements(chemical)
    
    # separate compounds from simple elements
    for component in primary_list:
        if re.match('\(.*?\)\d+', component):
            compound_list.append(element)
            primary_list.remove(element)
            
    # simplify the compounds
    for compound in compound_list:
        trim = re.findall('\)\d+', compound)
        length = len(trim[0])
        units = trim[0][1:]
        
        simplified_compound = compound[1:]
        simplified_compound = simplified_compound[:-length]
        
        for i in range(int(units)):
            simplified_compounds_list.append(simplified_compound)
    
    # decompose compounds
    for compound in simplified_compounds_list:
        temp_list = decompose_elements(compound)
        temp_primary_list = temp_primary_list + temp_list
    
    # merge inital list with decomposed compounds
    primary_list = primary_list + temp_primary_list
    
    # break down multiple atoms (e.g. Al2 = Al + Al)
    for element in primary_list:
        trim = re.findall('\d+', element)
        if trim:
            length = len(trim[0])
            units = trim[0]
            simplified_element = element[:-length]
            
        else:
            length = 0
            units = 1
            simplified_element = element
    
        for i in range(int(units)):
            raw_element_list.append(simplified_element) 
    
    # count and sum up all individual elements
    elements = pd.DataFrame.from_dict(Counter(raw_element_list), orient='index', columns = ["Counts"]).reset_index()
    elements = elements.rename(columns={"index": "Element"})
    
    # map atomic masses from periodic table and multiply by atomic counts
    elements['Mass'] = elements['Element'].map(periodic_table_mass) * elements['Counts']
    
    # sum and return mass
    return elements['Mass'].sum()

def moles_grams_converter(formula, mass, convert_to):
    """
    Converts between moles and grams depending on the conversion type provided

    Parameters
    ----------
    formula : string
        the checmical formula for the conversion
    mass : float
        the mass of molecule that needs to be converted (grams or moles)
    convert_to : string
        the type of conversion to be made to either "moles" or "grams"

    Returns
    -------
    float
        mass that is converted to either moles or grams

    Examples
    --------
    >>> moles_grams_converter("H2O", 0.05555, "moles")
    1.0007

    >>> moles_grams_converter("H2O", 18.01528, "grams")
    1.000
    """
    grams_per_mole = compute_mass()
    if convert_to == "grams":
        result = mass / grams_per_mole
    elif convert_to == "moles":
        result = mass * grams_per_mole
    else:
        raise Exception("Wrong arguments!")

    return round(result, 3)

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
    print(f"The percentage mass of {element} in {compound} is: {perc_mass} %")
    return perc_mass
