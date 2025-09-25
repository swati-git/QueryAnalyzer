from typing import Any, Dict
from src.chains.llm_repsonse_generation_chain import llm_answer
from src.graph_state.state import GraphState


def generate(state: GraphState) -> Dict[str, Any]:
    """Generate answer using documents and question."""
    print("---GENERATE---")
    question = state["query"]
    documents = state["documents"]
    llm_generated_response = llm_answer.invoke({"documents": documents, "query": question})
    return {"documents": documents, "query": question, "llm_generated_response": llm_generated_response}