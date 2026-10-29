def calculate_solar_plan(bills: list[float], roof_area: float, grid_type: str) -> dict:
    
    average_bill = sum(bills) / len(bills)
    max_panels = (int(roof_area // 2.5))
    if grid_type == "220V":
        type_of_system = "Single-Phase Inverter"
    elif grid_type == "380V" :
        type_of_system = "Three-Phase Inverter"
    else:
        type_of_system = "Unknown"

    return {
        "average_bill": average_bill,
        "max_panels": max_panels,
        "recommended_inverter": type_of_system
    }
r=calculate_solar_plan([100, 150, 200], 50, "220V")
print(r)