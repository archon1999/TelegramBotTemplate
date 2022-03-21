from backend.models import Template


class Messages():
    MESSAGE = Template.messages.get(id=1)


class Keys():
    KEY = Template.keys.get(id=2)


class Smiles():
    SMILES = Template.smiles.get(id=3)
