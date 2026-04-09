from fastapi import FastAPI
from langchain_openai import ChatOpenAI

app = FastAPI()

# Initialize LLM (only once)
llm = ChatOpenAI(
    temperature=0,
    api_key="YOUR_OPENAI_API_KEY"  # Replace with your key
)

# Mock delivery data
deliveries = [
    {"from": "Hyderabad", "to": "Bangalore", "load": "Electronics"},
    {"from": "Chennai", "to": "Mumbai", "load": "Furniture"},
    {"from": "Delhi", "to": "Pune", "load": "Clothing"}
]

# Mock return loads
return_loads = [
    {"from": "Bangalore", "to": "Hyderabad", "load": "Groceries"},
    {"from": "Mumbai", "to": "Chennai", "load": "Steel"},
    {"from": "Pune", "to": "Delhi", "load": "Machinery"}
]

@app.get("/")
def home():
    return {"message": "Backhaul Optimizer Running"}

@app.get("/find-delivery")
def find_delivery(location: str):
    results = [d for d in deliveries if d["from"].lower() == location.lower()]
    return {"deliveries": results}

@app.get("/find-return")
def find_return(destination: str):
    results = [r for r in return_loads if r["from"].lower() == destination.lower()]
    return {"return_loads": results}

@app.get("/optimize")
def optimize(location: str):
    delivery = [d for d in deliveries if d["from"].lower() == location.lower()]

    if not delivery:
        return {"message": "No delivery found"}

    destination = delivery[0]["to"]
    return_trip = [r for r in return_loads if r["from"].lower() == destination.lower()]

    return {
        "delivery": delivery,
        "return_load": return_trip
    }

@app.get("/ai-optimize")
def ai_optimize(location: str, use_mock: bool = True):
    """
    AI Optimization endpoint
    use_mock=True -> returns a fake response (safe for testing)
    use_mock=False -> calls OpenAI API through LangChain
    """
    prompt = f"""
    Find a delivery and return load plan for trucks starting from {location}.
    Available deliveries: {deliveries}
    Available return loads: {return_loads}
    """

    if use_mock:
        # Mock response for testing
        mock_response = f"Optimized route plan for {location} (mock response)"
        return {"result": mock_response}

    # Call real API safely
    try:
        response = llm.invoke(prompt)
        return {"result": response.content}
    except Exception as e:
        return {"error": f"API call failed: {str(e)}"}