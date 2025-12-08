# Multi-Agent Systems with CrewAI

This repository explores building multi-agent systems using **CrewAI**. It documents lessons learned while working with agents and multi-agent frameworks.  

## What is Agentic Automation?

Agentic automation refers to using intelligent agents to handle tasks where inputs, transformations, and outputs are **fuzzy or probabilistic**. For example:

- Inputs may be strings, but their actual type could be text, tabular data, or Markdown.  
- Transformations performed by the agent may be flexible or context-dependent.  
- Outputs are not deterministic—they vary based on the agent’s reasoning and interactions.  

Agentic automation allows systems to handle ambiguity and make decisions more autonomously.

## What is an Agent?

Without agents, interacting with large language models (LLMs) is often **recursive**: you repeatedly prompt the model, and improvements require human intervention.  

An **agent** solves this by:  

- Engaging in an **inner reasoning process**, iteratively improving its responses.  
- Asking its own questions when needed.  
- Interacting with **external tools** to complete tasks beyond text generation.  

Agents essentially allow LLMs to act more autonomously while still producing high-quality results.

## What is a Multi-Agent System?

A **multi-agent system** extends the agent concept by coordinating multiple agents to solve complex tasks. In this setup:  

- One agent can assign tasks to another.  
- Agents work collectively, leveraging specialized skills to achieve better outcomes.  

### Benefits of Multiple Agents

- **Specialization:** Each agent can focus on a single task, e.g., a researcher agent or a writer agent.  
- **Diverse Capabilities:** Different agents can run on different LLMs, including fine-tuned models optimized for specific tasks.  
- **Scalability:** Complex tasks can be divided among agents, allowing for parallel processing and collaboration.  

## SDK for Multi-Agent Systems: CrewAI

**CrewAI** provides the tools to build and deploy multi-agent systems efficiently. Key features include:  

- **Framework and Platform:** Breaks down complex agentic concepts into manageable structures.  
- **Patterns for Collaboration:** Provides patterns to connect agents and orchestrate multi-agent workflows.  
- **Tools and Skills:** Ships with pre-built tools and skills that agents can use out of the box.  
- **Production-Ready:** Offers a platform for bringing agents into production environments.  

## Core Building Blocks

When working with CrewAI, three main components form the foundation of multi-agent systems:  

1. **Agents** – Autonomous entities capable of reasoning and acting.  
2. **Tasks** – Work items assigned to agents.  
3. **Crews** – Groups of agents collaborating to achieve a goal.  

## Additional Best Practices

- **Agents perform better when role-playing.**  
- **Focus on goals and expectations.**  
- **One agent can handle multiple tasks.**  
- **Tasks and agents should be granular.**  
- **Tasks can be executed in different ways.**  
- **It's easy to create multi-agent systems with CrewAI.**  