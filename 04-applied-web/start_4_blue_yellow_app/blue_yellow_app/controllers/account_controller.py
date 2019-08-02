import pyramid_handlers
from blue_yellow_app.controllers.base_controller import BaseController
from blue_yellow_app.viewmodels.register_viewmodel import RegisterViewModel


class AccountController(BaseController):
    @pyramid_handlers.action(renderer='templates/account/index.pt')
    def index(self):
        return {}

    @pyramid_handlers.action(renderer='templates/account/signin.pt')
    def signin(self):
        return{}

    # GET /account/register
    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='GET',
                             name='register')
    def register_get(self):
        print('Calling register via get...')
        vm = RegisterViewModel()
        return vm.to_dict()

    # POST /account/register
    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='POST',
                             name='register')
    def register_post(self):
        vm = RegisterViewModel()
        vm.from_dict(self.request.POST)

        # print(f'Calling register via POST: {vm.email}, {vm.password}, {vm.confirm_password}')

        vm.validate()
        if vm.error:
            return vm.to_dict()

        # validations: no account exists, passwords match
        # create account in DB
        # send welcome email

        print("Redirecting to account index page...")
        self.redirect('/account')

        return{}
