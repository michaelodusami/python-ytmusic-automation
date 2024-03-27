from enum import Enum

class Status(Enum):
    SUCCESS = 'SUCCESS'
    ERROR = 'ERROR'
    INVALID = 'INVALID'
    DUPLICATES_EXIST = 'DUPLICATES_EXIST'
    IDENTICAL = 'IDENTICAL'
