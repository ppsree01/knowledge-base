from dataclasses import dataclass

@dataclass
class CloudStorageCard:
    name: str
    size: int

    def validate_size(self):
        return self.size > 0 

    def validate_name(self):
        if not self.name or not self.name.strip():
            return False
        return True

    def validate(self):
        return self.validate_name() and self.validate_size() 

    def copy(self):
        return CloudStorageCard(name=self.name, size=self.size)

class CloudStorage:

    def __init__(self):
        self.store = []

    def add_file(self, name: str, size: int) -> bool:
        data = CloudStorageCard(name=name, size=size)
        if data.validate():
            index = self.find_file(name)
            if index != -1:
                return False
            self.store.append(data)
            self.store = sorted(self.store, key=lambda x: x.name)
            return True
        return False

    def copy_file(self, name_from: str, name_to: str) -> bool:
        if not name_from or not name_from.strip() or not name_to or not name_to.strip():
            return False
        index_name_from = self.find_file(name_from)
        index_name_to = self.find_file(name_to)

        if index_name_from == -1 or index_name_to != -1:
            return False

        data = self.store[index_name_from].copy()
        self.store.append(data)
        self.store = sorted(self.store, key=lambda x: x.name)
        return True

    def get_file_size(self, name: str) -> int | None:
        if not name or not name.strip():
            return False

        index = self.find_file(name)
        if index == -1:
            return None
        return self.store[index].size

    def display(self):
        for data in self.store:
            print(f"{data.name} - {data.size}")

    def find_file(self, name: str) -> int:
        try:
            if len(self.store) == 0:
                return -1

            start, end = 0, len(self.store) - 1

            while start <= end:
                mid = (start + end) // 2

                if mid == start:
                    if self.store[start].name == name:
                        return start
                    elif self.store[end].name == name:
                        return end
                    return -1

                if self.store[mid].name == name:
                    return mid

                elif name > self.store[mid].name:
                    start = mid
                else:
                    end = mid
            return -1
        except Exception:
            print("Exception occurred")

    