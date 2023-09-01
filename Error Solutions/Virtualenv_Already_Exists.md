`ERROR:: --system is intended to be used for pre-existing Pipfile installation, not installation of specific packages. Aborting.`

- Solution:

```
# Remove existing virtualenv
cd ~/.local/share/virtualenvs
rm -rf dir_python-5Rka8dPB
```

Happens when you delete a project and then have another with the same name. Causes a conflict with virtualenv. You must remove the old one before you can create the new.