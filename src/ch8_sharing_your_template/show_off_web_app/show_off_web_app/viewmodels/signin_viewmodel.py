from show_off_web_app.viewmodels.viewmodelbase import ViewModelBase


class SigninViewModel(ViewModelBase):
    def __init__(self):
        self.email = None
        self.password = None
        self.error = None

    def from_dict(self, data_dict):
        self.email = data_dict.get('email')
        self.password = data_dict.get('password')

        # Just to test rollbar:
        # raise ValueError("Ka Boom!")
