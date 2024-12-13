from fastapi import FastAPI
from fastapi.responses.RedirectResponse
from langserve import add_routes
from langchain_core.runnables import Runnable  # Import the Runnable class

app = FastAPI()

# Define or import final_chain here
class MyRunnable(Runnable):
    def run(self, input):
        # Define the logic for your runnable here
        return "Processed: " + input

    def invoke(self, input):
        # Implement the abstract method
        return self.run(input)

final_chain = MyRunnable()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

# Edit this to add the chain you want to add
add_routes(app, final_chain, path="/rag")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)