from langgraph.graph import StateGraph
from langgraph.constants import  END
from src.graph_state.state import GraphState
from src.chains.query_router import query_router, QueryRouter
from src.graph_nodes.web_search import web_search
from src.graph_nodes.retrieve import retrieve

def route_query(state: GraphState) -> str:
    print("---ROUTE QUESTION---")
    source: QueryRouter = query_router.invoke({"query": state["query"]})
    return "WEBSEARCH" if source.source_answer_from == "WEBSEARCH" else "RETRIEVE"

workflow = StateGraph(GraphState)

workflow.add_node("WEBSEARCH", web_search)
workflow.add_node("RETRIEVE", retrieve)


workflow.set_conditional_entry_point(
    route_query,
    {
        "WEBSEARCH": "WEBSEARCH",
        "RETRIEVE": "RETRIEVE",
    },
)

application = workflow.compile()

application.get_graph().draw_mermaid_png(output_file_path="graph.png")



