#!/usr/bin/env python3

import secrets
import sys

config = {}
further_instructions = []

output_filepath = './.env'
if len(sys.argv) > 1:
    output_filepath = sys.argv[1]

input_base_url = input('Base URL [https://malwear.org]:').strip()
if not input_base_url:
    input_base_url = 'https://malwear.org'
config['BASE_URL'] = input_base_url

input_secret = input('Secret Key (leave blank to auto-generate): ').strip()
if input_secret:
    config['SECRET_KEY'] = input_secret
else:
    config['SECRET_KEY'] = secrets.token_hex(64)

input_session_timeout = input('Session Timeout in Minutes [30]: ').strip()
if not input_session_timeout:
    input_session_timeout = 30
config['SESSION_TIMEOUT_MINUTES'] = input_session_timeout

input_db_type = input('Database Type [sqlite] (sqlite/postgres/mysql): ').strip()
if not input_db_type:
    input_db_type = 'sqlite'

if input_db_type == 'sqlite':
    input_db_name = input('Database filepath [./malwear.db]: ').strip()
    if not input_db_name:
        input_db_name = './malwear.db'
    config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{input_db_name}'

elif input_db_type == 'postgres':
    input_db_driver = input('PostgreSQL Driver [psycopg2]: ').strip()
    if not input_db_driver:
        further_instructions.append('Ensure the psycopg2 driver is installed in the virtual environment.')
        input_db_driver = ''
    else:
        further_instructions.append(f'Ensure the {input_db_driver} driver is installed in the virtual environment.')
        input_db_driver = f'+{input_db_driver}'
    input_db_host = input('PostgreSQL Host [localhost:5432]: ').strip()
    if not input_db_host:
        input_db_host = 'localhost:5432'
    input_db_name = input('PostgreSQL Database Name [malwear]: ').strip()
    if not input_db_name:
        input_db_name = 'malwear'
    input_db_user = input('PostgreSQL User [malwear]: ').strip()
    if not input_db_user:
        input_db_user = 'malwear'
    input_db_pass = input(f'PostgreSQL Password [{input_db_user}]: ').strip()
    if not input_db_pass:
        input_db_pass = input_db_user
    config['SQLALCHEMY_DATABASE_URI'] = f'postgresql{input_db_driver}://{input_db_user}:{input_db_pass}' \
                                        f'@{input_db_host}/{input_db_name}'

elif input_db_type == 'mysql':
    input_db_driver = input('MySQL Driver [mysql-python]: ').strip()
    if not input_db_driver:
        further_instructions.append('Ensure the mysql-python driver is installed in the virtual environment.')
        input_db_driver = ''
    else:
        further_instructions.append(f'Ensure the {input_db_driver} driver is installed in the virtual environment.')
        input_db_driver = f'+{input_db_driver}'
    input_db_host = input('MySQL Host [localhost:3306]: ').strip()
    if not input_db_host:
        input_db_host = 'localhost:3306'
    input_db_name = input('MySQL Database Name [malwear]: ').strip()
    if not input_db_name:
        input_db_name = 'malwear'
    input_db_user = input('MySQL User [malwear]: ').strip()
    if not input_db_user:
        input_db_user = 'malwear'
    input_db_pass = input(f'MySQL Password [{input_db_user}]: ').strip()
    if not input_db_pass:
        input_db_pass = input_db_user
    config['SQLALCHEMY_DATABASE_URI'] = f'mysql{input_db_driver}://{input_db_user}:{input_db_pass}' \
                                        f'@{input_db_host}/{input_db_name}'

input_mail_server = input('SMTP Server [smtp.sendgrid.net]: ')
if not input_mail_server:
    input_mail_server = 'smtp.sendgrid.net'
config['MAIL_SERVER'] = input_mail_server

input_mail_username = input('SMTP Username [apikey]: ')
if not input_mail_username:
    input_mail_username = 'apikey'
config['MAIL_USERNAME'] = input_mail_username

input_mail_password = ''
while not input_mail_password:
    input_mail_password = input('SMTP Password: ').strip()
config['MAIL_PASSWORD'] = input_mail_password

input_mail_default_sender = input('SMTP From Address [malwear.org <no-reply@malwear.org>]: ')
if not input_mail_default_sender:
    input_mail_default_sender = 'malwear.org <no-reply@malwear.org>'
config['MAIL_DEFAULT_SENDER'] = input_mail_default_sender

print()

with open(output_filepath, 'w') as f:
    for key, value in config.items():
        print(f'{key}={value}')
        f.write(f'{key}={value}\n')
    f.close()

if further_instructions:
    print()
    for line in further_instructions:
        print(line)

print()
