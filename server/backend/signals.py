from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from backend.models import Template


def generate_code():
    code_text = str()
    code_text += 'from backend.models import Template\n'
    code_text += '\n\nclass Messages():\n'
    for message in Template.messages.all():
        code_text += f'    {message.title} = Template.messages.get(id={message.id})\n'

    code_text += '\n\nclass Keys():\n'
    for key in Template.keys.all():
        code_text += f'    {key.title} = Template.keys.get(id={key.id})\n'

    code_text += '\n\nclass Smiles():\n'
    for smile in Template.smiles.all():
        code_text += f'    {smile.title} = Template.smiles.get(id={smile.id})\n'

    return code_text


@receiver(post_save, sender=Template)
def template_post_save_handler(instance, **kwargs):
    template_file = 'backend/templates.py'
    with open(template_file, 'w') as file:
        file.write(generate_code())


@receiver(post_delete, sender=Template)
def template_post_delete_handler(instance, **kwargs):
    template_file = 'backend/templates.py'
    with open(template_file, 'w') as file:
        file.write(generate_code())
