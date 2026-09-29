from fastapi import FastAPI, HTTPException
from .schemas import TrainingResult, Certificate

app = FastAPI(
    title="AR Suraksha API",
    version="0.1.0",
    description="Offline-first training result synchronization API.",
)

# Temporary in-memory store for the MVP foundation.
# Replace with PostgreSQL repository/service code for deployment.
results: dict[str, TrainingResult] = {}
certificates: dict[str, Certificate] = {}


@app.get("/health")
def health():
    return {"status": "ok", "service": "ar-suraksha-api"}


@app.post("/api/v1/training-results")
def submit_training_result(result: TrainingResult):
    results[result.device_attempt_id] = result

    certificate_id = None
    if result.passed:
        certificate_id = f"ARS-{result.worker_id}-{result.device_attempt_id[:8]}"

        certificates[certificate_id] = Certificate(
            certificate_id=certificate_id,
            worker_id=result.worker_id,
            module=result.module,
            score=result.score,
            verified=True,
        )

    return {
        "synced": True,
        "device_attempt_id": result.device_attempt_id,
        "certificate_id": certificate_id,
    }


@app.get("/api/v1/certificates/{certificate_id}", response_model=Certificate)
def verify_certificate(certificate_id: str):
    certificate = certificates.get(certificate_id)

    if certificate is None:
        raise HTTPException(status_code=404, detail="Certificate not found")

    return certificate
