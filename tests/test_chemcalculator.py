from chemcalculator.chemcalculator import compute_mass
from chemcalculator.chemcalculator import moles_grams_converter
from chemcalculator.chemcalculator import percent_mass

def test_compute_mass():
    """
    Test the compute_mass function for correct output.
    """
    assert compute_mass('H2O') == pytest.approx(18.013, rel = 1e-3)
    
    assert compute_mass('C12H22O11') == pytest.approx(342.275, rel = 1e-3)
    
    assert compute_mass('Al2(SO4)3') == pytest.approx(342.147, rel = 1e-3)
    
    assert compute_mass('(NH4)HS') == pytest.approx(47.079, rel = 1e-3)
    
    with pytest.raises(TypeError):
        compute_mass(['H2O'])
        
    with pytest.raises(ValueError):
        compute_mass('CuSO4-5H2O')    

    with pytest.raises(ValueError):
        compute_mass('naOH')
    
    with pytest.raises(ValueError):
        compute_mass('(nH4)HS')
        
def test_moles_grams_converter():
    """
    Test the moles_grams_converter function for correct output
    """
    assert moles_grams_converter("H2O", 18.01528, "grams") == pytest.approx(1, rel=1e-3)
    
    assert moles_grams_converter("H2O", 1, "moles") == pytest.approx(18.015, rel=1e-3)
    
    with pytest.raises(TypeError):
        moles_grams_converter("H2O", 1, "tons")

def test_percent_mass():
    """
    Test the percent_mass function for correct output
    """
    assert percent_mass("H2O", "O") == pytest.approx(88.79, rel=1e-3)
    
    assert percent_mass("H2O", "H") == pytest.approx(5.6048, rel=1e-3)

    assert percent_mass("H2O", "H2") == pytest.approx(11.209, rel=1e-3)

    assert percent_mass("NaOH", "OH") == pytest.approx(42.525, rel=1e-3)

    assert percent_mass("H2SO4", "SO4") == pytest.approx(97.9404, rel=1e-3)

    assert percent_mass("H2SO4", "HSO4") == pytest.approx(98.9702, rel=1e-3)
    
