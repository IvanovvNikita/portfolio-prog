from flask import render_template


class UserView:

    @staticmethod
    def render_page(user, greetings):
        fullname = user.get_fullname()
        name = fullname['second_name'] + ' ' +fullname['first_name'] + ' ' + fullname['fathers_name']
        data = {
            "greetings": greetings,
            "name": name,
        }
        return render_template('extended_layout.html', data=data)