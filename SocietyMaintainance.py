# Expert System for Society Maintenance Issues

# Mock inputs: simulate system or admin input
day = "Monday"
water_tank_cleaning = True
water_pump_failure = False
lights_not_working = True
bulb_fused = False
electricity_maintenance = True

def explain_utility_issue(day):
    reasons = {}

    # Water supply rules
    if day == "Monday" and water_tank_cleaning:
        reasons["water"] = "No water due to scheduled water tank cleaning."
    elif water_pump_failure:
        reasons["water"] = "No water due to a pump failure."

    # Light rules
    if lights_not_working and bulb_fused:
        reasons["lights"] = "Lights not working due to fused bulb in the common passage."
    elif lights_not_working and electricity_maintenance:
        reasons["lights"] = "Lights not working due to ongoing electricity maintenance."

    return reasons

# Ask the system for explanation
issues = explain_utility_issue(day)

# Display output
if "water" in issues:
    print("Water Issue:", issues["water"])
else:
    print("Water Supply: Working normally.")

if "lights" in issues:
    print("Light Issue:", issues["lights"])
else:
    print("Lights: Working normally.")
