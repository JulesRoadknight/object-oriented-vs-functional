def get_users(users):
    return users

def update_users_age(users):
    return [
        {
            'age': user['age'] + 1,
            'name': user['name'],
            'upgraded': user['upgraded'],
            'transaction_ids': user['transaction_ids']
        }
        for user in users
    ]

def upgraded_users(users):
    return list(filter(lambda user: user.get('upgraded', False), users))

def add_user(users, new_user):
    return [*users, new_user]

def delete_user(users, attribute, value):
    return list(filter(lambda user: user.get(attribute) != value, users))
