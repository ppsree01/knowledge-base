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
