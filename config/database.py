import os

config = {
    'mysql': {
        'driver': os.getenv('DB_DRIVER'),
        'host': os.getenv('DB_HOST'),
        'database': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USERNAME'),
        'password': os.getenv('DB_PASSWORD')
    },
}
