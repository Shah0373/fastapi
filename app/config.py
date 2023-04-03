from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"
    # database_password: str = "localhost"
    # database_username: str = "postgres"
    # secret_key: str = "3hj4vkj32v432guv"
    # MY_DB_URL: str


settings = Settings()

# print(settings.MY_DB_URL)
