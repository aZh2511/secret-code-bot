from datetime import datetime

from aiogram import types
from asyncpg import Connection
from asyncpg.exceptions import UniqueViolationError

from loader import db


class DBCommands:
    """Class for working with DB."""
    pool: Connection = db

    ADD_NEW_USER = "INSERT INTO users (chat_id, username, full_name, adding_date) " \
                   "VALUES ($1, $2, $3, $4)"
    COUNT_USERS = "SELECT COUNT (*) FROM users"
    GET_USERS = "SELECT (username, full_name) FROM users"
    GET_CODE = "SELECT secret_code FROM code"
    GET_CODE_ID = "SELECT id FROM code"
    SET_CODE = "UPDATE code SET secret_code=$1 WHERE id=$2"
    ADD_NEW_USER_WHITELIST = "INSERT INTO whitelist (chat_id) VALUES ($1)"
    GET_WHITELIST = "SELECT chat_id FROM whitelist"
    GET_TEXT = "SELECT message FROM texts WHERE button=$1"
    SET_TEXT = "UPDATE texts SET message=$1 WHERE button=$2"

    async def add_new_user(self):
        """Add new user to db."""
        user = types.User.get_current()
        command = self.ADD_NEW_USER

        chat_id = user.id
        username = user.username
        full_name = user.full_name
        adding_date = datetime.now()

        args = chat_id, username, full_name, adding_date

        try:
            await self.pool.fetchval(command, *args)
        except UniqueViolationError:
            pass

    async def add_user_whitelist(self):
        """Add new user to whitelist."""
        user = types.User.get_current()
        command = self.ADD_NEW_USER_WHITELIST

        chat_id = user.id

        args = chat_id,

        try:
            await self.pool.fetchval(command, *args)
        except UniqueViolationError:
            pass

    async def count_users(self):
        """Count users in db."""
        command = self.COUNT_USERS
        record = await self.pool.fetchval(command)
        return record

    async def get_code(self):
        """Get secret-code from db."""
        command = self.GET_CODE

        result = await self.pool.fetchval(command)
        if result:
            return result
        else:
            return 'No code available right now'

    async def get_code_id(self):
        """Get id of the secret-code in db."""
        command = self.GET_CODE_ID
        code_id = await self.pool.fetchval(command)
        return code_id

    async def set_code(self, new_code):
        """Update current secret-code in db."""
        command = self.SET_CODE
        return await self.pool.fetchval(command, new_code, await self.get_code_id())

    async def get_users(self):
        """Get all users from the db."""
        command = self.GET_USERS
        data = await self.pool.fetch(command)

        data = [data[i][0] for i in range(len(data))]

        text = ''
        for num, row in enumerate(data):
            text += f'{num + 1}. @{row[0]} {row[1]}\n'
        return text

    async def get_whitelist(self):
        """Get users in whitelist."""
        command = self.GET_WHITELIST
        data = await self.pool.fetch(command)
        data = [data[i][0] for i in range(len(data))]
        return data

    async def get_text(self, button: str):
        """Get text from db."""
        command = self.GET_TEXT
        text = await self.pool.fetchval(command, button)
        text = text
        return text

    async def set_text(self, text: str, button: str):
        """Update text in db."""
        command = self.SET_TEXT
        args = text, button,
        return await self.pool.fetchval(command, *args)


database = DBCommands()
