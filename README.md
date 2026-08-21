# Modular Intelligent Workflow Engine

A modular intelligent Python workflow engine designed to explore the software architecture behind intelligent applications.

The project models a complete request lifecycle:

Request → Understand → Plan → Execute → Validate → Respond

The implementation intentionally keeps the decision-making deterministic rather than introducing an LLM. The focus is on understanding the engineering structure around an intelligent system — data contracts, component responsibilities, task orchestration, tool execution, validation, configuration, logging, and error handling.


## Why This Project?

When building AI-powered applications, it is easy to focus immediately on models, agents, tools, and frameworks.

This project takes a step back.

Before introducing an AI layer, it explores how a request can move through a well-structured application:

- How is incoming data validated?
- How is intent represented?
- How are tasks created?
- How are tools selected?
- How are execution results represented and validated?
- How are failures handled?
- How do different components communicate?

The goal is to understand the system around intelligence before adding intelligence itself.


## Workflow

                   User Request
                        │
                        ▼
                ┌───────────────┐
                │    Parser     │
                │ Intent        │
                │ Classification│
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │    Planner    │
                │ Task Creation │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │   Executor    │
                │ Tool Selection│
                │ & Execution   │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │   Validator   │
                │ Result Check  │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │    Response   │
                └───────────────┘