class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item):
        if self.__capacity > len(self.items):
            self.items.append(item)
        return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        item = ', '.join([el for el in self.items])
        diff = self.__capacity - len(self.items)
        return f'Items: {item}.\nCapacity left: {diff}'