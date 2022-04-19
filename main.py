from fastapi import FastAPI, HTTPException

from app.utils import fibonacci
from app.schemas import FibonacciRequestModel, FibonacciValueResponseModel


app = FastAPI(
    title="Fibonacci FastAPI Example",
    description="This FastAPI example returns the Fibonacci value that corresponds to the given index.",
    version="1.0.0",
)

@app.get("/api/v1/fibonacci/{fibonacci_index}/",
    response_model=FibonacciValueResponseModel,
    responses={
        200: {
            "description": "Return the Fibonacci value that corresponds to the given index.",
        },
        400: {
            "description": "Index value must be a positive integer.",
        }
    },    
)
async def get_index(fibonacci_index: int):
    try:
        fibo_idx = FibonacciRequestModel(fibonacci_index=fibonacci_index)
        fibo_value = fibonacci(fibo_idx.fibonacci_index)
        return FibonacciValueResponseModel(fibonacci_value=fibo_value)
    except:
        return HTTPException(status_code=400, detail="Index value must be a positive integer")
