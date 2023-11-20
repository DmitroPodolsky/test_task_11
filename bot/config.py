import json
from pathlib import Path
from typing import Optional

from loguru import logger
from pydantic import BaseSettings

project_dir = Path(__file__).parent.parent
data_dir = project_dir / "data"


class Settings(BaseSettings):
    API_ID: int
    API_HASH: str
    GROUP_LINK: str
    SESSION_TOKEN: Path = data_dir / "token_session.json"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()  # type: ignore


def get_session() -> Optional[str]:
    if settings.SESSION_TOKEN.exists():
        with open(file=settings.SESSION_TOKEN, encoding="utf-8") as file:
            json_data: dict = json.load(file)
            file.close()
            return json_data["token"]
    logger.warning("missing session_token, you need to generate new session_token")
    return None


def save_session(session_token: str):
    with settings.SESSION_TOKEN.open("w", encoding="utf-8") as file:
        json.dump({"token": session_token}, file, indent=4, ensure_ascii=False)
    logger.success("created new session_token")
