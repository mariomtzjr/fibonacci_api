from pydantic import BaseModel


class FibonacciRequestModel(BaseModel):
    fibonacci_index: int


class FibonacciValueResponseModel(BaseModel):
    fibonacci_value: int