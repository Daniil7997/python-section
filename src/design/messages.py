from abc import ABC
import enum
from dataclasses import dataclass


class MessageType(enum.Enum):
    TELEGRAM = enum.auto()
    MATTERMOST = enum.auto()
    SLACK = enum.auto()


@dataclass
class JsonMessage:
    message_type: MessageType
    payload: str


@dataclass
class ParsedMessage:
    """There is no need to describe anything here."""


@dataclass
class StandardMessage:
    msg_id: str
    user: str
    text: str
    timestamp: int


class MessageParser(ABC):
    pass


class ParserFactory(ABC):
    parsers: dict[MessageType, type[MessageParser]] = {}
