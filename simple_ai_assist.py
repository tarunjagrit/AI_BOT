from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url= os.getenv("BASE_URL"),
    api_key= os.getenv("API_KEY")
)
messages = []

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
        messages=messages
    )

    messages.append(
        {"role": "assistant",
         "content": response.choices[0].message.content
        }
    )
    print("Assistant response : "+response.choices[0].message.content)