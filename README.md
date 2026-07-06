# AI_Wealth_Advisor_MCP_LLM
An AI-powered Wealth Advisor application built to explore the Model Context Protocol (MCP) and how LLMs can interact with structured tools to generate financial advisor meeting notes.
The project demonstrates an MCP-based architecture where client data is retrieved through MCP tools, while an LLM is responsible only for analysis and recommendations.

# 🏦 AI Wealth Advisor (MCP + LLM)

An AI-powered Wealth Advisor application built to explore the **Model Context Protocol (MCP)** and how Large Language Models (LLMs) can interact with structured tools to generate financial advisor meeting notes.

The project demonstrates an MCP-based architecture where client data is retrieved through MCP tools, while an LLM is responsible only for analysis and recommendations.

---

## 🚀 Project Overview

Financial advisors often need to prepare before meeting clients. Instead of manually reviewing client information, this application generates concise advisor preparation notes using structured client data.

The project focuses on learning and implementing the **Model Context Protocol (MCP)** rather than building a production-ready financial advisory system.

---

## ✨ Features

* View client profile
* Display portfolio information
* Retrieve risk assessment through MCP tools
* Generate AI-powered advisor preparation notes using an LLM
* Simple Streamlit user interface
* Modular architecture separating data, tools, MCP, orchestration, and AI reasoning

---

## 🏗️ Architecture

```text
Streamlit UI
      │
      ▼
agent.py
      │
      ▼
executor.py
      │
      ▼
MCP Client
      │
      ▼
MCP Server
      │
      ▼
Tools
      │
      ▼
Mock Client Data
      │
      ▼
LLM (Ollama / Llama 3.2)
      │
      ▼
Advisor Preparation Notes
```

---

## 📂 Project Structure

```text
wealth_adv_agent/
│
├── app.py               # Streamlit user interface
├── agent.py             # Orchestrates the application workflow
├── executor.py          # Executes MCP tool calls
├── advisor.py           # Generates AI recommendations using Ollama
├── planner.py           # Tool selection logic (can be extended)
├── mcp_client.py        # MCP client implementation
├── mcp_server.py        # MCP server exposing tools
├── tools.py             # Business logic for retrieving client data
├── data.py              # Mock client dataset
└── requirements.txt
```

---

## 🔄 Workflow

1. User selects a client from the Streamlit interface.
2. The Agent coordinates the workflow.
3. The Executor invokes the appropriate MCP tool.
4. The MCP Client communicates with the MCP Server.
5. The MCP Server executes the requested tool.
6. Structured client data is returned.
7. The LLM generates advisor preparation notes based only on the retrieved data.
8. The final recommendations are displayed in the UI.

---

## 🧩 MCP Tools

The application exposes three MCP tools:

| Tool              | Purpose                            |
| ----------------- | ---------------------------------- |
| `client_profile`  | Returns client profile information |
| `portfolio`       | Returns portfolio details          |
| `risk_assessment` | Returns client's risk assessment   |

---

## 🤖 AI Component

The project uses **Ollama** with the **Llama 3.2** model.

The LLM is used only for reasoning and generating advisor notes.

It does **not** directly access client data. All structured information is retrieved through MCP tools.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Model Context Protocol (MCP)
* Ollama
* Llama 3.2
* AsyncIO

---

## 📚 Learning Objectives

This project was created to understand:

* Model Context Protocol (MCP)
* MCP Client–Server communication
* Tool-based AI architectures
* Agent orchestration
* Separation of business logic from LLM reasoning
* Building AI applications with Streamlit

---

## ⚠️ Disclaimer

This project is intended for educational purposes only.

Client data is mock data and does not represent real individuals.

The AI-generated advisor notes are demonstrations of LLM capabilities and should not be considered financial advice.

---

## 🚀 Future Improvements

* Support multiple MCP servers
* Add transaction history tool
* Portfolio performance analytics
* Live market data integration
* Retrieval-Augmented Generation (RAG)
* Authentication and user management
* Persistent database instead of mock data
* Docker deployment

---

## 📸 Demo

*Add screenshots or a short demo GIF here.*

---

## 👩‍💻 Author

Built as a learning project to explore **Model Context Protocol (MCP)**, AI agents, and LLM-powered financial advisory workflows.
