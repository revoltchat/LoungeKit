from __future__ import annotations

import aiohttp
import asyncpg
import revolt
import msgspec.toml
from revolt.ext import commands

from .loungekit_types.config import Config


class LoungeKitBot(commands.CommandsClient):
    config: Config
    db: asyncpg.Pool

    def __init__(self, session: aiohttp.ClientSession):
        self.load_config()

        super().__init__(session, self.config.token, case_insensitive=True)

    def load_config(self):
        with open("config.toml") as f:
            self.config: Config = msgspec.toml.decode(f.read(), type=Config)

    async def setup_hook(self):
        self.db = await asyncpg.create_pool(self.config.database.dsn) # type: ignore

        for extension in self.config.extensions:
            self.load_extension(f"extensions.{extension}")

    async def get_prefix(self, message: revolt.Message) -> str | list[str]:
        return self.config.prefix

    async def start(self) -> None:
        await self.setup_hook()
        await super().start()
