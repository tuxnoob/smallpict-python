# Changelog

All notable changes to the `smallpict` Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.4] - 2026-10-01

### Changed
- Dropped support for Python 3.8 and 3.9 (EOL).
- Set minimum supported Python version to `>= 3.10`.
- Added official support and testing matrix for Python 3.10, 3.11, 3.12, 3.13, and 3.14.

## [1.0.0] - 2026-08-22

### Added
- Official Python SDK implementation for SmallPict OpenAPI 3.1.0 API.
- First-class `SmallPictClient` (sync) and `AsyncSmallPictClient` (async) clients powered by `httpx`.
- Context manager support (`with` and `async with`).
- Pydantic models for request options and response payloads.
- 4 unified core client methods: `optimize()`, `get_quota()`, `purge_cdn()`, and `validate_key()`.
- Helper `get_job_status()` for polling async conversion tasks.
- Optional Pillow / PIL integration (`smallpict[pil]`) supporting direct `PIL.Image` input.
- Automatic secret masking to ensure API keys and signatures never leak in exception strings.
- Resilient HTTP transport with 30s timeouts, exponential backoff, jitter, and automatic `Idempotency-Key` UUID injection.
- Optional `fallback_mode=FallbackMode.PASSTHROUGH` for high availability on quota limits.
- Full type annotations (PEP 561 `py.typed`) and strict `mypy` compatibility.
