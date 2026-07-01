import subprocess

def run_agent(query: str):
    """
    Developer Query Agent
    Uses Antigravity CLI with Developer Knowledge MCP to answer technical queries.
    """
    print(f"\n🤖 Developer Query Agent")
    print(f"📝 Query: {query}")
    print("-" * 50)
    
    # Run query through Antigravity CLI
    result = subprocess.run(
        ["agy", "prompt", query],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"Error: {result.stderr}")

if __name__ == "__main__":
    # Example queries to demonstrate the agent
    queries = [
        "Based on the Google Developer Knowledge, what is the best way to authenticate with Google APIs?",
        "Based on the Google Developer Knowledge, does Google Workspace support MCP servers?"
    ]
    
    for query in queries:
        run_agent(query)
        print("\n" + "="*50 + "\n")
