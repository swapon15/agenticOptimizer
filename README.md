
<img width="816" height="689" alt="Screenshot 2026-10-24 at 10 49 10 AM" src="https://github.com/user-attachments/assets/44acd3c1-3e9f-41d8-9a91-c4cf67af849d" />



# Building a Reusable Engineering Optimization Agent

**An incremental engineering project exploring genetic algorithms, MATLAB optimization, MCP-based integration, and AI agent orchestration.**

## Project Overview

This project explores how to build a reusable engineering optimization system that combines mathematical optimization with AI agent capabilities.

The first application is **EvolveMySketch**: an interactive creative optimization application where users provide an initial sketch, select preferred design variations, and iteratively evolve the design using a Genetic Algorithm (GA).

Rather than building a generic AI image generator, the goal is to demonstrate how evolutionary optimization can explore a parameterized design space while keeping humans in control of the design process.

## The Problem

Imagine sketching a flower and wanting to explore different designs.

You might want to change:

- Number of petals
- Petal size and shape
- Color
- Petal arrangement
- Center size
- Leaf dimensions

Instead of manually adjusting each feature, a Genetic Algorithm can generate candidate designs, evaluate them, and evolve subsequent generations based on human preferences.

The user becomes part of the optimization loop by selecting preferred candidates.

## Development Strategy

Development follows two incremental stages.

### Stage 1: Deterministic Optimization (Without LLM)

Establish a working optimization system before introducing AI.

**Architecture:**

User → Python UI → Python Orchestration → Python MCP Client → MATLAB MCP Server → MATLAB Global Optimization Toolbox → Genetic Algorithm

Key capabilities:

- Parameterized sketch representation
- Candidate design generation
- Genetic Algorithm implementation using MATLAB `ga`
- Human-guided candidate selection
- Fitness evaluation and convergence tracking
- Visualization of evolutionary progress

The objective is to validate the optimization workflow independently of an LLM.

### Stage 2: Agentic Optimization (With LLM)

Introduce an AI agent on top of the validated optimization infrastructure.

Additional capabilities:

- Understand natural-language design requests.
- Translate user preferences into optimization parameters and constraints.
- Recommend optimization configurations.
- Invoke MATLAB optimization capabilities through MCP.
- Explain optimization results.
- Incorporate human feedback into subsequent optimization cycles.

The LLM is responsible for reasoning and orchestration. MATLAB remains responsible for numerical optimization.

## Technology Stack

| Component | Technology |
|---|---|
| Application and orchestration | Python |
| Optimization engine | MATLAB |
| Optimization algorithms | MATLAB Global Optimization Toolbox |
| Integration | MATLAB MCP Server |
| MCP client | Python MCP SDK |
| User interface | Streamlit |
| Image representation | SVG / parameterized geometry |
| AI agent | LLM-based agent (Stage 2) |

## Architectural Principles

1. Separate problem formulation from optimization execution.
2. Keep the optimization engine independent of the LLM.
3. Use MCP as the integration boundary between Python and MATLAB.
4. Make optimization experiments reproducible.
5. Keep humans involved in preference-based design decisions.
6. Build modular components that can support additional optimization problems.

## Roadmap

- [ ] Define the initial sketch representation.
- [ ] Define optimization variables and constraints.
- [ ] Implement the MATLAB Genetic Algorithm.
- [ ] Integrate Python with MATLAB through MCP.
- [ ] Build candidate rendering and visualization.
- [ ] Implement human-guided selection.
- [ ] Validate evolutionary behavior.
- [ ] Introduce the LLM-powered agent.
- [ ] Generalize the framework to additional engineering optimization problems.

## Project Philosophy

**Optimization first. AI orchestration second.**

The project aims to demonstrate that reliable AI-powered engineering workflows should be built on top of independently validated computational systems.

This is an ongoing engineering project. Architecture, implementation decisions, experiments, and lessons learned will be documented incrementally.

