import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from src.workflow.graph import application

def main():  
    query = input("Type your query:")
    print(f"You asked: {query}")

    for output in application.stream({"query": query}):
        for key, value in output.items():
            result = value
                    
    if result:
        print(f"\nAnswer: {format_response(result)}")
    else:
        print("No response generated.")


def format_response(result):
    """Extract response from workflow result."""
    if isinstance(result, dict) and "generation" in result:
        return result["generation"]
    elif isinstance(result, dict) and "response" in result:
        return result["response"]
    else:
        return str(result)
    
if __name__ == "__main__":
    main()