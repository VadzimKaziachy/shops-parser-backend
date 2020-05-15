from typing import NoReturn


class BaseService:

    def start(self) -> NoReturn:
        raise NotImplemented()
