from orator.migrations import Migration


class Tokens(Migration):

    def up(self):
        with self.schema.create('auth_tokens') as table:
            table.increments('id')
            table.integer('user_id')
            table.text('token')
            table.timestamp('expire_time')
            table.timestamp('created_at').nullable()

    def down(self):
        self.schema.drop_if_exists('auth_tokens')