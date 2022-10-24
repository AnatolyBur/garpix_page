
from atexit import register

from ..models import Category
from garpix_page.contexts.register import register
from garpix_page.contexts.base_service import BasePageService


@register(Category)
class CategoryPageService(BasePageService):
    def get_base_context(self, request, object):
        print(self, request, object)
        return {
            'hello_service': 'Hello, service'
        }
