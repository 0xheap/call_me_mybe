from pydantic import BaseModel
from typing import List, Dict


class PromptInput(BaseModel):
    prompt: str

class Parameters(BaseModel):
    type: str

class ReturnType(BaseModel):
    type: str

class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: Dict[str, Parameters]
    returns: ReturnType

class FunctionCall(BaseModel):
    prompt: str
    name: str
    parameters: dict