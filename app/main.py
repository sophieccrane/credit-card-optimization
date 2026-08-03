from fastapi import FastAPI
from app.api.v1.endpoints.lookups import router

# Initialize the application instance
app = FastAPI(name="Credit Card API", version="1.0.0", description="API for credit card optimization")

app.include_router(router)