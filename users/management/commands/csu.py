from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для создания суперпользователя с логином "admin@admin.com" и паролем "12345"."""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.com',
            first_name='Admin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('12345')
        user.save()
