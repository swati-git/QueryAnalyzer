from typing import TypedDict, List


class GraphState(TypedDict):
    query: str
    llm_generated_response: str
    documents : List[str]
    grade: bool