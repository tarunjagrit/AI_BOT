import json
from openai import OpenAI
import os
from dotenv import load_dotenv
from tools import TOOLS, function_name_to_function
load_dotenv()

client = OpenAI(
    base_url= os.getenv("BASE_URL"),
    api_key= os.getenv("API_KEY")
)
messages = []

messages.append(
    {
        "role": "system",
        "content": "You are a helpful assistant. You will answer the questions asked by the user in a concise and clear manner in less than 20 words. If you don't know the answer, you will say 'I don't know'."
    }
)
while True:
    user_input = input("You: ")
    if(user_input.lower() == "exit" or user_input.lower() == "quit" or user_input.lower() == "bye"):
        break

    messages.append(
        {"role": "user",
         "content": user_input
        }
    )


    response = client.chat.completions.create(
        model= os.getenv("Model"),
        messages=messages,
        tools=TOOLS,
    )

    msg= response.choices[0].message
   
    if msg.tool_calls:
        messages.append(msg)

        for tool_call in msg.tool_calls:
            func_name= tool_call.function.name
            func_args= json.loads(tool_call.function.arguments)
    
            fn =function_name_to_function[func_name]
            result = fn(**func_args)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })
        #2nd call to the model after tool execution
        response = client.chat.completions.create(
            model= os.getenv("Model"),
            messages=messages,
            tools=TOOLS
        )
        msg= response.choices[0].message

    messages.append(
        {
            "role": "assistant",
            "content": msg.content
        }
    )

    print("Assistant: " + msg.content)