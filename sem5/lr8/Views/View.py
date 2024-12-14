from flask import render_template


class View:

    @staticmethod
    def render_page(data):
        return render_template('layout.html', data=data)
