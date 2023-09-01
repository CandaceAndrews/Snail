### Heroku

`CommandError: This command only runs when DEBUG is set to True.`

The error message indicates that the seed_data command can only be run when DEBUG is set to True in your Django settings. To run the command on Heroku, you can temporarily set the DEBUG environment variable to True using the heroku config:set command. Here's an example:

```
heroku config:set DEBUG=True
heroku run python manage.py seed_data
```

After running the seed_data command, you can unset the DEBUG environment variable:

```
heroku config:unset DEBUG

```

Note that running with DEBUG=True in a production environment is not recommended, so make sure to unset the environment variable after running the command.