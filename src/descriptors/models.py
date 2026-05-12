class Field:
    def __init__(self, path: str):
        self.path = path.split('.')

    def __get__(self, instance, owner):
        if instance is None:
            return self

        data = instance.payload
        for key in self.path:
            try:
                data = data[key]
            except (KeyError, TypeError):
                return None
        return data

    def __set__(self, instance, value):
        data = instance.payload
        parts = self.path
        for key in parts[:-1]:
            data = data[key]
        data[parts[-1]] = value


class Model:
    def __init__(self, payload: dict):
        self.payload = payload
