from orator import Model

class User(Model):
    __table__ = 'users'
    __timestamps__ = False

    @classmethod
    def print_all_users(cls):
        res = cls.all()
        for _r in res:
            print(f"{_r.id}  {_r.name}  {_r.height}")

    @classmethod
    def find_by_name(cls, name):
        return cls.where('name', '=', name).get()

    @classmethod
    def create(cls, name, height):
        new_u = cls()
        new_u.name = name
        new_u.height = height
        new_u.save()
        return new_u

    def update(self, name=None, height=None):
        if name:
            self.name = name
        if height:
            self.height = height
        self.save()
