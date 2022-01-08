class App:
    def __init__(self, param='some_value'):
        pass

    def public(self):
        'User, this public method is for you!'
        return 'public method'

    def _indicate_private(self):
        return 'private method'

    def __pseudo_private(self):
        return 'really private method'