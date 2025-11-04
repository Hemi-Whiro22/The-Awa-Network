"""Application configuration helpers.

Uses Pydantic settings to orchestrate Tiwhanawhana environment variables.
"""
from functools import lru_cache
from typing import List

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    project_name: str = Field(
        default="Tiwhanawhana Orchestrator", alias="PROJECT_NAME")
    debug: bool = Field(default=False, alias="DEBUG")
    fastapi_host: str = Field(default="0.0.0.0", alias="FASTAPI_HOST")
    fastapi_port: int = Field(default=8000, alias="FASTAPI_PORT")
    cors_origins: str = Field(default="", alias="CORS_ORIGINS")

    supabase_url: str | None = Field(default=None, alias="SUPABASE_URL")
    supabase_key: str | None = Field(default=None, alias="SUPABASE_KEY")
    publishable_key: str | None = Field(default=None, alias="PUBLISHABLE_KEY")

    openai_api_key: str | None = Field(default=None, alias="OPENAI_API_KEY")
    embedding_model: str = Field(
        default="text-embedding-3-large", alias="EMBEDDING_MODEL")
    ocr_model: str = Field(default="gpt-4o-mini", alias="OCR_MODEL")
    translation_model: str = Field(
        default="gpt-4o-mini", alias="TRANSLATION_MODEL")
    assistant_model: str = Field(default="gpt-5", alias="ASSISTANT_MODEL")
    local_llm_model: str = Field(default="llama3", alias="LOCAL_LLM_MODEL")

    database_url: str | None = Field(default=None, alias="DATABASE_URL")

    mauri_root: str = Field(default="~/mauri", alias="MAURI_ROOT")
    logs_dir: str = Field(default="logs/", alias="LOGS_DIR")
    uploads_dir: str = Field(default="uploads/", alias="UPLOADS_DIR")
    cache_dir: str = Field(default="cache/", alias="CACHE_DIR")

    supabase_table_memory: str | None = Field(
        default=None, alias="SUPABASE_TABLE_MEMORY")
    supabase_table_uploads: str | None = Field(
        default=None, alias="SUPABASE_TABLE_UPLOADS")
    supabase_table_summaries: str | None = Field(
        default=None, alias="SUPABASE_TABLE_SUMMARIES")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

    def cors_origin_list(self) -> List[str]:
        """Return CORS origins as a list for FastAPI configuration."""
        if not self.cors_origins:
            return []
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache()
def get_settings() -> Settings:
    """Cached settings instance so the orchestrator reads env once."""
    return Settings()
