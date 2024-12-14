class UserController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_user_data(self):
        greetings = "Здравствуй"
        return self.view.render_page(self.model, greetings)