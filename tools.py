from datetime import datetime
from zoneinfo import ZoneInfo
import requests

#GETS the current date and time. Uses the computer's local timezone if none is given.
def get_current_time(timezone=None):
    """Current date and time. Uses the computer's local timezone if none is given."""
    if timezone is None:
        now = datetime.now().astimezone()
    else:
        try:
            now = datetime.now(ZoneInfo(timezone))
        except Exception:
            return f"Error: unknown timezone '{timezone}'. Use names like 'Asia/Kolkata'."
    return now.strftime("%Y-%m-%d %H:%M:%S (%A) %Z")

def get_weather(location):
    url = f"https://wttr.in/{location}?format=3"
    response = requests.get(url, timeout=10)

    return response.text



TOOLS= [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current date and time. Use only when the user asks for the time or date. If the user asks for the time without naming a place, call get_current_time "
            "with no arguments. Do not ask which timezone.",
            "parameters": {"type": "object", 
                            "properties": {
                                "timezone": {"type": "string", "description": "The timezone to get the current time for. Use names like 'Asia/Kolkata' or 'America/New_York'. If not provided, the computer's local timezone will be used."}
                            }}
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "this tool return the current weather for a given location.",
            "parameters": {"type": "object", 
                            "properties": {
                                "location": {"type": "string", "description": "The location to get the weather for."} 
                            }}
        }
    }
    ]

function_name_to_function ={
    "get_current_time": get_current_time,
    "get_weather": get_weather
}