from langgraph.graph import StateGraph, START, END
from graph.state import AgentState
from nodes.input_node import input_node
from nodes.response_node import response_node

def build_health_graph():
    builder = StateGraph(AgentState)
    builder.add_node("input_node", input_node)
    builder.add_node("response_node", response_node)

    builder.add_edge(START, "input_node")

    def router(state):
        return "response_node" if state.get("is_finished") else END

    builder.add_conditional_edges("input_node", router)
    builder.add_edge("response_node", END)
    
    return builder.compile()