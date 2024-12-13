from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse

app = FastAPI()

# Define or import final_chain here
class MyRunnable:
    def run(self, input):
        # Define the logic for your runnable here
        return "Processed: " + input

    def invoke(self, input):
        # Implement the method
        return self.run(input)

final_chain = MyRunnable()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

@app.post("/rag")
async def rag_endpoint(request: Request):
    data = await request.json()
    input_data = data.get("input")
    result = final_chain.invoke(input_data)
    return JSONResponse(content={"result": result})

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)