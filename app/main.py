from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from api.v1.schemas.response_models import StandardResponse, SuccessResponse
from api.v1.routes import api_version_one_router

import uvicorn

app = FastAPI(
    title="Converter API",
    version="1.0.0",
    docs_url="/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_version_one_router)

@app.get("/",
         tags=["Home"],
         response_model=StandardResponse,
         responses={
             200: {
                 "model": StandardResponse,
                 "description": "Welcome response"
             }
         })
async def get_root(request: Request) -> dict:
    """
    Root endpoint for the API

    Returns:
        Standardized success response with welcome message
    """
    success_response = SuccessResponse(
        status_code=status.HTTP_200_OK,
        message="Welcome to converter API. Access the API documentation at /docs",
        data={}
    )
    return success_response


@app.get("/probe",
         tags=["Home"],
         response_model=StandardResponse,
         responses={
             200: {
                 "model": StandardResponse,
                 "description": "API probe response"
             }
         })
async def probe():
    """
    Probe endpoint to check if the API is running

    Returns:
        Standardized success response confirming API is running
    """
    success_response = SuccessResponse(
        status_code=status.HTTP_200_OK,
        message="I am the Python FastAPI API responding",
        data={}
    )
    return success_response


@app.get("/health",
         tags=["Home"],
         response_model=StandardResponse,
         responses={
             200: {
                 "model": StandardResponse,
                 "description": "Health check response"
             }
         })
async def health_check():
    """
    Health check endpoint for monitoring

    Returns:
        Standardized success response with health status
    """
    success_response = SuccessResponse(
        status_code=status.HTTP_200_OK,
        message="Health check successful",
        data={"status": "healthy"}
    )
    return success_response


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )