from orator.migrations import Migration


class Users(Migration):

    def up(self):
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('username')
            table.string('email')
            table.string('password')

    def down(self):
        self.schema.drop_if_exists('users')
