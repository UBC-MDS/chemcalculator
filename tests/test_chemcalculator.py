
from chemcalculator.chemcalculator import compute_mass
from chemcalculator.chemcalculator import moles_grams_converter
from chemcalculator.chemcalculator import percent_mass
import pytest

def test_compute_mass():
    """
    Test the compute_mass function for correct output.
    """
    assert compute_mass('H2O') == pytest.approx(18.013, rel = 1e-3), \
    'compute_mass is not calculated properly (H2O).'
    
    assert compute_mass('C12H22O11') == pytest.approx(342.275, rel = 1e-3), \
    'compute_mass is not calculated properly (C12H22O11).'
    
    assert compute_mass('Al2(SO4)3') == pytest.approx(342.147, rel = 1e-3), \
    'compute_mass is not calculated properly (Al2(SO4)3).'
    
    assert compute_mass('(NH4)HS') == pytest.approx(51.107, rel = 1e-3), \
    'compute_mass is not calculated properly ((NH4)HS).'
    
def test_compute_mass_error():
    """
    Check that error is raised when input is invalid.
    """
    with pytest.raises(TypeError):
        compute_mass(['H2O'])
        
    with pytest.raises(ValueError):
        compute_mass('CuSO4-5H2O')    

    with pytest.raises(ValueError):
        compute_mass('naOH')
    
    with pytest.raises(ValueError):
        compute_mass('(nH4)HS')
        
    with pytest.raises(ValueError):
        compute_mass('NaaaaaaaaOH')
        
def test_moles_grams_converter():
    """
    Test the moles_grams_converter function for correct output
    """
    assert moles_grams_converter("H2O", 18.01528, "grams") == pytest.approx(1, rel=1e-3)
    
    assert moles_grams_converter("H2O", 1, "moles") == pytest.approx(18.015, rel=1e-3)

def test_moles_grams_converter_error():
    """
    Check that error is raised when input is invalid.
    """
    with pytest.raises(TypeError):
        moles_grams_converter('H2O', 1, 'tons')
        
    with pytest.raises(TypeError):
        moles_grams_converter(['H2O'], 1, 'moles')
        
    with pytest.raises(ValueError):
        moles_grams_converter('CuSO4-5H2O', 1, 'moles')    

    with pytest.raises(ValueError):
        moles_grams_converter('naOH', 1, 'moles')
    
    with pytest.raises(ValueError):
        moles_grams_converter('(nH4)HS', 1, 'moles')
        
    with pytest.raises(ValueError):
        moles_grams_converter('NaaaaaaaaOH', 1, 'moles')

def test_percent_mass():
    """
    Test the percent_mass function for correct output
    """
    assert percent_mass("H2O", "O") == pytest.approx(88.819, rel=1e-3), \
    "precent_mass is not calculated correctly (H2O, O)"
    
    assert percent_mass("H2O", "H") == pytest.approx(5.59, rel=1e-3), \
    "precent_mass is not calculated correctly (H2O, H)"

    assert percent_mass("H2O", "H2") == pytest.approx(11.181, rel=1e-3), \
    "precent_mass is not calculated correctly (H2O, H2)"

    assert percent_mass("NaOH", "OH") == pytest.approx(42.519, rel=1e-3), \
    "precent_mass is not calculated correctly (NaOH, OH)"

    assert percent_mass("H2SO4", "SO4") == pytest.approx(97.946, rel=1e-3), \
    "precent_mass is not calculated correctly (H2SO4, SO4)"

    assert percent_mass("H2SO4", "HSO4") == pytest.approx(98.973, rel=1e-3), \
    "precent_mass is not calculated correctly (H2SO4, HSO4)"

    assert percent_mass("Na(H2SO4)3", "NaH2SO4") == pytest.approx(38.165, rel=1e-3), \
    "precent_mass is not calculated correctly (Na(H2SO4)3, NaH2SO4)"


def test_percent_mass_error():
    """Check that error is raised when input is incorrect"""
    with pytest.raises(ValueError):
        percent_mass("H2SO4", "NaSO4")
    with pytest.raises(ValueError):
        percent_mass("H2SO4", "Al")
    with pytest.raises(ValueError):
        percent_mass("H2SO4", "H2SO4C5")
    with pytest.raises(ValueError):
        percent_mass("H2SO4", "H3")
    with pytest.raises(ValueError):
        percent_mass("H2SO4", "H3S5")
    with pytest.raises(ValueError):
        percent_mass(".", "H2O")
    with pytest.raises(ValueError):
        percent_mass("NaOH", "sss")
    with pytest.raises(TypeError):
        percent_mass(3, "O")

        
