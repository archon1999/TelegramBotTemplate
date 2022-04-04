from backend.models import Template


class Messages():
    MESSAGE = Template.messages.get(id=1)
    START_COMMAND = Template.messages.get(id=4)


class Keys():
    KEY = Template.keys.get(id=2)


class Smiles():
    SMILES = Template.smiles.get(id=3)
