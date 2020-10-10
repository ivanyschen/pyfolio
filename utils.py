import yaml

import base


with open('config.yaml', 'r') as file:
    CONFIG = yaml.safe_load(file)


class YmlModifier:

    def __init__(self, path_to_yml):
        self._path_to_yml = path_to_yml
        self._data = self._read_yml()
        self._required_data_fields = self._data['REQUIRED_DATA_FIELDS']
        self._items = self._data['ITEMS']

    def add_item(self, obj):
        new_item = {}
        for field in self._required_data_fields:
            new_item[field] = getattr(obj, field)
        self._items.append(new_item)
        self._save_yml()

    def _read_yml(self):
        with open(self._path_to_yml, 'r') as file:
            data = yaml.safe_load(file)
        return data

    def _save_yml(self):
        with open(self._path_to_yml, 'w') as file:
            yaml.safe_dump(self._data, file)


class AccountModifier(YmlModifier):

    def __init__(self, path_to_yml=None):
        if path_to_yml is None:
            path_to_yml = CONFIG['ACCOUNT_YAML']
        super().__init__(path_to_yml)

    def list_items(self, n=1, from_top=True):
        if from_top:
            return [base.Account(**item) for item in self._items[:n]]

        return [base.Account(**item) for item in self._items[:-n-1:-1]]


class OrderModifier(YmlModifier):

    def __init__(self, path_to_yml=None):
        if path_to_yml is None:
            path_to_yml = CONFIG['ORDER_YAML']
        super().__init__(path_to_yml)

    def list_items(self, n=1, from_top=True):
        if from_top:
            return [base.Order(**item) for item in self._items[:n]]

        return [base.Order(**item) for item in self._items[:-n-1:-1]]

