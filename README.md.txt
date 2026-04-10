Business Problem:
Many trucks return empty after delivering goods, known as the empty backhaul problem.
This leads to increased fuel consumption, higher costs, and inefficient use of transportation resources.


Possible Solution:
A system that matches delivery routes with available return loads can reduce empty trips and improve efficiency in logistics.


Implemented Solution:
We developed a Backhaul Optimizer that:
Takes a location as input
Finds delivery routes
Matches return loads
Uses n8n for automation and AI for better suggestions


Tech Stack Used:
FastAPI (Backend)
n8n (Workflow Automation)
HTML, JavaScript (Frontend)
OpenAI / LLM (AI Integration)


How to Run Locally:
git clone <repo-link>
cd project
pip install fastapi uvicorn langchain-openai
setx OPENAI_API_KEY "your_api_key"
uvicorn main:app --reload
n8n


References:
FastAPI Docs
n8n Docs
OpenAI Docs
