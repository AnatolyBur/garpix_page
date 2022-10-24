from garpix_page.models import BasePage


class AlreadyRegistered(Exception):
    pass


class PageService:
    def __init__(self):
        self._registry = {}

    def register(self, model_or_iterable, service_class, **options): # service_class сделать дефолт
        if isinstance(model_or_iterable, BasePage):
            model_or_iterable = [model_or_iterable]
        for _model in model_or_iterable:
            model = _model
            if model in self._registry:
                msg = 'The model %s is already registered ' % model.__name__
                raise AlreadyRegistered(msg)
            self._registry[model] = service_class
        return True

    def is_registered(self, model):
        return model in self._registry

    def get_service_by_name(self, model):
        return self._registry.get(model, None)


class DefaultPageService(PageService):
    pass


page_service = DefaultPageService()
