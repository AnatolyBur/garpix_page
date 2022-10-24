from .service import page_service


def register(*models):
    def _model_page_wrapper(service_class):
        if not models:
            raise ValueError("At least one model must be passed to register.")

        service = page_service
        service.register(models, service_class=service_class)

        return service_class

    return _model_page_wrapper
