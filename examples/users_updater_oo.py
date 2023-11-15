class UsersUpdaterOO(object):
    def __init__(self, users):
        self.users = users
    
    def update_users_age(self):
        for user in self.users:
            if 'age' in user:
                user['age'] += 1
        return self.users

    def upgraded_users(self):
        return [user for user in self.users if user['upgraded']]
    
    def add_user(self, new_user):
        self.users.append(new_user)

    def delete_user(self, attribute, value):
        self.users = [user for user in self.users if user.get(attribute) != value]
