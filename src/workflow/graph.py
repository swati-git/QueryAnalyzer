from langgraph.graph import StateGraph
from langgraph.constants import  END
from src.graph_state.state import GraphState
from src.chains.query_router import query_router, QueryRouter
from src.graph_nodes.web_search import web_search
from src.graph_nodes.retrieve import retrieve
from src.graph_nodes.grader import grader
from src.graph_nodes.generate_llm_answer import generate


workflow = StateGraph(GraphState)

workflow.add_node("WEBSEARCH", web_search)
workflow.add_node("RETRIEVE", retrieve)
workflow.add_node("GRADER", grader)
workflow.add_node("GENERATE_ANSWER", generate)

def route_query(state: GraphState) -> str:
    print("---ROUTE QUESTION---")

    source: QueryRouter = query_router.invoke({"query": state["query"]})
    print(f"Routed to source: {source.source}")
    
    return "WEBSEARCH" if source.source == "WEBSEARCH" else "RETRIEVE"

workflow.set_conditional_entry_point(
    route_query,
    {
        "WEBSEARCH": "WEBSEARCH",
        "RETRIEVE": "RETRIEVE",
    },
)
workflow.add_edge("WEBSEARCH", "GRADER")
workflow.add_edge("RETRIEVE", "GRADER")
workflow.add_edge("GRADER", "GENERATE_ANSWER")

application = workflow.compile()

#application.get_graph().draw_mermaid_png(output_file_path="graph.png")



