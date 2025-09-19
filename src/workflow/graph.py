from langgraph.graph import StateGraph
from langgraph.constants import  END
from src.graph_state.state import GraphState
from src.chains.query_router import query_router, QueryRouter

def route_question(state: GraphState) -> str:
    print("---ROUTE QUESTION---")
    source: QueryRouter = query_router.invoke({"question": state["query"]})
    return "WEBSEARCH" if source.datasource == "WEBSEARCH" else "RETRIEVE"


workflow = StateGraph(GraphState)

workflow.set_conditional_entry_point(
    route_question,
    {
        "WEBSEARCH": "WEBSEARCH",
        "RETRIEVE": "RETRIEVE",
    },
)

application = workflow.compile()

application.get_graph().draw_mermaid_png(output_file_path="graph.png")



