class BasePageService:
    rest_serializer = None
    
    def get_base_context(self, request, object):
        pass

    def get_context(self, request, object):
        return self.get_base_context(request, object)

    def get_rest_context(self, request, object):
        print(self.rest_serializer, 'self.rest_serializer')
        if self.rest_serializer is None:
            return {}
        return self.rest_serializer(self.get_base_context(request, object)).data
