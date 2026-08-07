# ⚙️ AI Workflow Engine with Pydantic

A type-safe, modular workflow engine for building reliable AI applications — built from the ground up with Python + Pydantic.

AI systems are not just about sending a prompt to an LLM and receiving an answer.

A reliable AI application needs to understand a request, create a plan, execute the right action, validate the result, and return a structured response.

This project explores how to build that foundation without LangChain, LangGraph, or other agent frameworks.

## 🧠 What is this project?

The AI Workflow Engine is a lightweight workflow system where every stage communicates through strongly typed Pydantic models.

&emsp;&emsp;&emsp;User Request\
&emsp;&emsp;&emsp;&emsp; &emsp;│\
&emsp;&emsp;&emsp;&emsp;&emsp;▼\
&emsp;&emsp;&emsp;Parser Node\
&emsp;&emsp;&emsp;&emsp; &emsp;│\
&emsp;&emsp;&emsp;&emsp;&emsp;▼\
&emsp;&emsp;&emsp;Planner Node\
&emsp;&emsp;&emsp;&emsp; &emsp;│\
&emsp;&emsp;&emsp;&emsp;&emsp;▼\
&emsp;&emsp;&emsp;Workflow Task\
&emsp;&emsp;&emsp;&emsp; &emsp;│\
&emsp;&emsp;&emsp;&emsp;&emsp;▼\
&emsp;&emsp;&emsp;Executor Node\
&emsp;&emsp;&emsp;&emsp; &emsp;│\
&emsp;&emsp;&emsp;&emsp;&emsp;▼\
┌──────────────┐\
│&emsp;&emsp;Tool Registry&emsp;&ensp;&emsp;│\
└──────┬───────┘\
&emsp;&ensp;&emsp;&emsp; &emsp;&ensp;|\
   ┌──────┼──────┐\
▼&emsp;&emsp;&emsp;&emsp;▼&emsp;       &emsp;&emsp;&emsp;▼\
 Answer Summarize Search\
   Tool &emsp;&ensp;   Tool  &emsp; &emsp; Tool\
   └──────┬──────┘\
&emsp;&emsp;&emsp;&emsp;&emsp;▼\
&emsp;&emsp;&emsp;Execution Result\
&emsp;&emsp;&emsp;&emsp; &emsp;│\
&emsp;&emsp;&emsp;&emsp;&emsp;▼\
&emsp;&emsp;&emsp;Validator Node\
&emsp;&emsp;&emsp;&emsp; &emsp;│\
&emsp;&emsp;&emsp;&emsp;&emsp;▼\
&emsp;&emsp;&emsp;Final Response

The project is intentionally being built incrementally, starting with pure Python and Pydantic before introducing an LLM.

## 🎯 Why build this?

The goal is not to create another chatbot.

The goal is to understand the engineering underneath an AI agent:

* How structured data moves through an AI system
* How different components communicate
* How tasks are represented
* How tools are selected and executed
* How validation prevents bad data
* How workflows can be made modular and extensible

This project is also a foundation for eventually building a pure-Python AI agent without depending on an agent framework.
