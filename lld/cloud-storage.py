from dataclasses import dataclass

@dataclass
class CloudStorageCard:
    name: str
    size: int

    def validate_name(self):
        if not self.name or not self.name.strip():
            return False
        return True


    def validate_size(self):
        if self.size < 0:
            return False
        return True

    def validate(self):
        return self.validate_name() and self.validate_size()


class CloudStorageManager:
    def __init__(self):
        self.cards = []

    def add_card(self, card: CloudStorageCard):
        if card.validate():
            self.cards.append(card)
            return True
        return False

    def get_cards(self):
        return self.cards

    def get_card_by_name(self, name: str):
        for card in self.cards:
            if card.name == name:
                return card
        return None

    def copy_card(self, name: str):
        card = self.get_card_by_name(name)
        if card:
            copied_card = CloudStorageCard(name=card.name, size=card.size)
            self.cards.append(copied_card)
            return True
        return False