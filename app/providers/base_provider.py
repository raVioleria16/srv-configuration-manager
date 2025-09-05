from abc import ABC, abstractmethod

from rv16_lib.architecture.base_provider import BaseProvider


class Provider(BaseProvider):

    @abstractmethod
    def register_service(self, service: str, configuration: dict):
        """
        Register a service to the ConfigurationManager registry.
        :param service: the service to register.
        :param configuration: the configuration of the service.
        :return:
        """
        pass


    @abstractmethod
    def get_service(self, service: str):
        """
        Get the configuration of a service for a target (service or app).
        :param service: the service to get the configuration from.
        :return:
        """
        pass
