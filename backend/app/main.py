"""Entry point of the AntojoBot API."""

from fastapi import FastAPI

app = FastAPI(
    title="AntojoBot API",
    description="Recommends dishes based on natural-language cravings.",
    version="0.1.0",
)


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    """Return the service status. Used to check that the API is running."""
    return {"status": "ok"}
