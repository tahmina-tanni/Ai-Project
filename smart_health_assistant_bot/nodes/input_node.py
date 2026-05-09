from logic.health_logic import get_questions_list

def input_node(state):
    questions = get_questions_list()
    idx = state.get("current_idx", 0)
    
    # If we still have questions left
    if idx < len(questions):
        return {
            "next_question": questions[idx],
            "current_idx": idx,
            "is_finished": False
        }
    
    return {"is_finished": True}