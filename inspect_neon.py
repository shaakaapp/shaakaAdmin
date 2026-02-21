import os
import django
from django.conf import settings
from django.core.management import call_command

settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'neondb',
            'USER': 'neondb_owner',
            'PASSWORD': 'npg_ZPjzbf7Nx6Kv',
            'HOST': 'ep-bold-bonus-a1abfgjo-pooler.ap-southeast-1.aws.neon.tech',
            'PORT': '5432',
            'OPTIONS': {
                'sslmode': 'require',
            }
        }
    },
    INSTALLED_APPS=[]
)

django.setup()

with open('models.py', 'w', encoding='utf-8') as f:
    call_command('inspectdb', stdout=f)

print("Database introspection complete. Models written to models.py")
