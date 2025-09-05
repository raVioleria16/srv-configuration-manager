from rv16_lib.exceptions import RV16Exception


class ConfigurationManagerException(RV16Exception):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code, message)