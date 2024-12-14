from LR8.Views.View import View


class Controller:

    def __init__(self):
        self.view = View()
        self.data = {
            "greetings": "Привет",
        }

    def get_user_data(self):
        return self.view.render_page(self.data)
