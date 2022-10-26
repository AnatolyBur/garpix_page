
from atexit import register

from ..models import Category
from garpix_page.contexts.base_service import BasePageService


class CategoryPageService(BasePageService):
    page_model = Category

    def get_base_context(self, request, object):
        print(request, object, 'request, object')
        return {
            'hello_service': 'Hello, service'
        }
