from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Postgres:
    postgres_host: str
    postgres_db: str
    postgres_password: str
    postgres_port: int
    postgres_user: str

    def get_connection_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


@dataclass
class Telethon:
    api_id: int
    api_hash: str


@dataclass
class Config:
    tg_bot: TgBot
    postgres_db: Postgres
    telethon: Telethon


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(token=env("BOT_TOKEN")),
        postgres_db=Postgres(
            postgres_host=env("POSTGRES_HOST"),
            postgres_db=env("POSTGRES_DB"),
            postgres_password=env("POSTGRES_PASSWORD"),
            postgres_port=env.int("POSTGRES_PORT"),
            postgres_user=env("POSTGRES_USER"),
        ),
        telethon=Telethon(api_id=env("API_ID"), api_hash=env("API_HASH")),
    )
