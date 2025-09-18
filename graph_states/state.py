from typing import TypedDict
from urllib import response


class GraphState(TypedDict):
    query: str
    response: str