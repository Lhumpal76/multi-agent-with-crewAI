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

## What Makes a Good Agent?

### Role Playing
Taking on a clear role or persona pays off. When you point the model toward a certain kind of voice or behavior, it tends to stay on track and give the kind of answers you’re after.

### Focus
Context windows keep getting bigger, but cramming them full works against you. Too much clutter makes an agent lose important details and raises the odds of hallucinations. Know what the agent is trying to accomplish, and don’t expect one agent to handle every task under the sun.

### Tools
Folks often overload their agents with tools. That usually backfires—too many options make it harder for the agent to understand what to use and when. Pick tools with intention, not volume.

### Cooperation
Agents that can bounce ideas off one another, accept feedback, and hand off tasks end up stronger together. Good collaboration helps the whole system balance itself and produce steadier results.

### Guardrails
AI applications deal with fuzzy inputs and outputs, so they need gentle nudging rather than strict rules. Guardrails keep an agent pointed in the right direction without forcing it into rigid, deterministic answers. Most frameworks handle a lot of this for you, helping keep things consistent.

### Memory
A capable agent remembers what it has done and learns from it. In CrewAI, agents come with three types of memory:

- **Short-term memory:** Lives only during crew execution and task execution.  
- **Long-term memory:** Saved after an execution run; includes self-critique and lessons learned, helping the agent improve over time.  
- **Entity memory:** Tracks who and what is being discussed—people, organizations, places—during a run.

Memory keeps agents from starting fresh every time and lets them refine their behavior as they go.

## Interesting Excerpts
> "Having a dedicated final agent that serves as a quality-assurance layer makes a noticeable difference. That last pass—whether it’s on a blog post, a customer interaction, or anything else—tends to sharpen the output and smooth out mistakes. It’s worth adding a QA agent to any multi-agent setup you build. Systems that include one consistently outperform those that don’t."

## Mental Framework for Agent Creation
- **Think as a manager:** Consider the overall goal and the process to achieve it.  
- **Define roles:** What kind of people would you hire to accomplish this? Consider roles, backstories, and goals.

## Key Elements of Agent Tools
### What Makes a Great Tool
- **Versatile:** Able to accept a variety of request types, from fuzzy LLM inputs to strongly-typed external tool outputs. Should handle text, JSON, numbers, lists, and more.  
- **Fault-Tolerant:** Tools should fail gracefully when errors occur, returning exceptions to the agent for refinement. The system should self-heal and continue execution without breaking.  
- **Caching:** Prevent unnecessary requests by reusing cached responses. A smart caching layer can operate across agents, saving execution time and helping stay within API rate limits.

### Examples of Tools
- Search the internet  
- Scrape websites  
- Connect to databases  
- Call APIs  
- Send notifications  

CrewAI provides a variety of tools out of the box, and also supports all LangChain tools.


## Memory
Agent memory is a critical component of AI systems and is highly dependent on the application context. At its core, memory answers two questions:

1. What does the agent need to do?  
2. What information should it remember?

Memory in agents is typically divided into **short-term** and **long-term** types, each serving distinct purposes.

## Short-Term Memory
Short-term memory is transient and thread- or session-specific. It helps agents maintain context during ongoing interactions.

- **Conversational memory**: Keeps track of the current conversation using tools like LangChain checkpointers.  
- **Common techniques**:
  - Filtering messages (e.g., keeping the last N messages, including human and AI messages, excluding tool messages)  
  - Summarizing recent exchanges  
  - Maintaining chat history  
- **Implementation**: Often managed with a rolling buffer or context window.

## Long-Term Memory
Long-term memory persists across conversations and allows agents to retain knowledge over time.

- **Update strategies**:
  - **Hot path updates**: Application logic updates memory in real-time. This is transparent and immediate but can introduce latency and complexity.  
  - **Background updates**: Memory is updated asynchronously. Keeps application logic clean but may lag behind the most recent interactions.

- **Memory structures**:
  - **Instructions**: Guidelines the agent updates dynamically.  
  - **Profiles**: Key-value stores representing entities such as user profiles, updated over time. Can be injected into system messages.  
  - **Lists**: Collections of items relevant to the agent (e.g., favorites, preferences).  

- **Memory types**:
  - **Episodic memory**: Stores events, actions, and outcomes to inform future decisions.  
  - **Semantic memory**: Stores general knowledge, facts, and rules for reasoning. Unlike episodic memory, it is not event-specific.  
  - **Procedural memory**: Stores learned skills and action sequences, allowing the agent to perform tasks efficiently without explicit reasoning. Often trained via reinforcement learning.

---

This structure gives developers and system architects a clear understanding of how agent memory is designed, updated, and utilized within the system.
