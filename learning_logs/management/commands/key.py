from random import choice, randrange

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'change or add SECRET_KEY for learning_log.settings'

    def handle(self, *args, **options):
        self.stdout.write("Loading...")
        char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', 
        '2', '3', '4', '5', '6', '7', '8', '9', '`', '~', '!', '@', '#', '$', 
        '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', 
        '\\', '|', ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?']
        secret_key = ''

        self.stdout.write("Generating SECRET_KEY...")
        for x in range(0, randrange(32, 64)):
            secret_key += choice(char)

        self.stdout.write("Writing SECRET_KEY to learning_log/secret_key.txt...")
        with open('learning_log/secret_key.txt', 'wt') as f:
            f.write(secret_key)
            
        self.stdout.write("Change or add SECRET_KEY is OK.Restart the server to update the SECRET_KEY\nExiting...")