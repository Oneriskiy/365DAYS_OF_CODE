from pydantic import BaseModel, Field

class MonumentsSchema(BaseModel):
    title: str = Field(max_length=30)
    price:  int = Field(gt=0)
