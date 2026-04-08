from fastapi import FastAPI

app = FastAPI()

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