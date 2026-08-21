from fastapi import FastAPI
from app.api.v1.endpoints.lookups import router as lookups_router
from app.api.v1.endpoints.calculations import router as calculation_router

# Initialize the application instance
app = FastAPI(title="Credit Card API", version="1.0.0", description="API for credit card optimization")

app.include_router(lookups_router)
app.include_router(calculation_router)