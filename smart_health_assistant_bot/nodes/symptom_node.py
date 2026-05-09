from logic.health_logic import get_symptom_advice

def symptom_node(state):
    if state.get("is_finished") and state.get("symptom"):
        s_advice = get_symptom_advice(state["symptom"])
        return {"advice": f"{state['advice']}\n\nSymptom Note: {s_advice}"}
    return {}
