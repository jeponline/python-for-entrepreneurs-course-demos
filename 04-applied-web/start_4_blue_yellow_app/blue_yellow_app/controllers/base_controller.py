from blue_yellow_app.infrastructure import static_cache


class BaseController:
    def __init__(self, request):
        self.request = request
        self.build_cache_id = static_cache.build_cache_id
