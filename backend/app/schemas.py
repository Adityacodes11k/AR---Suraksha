from pydantic import BaseModel, Field


class TrainingResult(BaseModel):
    worker_id: str = Field(min_length=1)
    module: str = Field(min_length=1)
    score: int = Field(ge=0, le=100)
    passed: bool
    completed_at: str
    device_attempt_id: str = Field(min_length=1)


class Certificate(BaseModel):
    certificate_id: str
    worker_id: str
    module: str
    score: int
    verified: bool
