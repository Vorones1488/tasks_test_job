from abc import ABC, abstractmethod


class DTO(ABC):
    @abstractmethod
    async def serialaizr_to_dict(self, json) -> dict:
        raise NotImplementedError
