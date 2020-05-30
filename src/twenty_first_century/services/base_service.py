from typing import NoReturn


class BaseService:
    """
    This class describes the rules that a developer must follow when adding a new service.
    """

    def start(self) -> NoReturn:
        """
        This method should be the last in all services.
        """
        raise NotImplemented('Method `start` was not overridden.')
