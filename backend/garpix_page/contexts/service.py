from garpix_page.models import BasePage
from .base_service import BasePageService

class AlreadyRegistered(Exception):
    pass


class PageService:
    def __init__(self):
        self._registry = {}

    def register(self, service_or_iterable, **options): # service_class сделать дефолт
        if issubclass(service_or_iterable, BasePageService):
            service_or_iterable = [service_or_iterable]
        for service in service_or_iterable:
            model = service.page_model
            if model in self._registry:
                msg = 'The model %s is already registered ' % model.__name__
                raise AlreadyRegistered(msg)
            self._registry[model] = service
        return True

    def is_registered(self, model):
        return model in self._registry

    def get_service_by_name(self, model):
        return self._registry.get(model, None)


class DefaultPageService(PageService):
    pass


page_service = DefaultPageService()
