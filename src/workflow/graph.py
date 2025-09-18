from langgraph.graph import StateGraph
from langgraph.constants import START, END
from src.graph_nodes.query_analyzer_node import query_analyzer_node
from src.graph_state.state import GraphState


workflow = StateGraph(GraphState)

workflow.add_node("QueryAnalyzer", query_analyzer_node)

workflow.add_edge(START, "QueryAnalyzer")
workflow.add_edge("QueryAnalyzer", END)

application = workflow.compile()

application.get_graph().draw_mermaid_png(output_file_path="graph.png")



