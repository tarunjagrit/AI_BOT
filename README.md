# AI Assistant & Agent

A personal project where I'm building an AI assistant using Python and local LLMs, and gradually turning it into an AI agent that can use tools and perform tasks.

I'm using Ollama to run models locally and an OpenAI-compatible API to interact with them. The project started with a simple assistant and is growing to include conversation history, tool calling, multi-step tasks, streaming responses, and document search using RAG.


## What I'm building

The idea is to go beyond sending a prompt to an LLM and printing its response. I want to build an assistant that can remember the conversation, decide when it needs a tool, use that tool, and use the result to answer the user.

### Current features

- Python-based AI assistant
- Local LLM integration using Ollama
- OpenAI-compatible API client
- Configurable model and API endpoint
- Environment variables for configuration

### What's next

- Add conversation history so the assistant can follow a conversation across multiple messages.
- Use system prompts to control the assistant's behavior and personality.
- Give the assistant tools it can call, such as a weather API.
- Let it use multiple tools to complete a task instead of stopping after one call.
- Add streaming so responses appear as they're generated.
- Improve debugging and error handling.
- Build a RAG pipeline so the assistant can search documents and answer questions using their content.

## Technologies and Concepts

- **Python & Ollama:** Building and running LLM-powered applications.
- **LLM APIs & Prompt Engineering:** Model interaction, system prompts, and response generation.
- **Agent Tooling:** Function calling, external API integrations, and multi-step execution.
- **LangGraph:** Stateful agent workflows and execution control.
- **Model Context Protocol (MCP):** Connecting AI applications to external tools and data sources.
- **CrewAI:** Experimenting with collaborative multi-agent workflows.
- **RAG:** Document embeddings, semantic search, and context-aware responses.

The project is being developed incrementally, with each technology added when it has a concrete role in the implementation.


## How it works

The assistant sends the user's message to a language model and returns its response. As I add agent capabilities, the workflow will expand: the model will be able to request a tool, the application will execute it, and the result will be passed back to the model to generate an answer.

For RAG, I'll add a separate workflow to process documents, find relevant information, and provide that information to the model as context.


## Project Structure


AI_BOT/
├── simple_ai_assist.py
├── .gitignore
├── README.md
└── requirements.txt


The structure will change as I add tools, tests, and document-retrieval features.

## Author

Tarun Jagrit
