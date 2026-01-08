from pydantic import BaseModel, HttpUrl

class TestRequest(BaseModel):
    url: HttpUrl
    duration: int = 10
    rps: int = 2
