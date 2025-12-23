from src.graph_state.state import GraphState
from typing import Any, Dict
from  src.create_vectorstore.create_vectorstore import initialize_retriever

def retrieve(state: GraphState) -> Dict[str, Any]:
    retriever = initialize_retriever()
    print("---RETRIEVE---")
    retrieved_docs = retriever.invoke(state["query"])
    print(f"Retrieved {len(retrieved_docs)} documents.")
    return {"documents": retrieved_docs}   
