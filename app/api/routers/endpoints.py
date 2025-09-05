from fastapi import APIRouter, HTTPException
from rv16_lib.logger import logger
from starlette import status
from starlette.responses import JSONResponse

from rv16_lib.configuration_manager.entities import ServiceRegistrationRequest, ServicePairingRequest, ServiceConfigurationRequest

from service import service as srv

# Create an API Router
router = APIRouter()

# Example endpoint
@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/health")
def health_check(request_body: dict):
    return {"status": "ok", "message": request_body}


@router.post("/register-service")
def register_service(request_body: ServiceRegistrationRequest) -> JSONResponse:

    if not srv or srv.providers == {}:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Service is not available",
        )

    provider = srv.get_provider(request_body.provider)
    response = provider.register_service(service=request_body.service,
                                         configuration=request_body.configuration)

    return JSONResponse(status_code=status.HTTP_200_OK, content=response)


@router.post("/get-service-configuration")
def get_service_configuration(request_body: ServiceConfigurationRequest) -> JSONResponse:

    if not srv or srv.providers == {}:
        print(f"Provider {request_body.provider} is not available. No providers registered.")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Service is not available",
        )

    provider = srv.get_provider(request_body.provider)
    if not provider:
        print(f"Provider {request_body.provider} is not available. Choose among {list(srv.providers.keys())}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Provider {request_body.provider} is not available. Choose among {list(srv.providers.keys())}",
        )

    response = provider.get_service(service=request_body.service)
    return JSONResponse(status_code=status.HTTP_200_OK, content=response)

