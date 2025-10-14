import json

from rv16_lib.logger import logger
from starlette import status

from rv16_lib.storage.database_connector import DatabaseConnector
from rv16_lib.storage.redis_connector import RedisElement

from models.exceptions.exceptions import ConfigurationManagerException
from providers.base_provider import Provider


class LocalProvider(Provider):

    def __init__(self, db_client: DatabaseConnector):
        self.db_client = db_client

    def register_service(self, service: str, configuration: dict):
        logger.info("Registering service %s with configuration %s", service, configuration)

        payload = RedisElement(
            key=service,
            value=json.dumps(configuration)
        )
        result = self.db_client.insert_one(payload)
        logger.info("Service %s registered: %s", service, result)
        return result


    def get_service(self, service: str):
        logger.info(f"Retrieving configuration for service {service}")
        payload = RedisElement(
            key=service,
        )
        service_params = self.db_client.find(payload)
        if service_params is None:
            raise ConfigurationManagerException(status_code=status.HTTP_404_NOT_FOUND, message=f"Service {service} not found.")
        response = json.loads(service_params)
        logger.info(f"Configuration found for service {service}: {type(response)} {response}")
        return response
