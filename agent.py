# Developer Query Agent
# Uses Google Antigravity + Developer Knowledge MCP + Agent Skills

QUERIES = [
    "Based on the Google Developer Knowledge, what is the best way to authenticate with Google APIs?",
    "Based on the Google Developer Knowledge, does Google Workspace support MCP servers?"
]

print("=" * 60)
print("   DEVELOPER QUERY AGENT")
print("   Powered by Antigravity + Developer Knowledge MCP")
print("=" * 60)
print()
print("This agent uses the following course concepts:")
print("  1. MCP Server — Developer Knowledge API")
print("  2. Antigravity — Agentic IDE")
print("  3. Agent Skills — answer-formatter skill")
print()
print("Example queries this agent handles:")
print()
for i, q in enumerate(QUERIES, 1):
    print(f"  Query {i}: {q}")
print()
print("To run: Open Antigravity CLI (agy) and paste any query above.")
print("=" * 60)
