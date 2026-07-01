# Developer Query Agent

An AI agent built using Google Antigravity, Developer Knowledge MCP Server, and Agent Skills.

## Problem
Developers waste time searching through scattered documentation to find accurate, grounded answers to technical questions.

## Solution
This agent uses Google's Developer Knowledge MCP server to provide grounded, accurate answers to technical queries — directly inside the Antigravity IDE.

## Architecture
- **Antigravity CLI** — agentic IDE for running the agent
- **Developer Knowledge MCP** — provides grounded answers from Google's official documentation
- **Agent Skills** — custom `answer-formatter` skill for clean, structured responses

## Course Concepts Used
1. MCP Server (Developer Knowledge API)
2. Antigravity (agentic IDE)
3. Agent Skills (answer-formatter)

## Setup Instructions

### Prerequisites
- Google Antigravity installed
- Developer Knowledge API enabled
- API key created and configured in `~/.gemini/config/mcp_config.json`

### Installation
1. Clone this repo:
   git clone https://github.com/poddarvivek1010-dot/developer-query-agent.git

2. Run the agent:
   python agent.py

## Demo
Watch the demo video: [YouTube Link]

## Author
Vivek Kumar# developer-query-agent
AI agent using Antigravity, MCP and Agent Skills
