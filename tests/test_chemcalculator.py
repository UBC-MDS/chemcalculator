from typing import Type
from chemcalculator.chemcalculator import percent_mass


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
    assert percent_mass("H2O", "O") == pytest.approx(88.819, rel=1e-3), \
    "precent_mass is not calculated correctly."
    
    assert percent_mass("H2O", "H") == pytest.approx(5.59, rel=1e-3), \
    "precent_mass is not calculated correctly."

    assert percent_mass("H2O", "H2") == pytest.approx(11.181, rel=1e-3), \
    "precent_mass is not calculated correctly."

    assert percent_mass("NaOH", "OH") == pytest.approx(42.519, rel=1e-3), \
    "precent_mass is not calculated correctly."

    assert percent_mass("H2SO4", "SO4") == pytest.approx(97.946, rel=1e-3), \
    "precent_mass is not calculated correctly."

    assert percent_mass("H2SO4", "HSO4") == pytest.approx(98.973, rel=1e-3), \
    "precent_mass is not calculated correctly."

    assert percent_mass("Na(H2SO4)3", "NaH2SO4") == pytest.approx(38.165, rel=1e-3), \
    "precent_mass is not calculated correctly."


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

        
