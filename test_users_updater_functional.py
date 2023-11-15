from users_updater.users_updater_functional import *

class TestUsersUpdaterFunctional():    
    def test_it_runs(self):
        return
    
    def test_it_returns_users(self):
        users = [
            {'age': 90,
            'name': 'Zebedee',
            'upgraded': False,
            'transaction_ids': [10000, 10001]},
            {'age': 22,
            'name': 'Dolly',
            'upgraded': True,
            'transaction_ids': [11000, 11001]}
        ]

        assert get_users(users) == users

    def test_it_increments_user_ages(self):
        users = [
            {'age': 90,
            'name': 'Zebedee',
            'upgraded': False,
            'transaction_ids': [10000, 10001]},
            {'age': 22,
            'name': 'Dolly',
            'upgraded': True,
            'transaction_ids': [11000, 11001]}
        ]

        updated_users = [
            {'age': 91,
            'name': 'Zebedee',
            'upgraded': False,
            'transaction_ids': [10000, 10001]},
            {'age': 23,
            'name': 'Dolly',
            'upgraded': True,
            'transaction_ids': [11000, 11001]}
        ]

        assert update_users_age(users) == updated_users

    def test_it_returns_upgraded_users(self):
        users = [
            {'age': 90,
            'name': 'Zebedee',
            'upgraded': False,
            'transaction_ids': [10000, 10001]},
            {'age': 22,
            'name': 'Dolly',
            'upgraded': True,
            'transaction_ids': [11000, 11001]}
        ]

        upgraded_users_list = [
            {'age': 22,
            'name': 'Dolly',
            'upgraded': True,
            'transaction_ids': [11000, 11001]}
        ]
        assert upgraded_users(users) == upgraded_users_list

    def test_it_adds_a_new_user(self):
        users = [
            {'age': 90,
            'name': 'Zebedee',
            'upgraded': False,
            'transaction_ids': [10000, 10001]},
            {'age': 22,
            'name': 'Dolly',
            'upgraded': True,
            'transaction_ids': [11000, 11001]}
        ]
        new_user = {'age': 34,
            'name': 'Mr Lucky',
            'upgraded': False,
            'transaction_ids': []}

        updated_users = [
            {'age': 90,
            'name': 'Zebedee',
            'upgraded': False,
            'transaction_ids': [10000, 10001]},
            {'age': 22,
            'name': 'Dolly',
            'upgraded': True,
            'transaction_ids': [11000, 11001]},
            new_user
        ]

        assert add_user(users, new_user) == updated_users

    def test_it_deletes_a_user(self):
        users = [
            {'age': 90,
            'name': 'Zebedee',
            'upgraded': False,
            'transaction_ids': [10000, 10001]},
            {'age': 22,
            'name': 'Dolly',
            'upgraded': True,
            'transaction_ids': [11000, 11001]}
        ]
        updated_users = [
            {'age': 22,
            'name': 'Dolly',
            'upgraded': True,
            'transaction_ids': [11000, 11001]}
        ]

        assert delete_user(users, 'name', 'Zebedee') == updated_users