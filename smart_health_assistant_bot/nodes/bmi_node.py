from logic.health_logic import calculate_bmi_data

def bmi_node(state):
    if state.get("is_finished"):
        bmi, cat, tip = calculate_bmi_data(float(state["weight"]), float(state["height"]))
        return {"bmi_score": bmi, "bmi_cat": cat, "advice": tip}
    return {}