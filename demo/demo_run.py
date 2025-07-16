
# Simulated demo run of the AI agent (replace with actual imports and agent)
queries = [
    "Where is my order?",
    "How can I contact customer support?",
    "I want to cancel my subscription."
]

def run_demo():
    for q in queries:
        print(f"User: {q}")
        # Replace with: response = agent.run(q)
        response = "This is a sample response for: " + q
        print("Bot:", response)
        print("-" * 50)

if __name__ == "__main__":
    run_demo()
