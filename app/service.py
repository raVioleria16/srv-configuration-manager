from rv16_lib.storage.redis_connector import RedisConnector
from rv16_lib.architecture.base_service import BaseService
from rv16_lib import get_object_from_config

from config import SrvConfig
from providers import ProviderType
from providers.local import LocalProvider


class Service(BaseService):

    def __init__(self):
        super().__init__()
        self.config = get_object_from_config(config_model=SrvConfig)
        self.service_name = self.config.hostname

    def initialize_service(self):
        redis_cfg = self.config.ext_srv.redis_srv

        self.providers = {
            ProviderType.LOCAL: LocalProvider(
                db_client=RedisConnector(
                    host=redis_cfg.host,
                    port=redis_cfg.port,
                    db=redis_cfg.db
                )
            )
        }


service = Service()
