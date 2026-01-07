from pydantic import BaseModel
from typing import List


class ArticleSummary(BaseModel):
    summary: str
    key_points: List[str]


class RewriteResult(BaseModel):
    rewritten_text: str


class ExtractResult(BaseModel):
    items: List[str]
