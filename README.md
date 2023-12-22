# Little Lemon Web Application for Meta Back-End Developer Capstone Project

## Evaluate the following points:

- Does the web application use Django to serve static HTML content?

- Has the learner committed the project to a Git repository?

- Does the application connect the backend to a MySQL database?

- Are the menu and table booking APIs implemented?

- Is the application set up with user registration and authentication?

- Does the application contain unit tests?

- Can the API be tested with the Insomnia REST client?

## Please configure the database if necessary

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LittleLemon',     # change to your littlelemon database name if necessary
        'USER': 'root',            # change to your user name if necessary
        'PASSWORD': 'Root123@!',   # change to your user password
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

## API paths

- Check/Add users: `/auth/users/`

- Check menu items/add a menu item: `/restaurant/menu/`

- Check/modify/delete an existing menu item: `/restaurant/menu/:id`

- Check booking tables/add a booking table: `/restaurant/booking/tables/`

- Check/modify/delete an existing booking table: `/restaurant/booking/tables/:id/`

## Note

- Unit testing is implemented in Menu APIs.

- Bearer token authorization is implemented in Booking APIs.
