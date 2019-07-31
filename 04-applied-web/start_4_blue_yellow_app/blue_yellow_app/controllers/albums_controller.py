import pyramid_handlers
from blue_yellow_app.controllers.base_controller import BaseController
from blue_yellow_app.services.album_service import  AlbumsService


class AlbumsController(BaseController):
    @pyramid_handlers.action(renderer='templates/albums/index.pt')
    def index(self):
        # data / service access
        albums = AlbumsService.get_albums()

        # return the model
        return {'albums': albums}
