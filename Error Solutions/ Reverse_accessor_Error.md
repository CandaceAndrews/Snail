`ERRORS:
auth.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'auth.User.groups' clashes with reverse accessor for 'webtoon_app.User.groups'.`


 - Solution:
 ```
	AUTH_USER_MODEL = 'YourAppName.YourClassName'
 ```