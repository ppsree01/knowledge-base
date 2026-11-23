from cloud_storage_card import CloudStorageCard
from typing import List

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

        data = CloudStorageCard(name=name_to, size=self.store[index_name_from].size)
        self.store.append(data)
        self.store.sort(key=lambda x: x.name)
        return True

    def get_file_size(self, name: str) -> int | None:
        if not name or not name.strip():
            return None

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

                if self.store[mid].name == name:
                    return mid

                elif name > self.store[mid].name:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        except Exception:
            print("Exception occurred")
            return -1

    def find_by_prefix_and_suffix(self, prefix: str, suffix: str) -> List[str]:
        result = []
        if len(self.store) == 0:
            return result
        elif len(self.store) == 1:
            item = self.store[0]
            if item.name.startswith(prefix) and item.name.endswith(suffix):
                return [f"{item.name}({item.size})"]
            return result

        store = sorted(self.store, key=lambda x: (-x.size, x.name))
        for item in store:
            if item.name.startswith(prefix) and item.name.endswith(suffix):
                result.append(f"{item.name}({item.size})")

        return result


