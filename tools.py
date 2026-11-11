from datetime import datetime

def get_current_time():
    """Returns the current time as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

TOOLS= [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "ONLY call this when the user explicitly asks for the current time.",
            "parameters": {"type": "object", "properties": {}}
        }
    }
]

function_name_to_function ={
    "get_current_time": get_current_time
}