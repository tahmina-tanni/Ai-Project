from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    # Tracking
    current_idx: int
    questions: List[str]
    responses: List[str]
    
    # Final Output
    next_question: str
    is_finished: bool
    report_data: str