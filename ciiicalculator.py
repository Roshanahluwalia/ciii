def calculate_cii(deadweight, distance_travelled, fuel_consumed, co2_emissions):
    """
    Calculate the Carbon Intensity Index (CII) for a vessel.

    Args:
    - deadweight (float): The deadweight of the vessel in metric tons.
    - distance_travelled (float): The distance travelled by the vessel in nautical miles.
    - fuel_consumed (float): The amount of fuel consumed by the vessel in metric tons.
    - co2_emissions (float): The CO2 emissions from the vessel in metric tons.

    Returns:
    - cii (float): The Carbon Intensity Index (CII) for the vessel in grams CO2 per deadweight nautical mile (gCO2/dwt-nm).
    """
    # Calculate the deadweight nautical miles (dwt-nm) travelled by the vessel
    dwt_nm = deadweight * distance_travelled

    # Calculate the CII for the vessel in gCO2/dwt-nm
    cii = (co2_emissions / fuel_consumed) * (1 / dwt_nm) * 1000 * 1000

    return cii
