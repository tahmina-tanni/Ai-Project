from logic.health_logic import generate_final_analysis

def response_node(state):
    if state.get("is_finished"):
        full_report = generate_final_analysis(state["responses"])
        return {"next_question": full_report}
    return {}