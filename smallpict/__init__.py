"""
SmallPict Official Python SDK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
High-performance cloud image optimization, format transcoding (WebP, AVIF),
CDN edge invalidation, and real-time quota tracking.
"""

from .aclient import AsyncSmallPictClient
from .client import SmallPictClient
from .errors import (
    AuthenticationError,
    NetworkError,
    NotFoundError,
    PermissionDeniedError,
    QuotaExceededError,
    RateLimitError,
    ServerError,
    SmallPictError,
    TimeoutError,
    ValidationError,
    sanitize_message,
)
from .models import (
    FallbackMode,
    FitMode,
    ImageFormat,
    JobStatusResult,
    OptimizeOptions,
    OptimizeResult,
    PurgeOptions,
    PurgeResponse,
    PurgeType,
    QuotaResponse,
)

__version__ = "0.0.1"
__all__ = [
    "AsyncSmallPictClient",
    "AuthenticationError",
    "FallbackMode",
    "FitMode",
    "ImageFormat",
    "JobStatusResult",
    "NetworkError",
    "NotFoundError",
    "OptimizeOptions",
    "OptimizeResult",
    "PermissionDeniedError",
    "PurgeOptions",
    "PurgeResponse",
    "PurgeType",
    "QuotaExceededError",
    "QuotaResponse",
    "RateLimitError",
    "ServerError",
    "SmallPictClient",
    "SmallPictError",
    "TimeoutError",
    "ValidationError",
    "sanitize_message",
]
