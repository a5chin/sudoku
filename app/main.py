from collections.abc import Callable
from logging import getLogger

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from google.cloud.logging import Client
from google.cloud.logging.handlers import StructuredLogHandler
from google.cloud.logging_v2.handlers import setup_logging
from opentelemetry import trace
from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.propagate import set_global_textmap
from opentelemetry.propagators.cloud_trace_propagator import CloudTraceFormatPropagator
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from app.api.errors import http422_error_handler, http_error_handler
from app.api.routes.api import router as api_router
from app.core import get_app_settings
from app.core.settings import AppSettings


def init_application():
    settings = get_app_settings()

    application = FastAPI(**settings.fastapi_kwargs)
    application.add_middleware(
        middleware_class=CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    if settings.debug:
        setup_logging(StructuredLogHandler())
    else:
        client = Client()
        client.setup_logging()

        set_global_textmap(CloudTraceFormatPropagator)
        tracer_provider = TracerProvider()
        cloud_trace_exporter = CloudTraceSpanExporter()
        tracer_provider.add_span_processor(BatchSpanProcessor(cloud_trace_exporter))
        trace.set_tracer_provider(tracer_provider)
        FastAPIInstrumentor.instrument_app(application)

    application.add_event_handler(
        "startup", create_start_app_handler(application, settings)
    )
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix=settings.api_prefix_v1)

    logger = getLogger(__name__)
    logger.info(settings)

    return application


def create_start_app_handler(fastapi: FastAPI, settings: AppSettings) -> Callable:
    def start_app() -> None:
        fastapi.state.settings = settings

    return start_app


def create_stop_app_handler(fastapi: FastAPI) -> Callable:
    def stop_app() -> None:
        pass

    return stop_app


app = init_application()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8080")
