# Users Updater

A project to demonstrate best practices in OO and Functional programming.

## Requirements

Implement functionality to:

- Increment the age of all users
- Return a list of upgraded users
- Create a new user
- Delete an existing user
- Add transaction id 88888 to all upgraded users
- Upgrade/downgrade a user

### OO

- Model the data as a real world object
- Create an object, and then mutate it to achieve the desired result

Extended:

- Use the constructor pattern when creating users
- Refactor the code so that upgraded users are subtypes of 'User'

### FP

- Do not mutate any data
- Avoid assigning state
- If loops are used, try replacing them with recursion
- Try out map, filter, and reduce functions
