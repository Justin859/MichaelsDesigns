import os

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'michaelsdesignsza'
AWS_QUERYSTRING_AUTH = False

# Email settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp-mail.outlook.com"
EMAIL_HOST_USER = "yourdeveloper@outlook.com"
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Mail Chimp

SECRET_API_KEY = os.environ.get('SECRET_API_KEY')
SECRET_LIST_KEY = os.environ.get('SECRET_LIST_KEY')

# Django

SECRET_KEY = os.environ.get('SECRET_KEY')