from app import app
import os

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://diana:1234@localhost:5432/postgres'
app.secret_key = b'1234'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
