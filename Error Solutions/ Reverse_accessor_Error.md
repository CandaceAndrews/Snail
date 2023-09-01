`ERRORS:
auth.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'auth.User.groups' clashes with reverse accessor for 'webtoon_app.User.groups'.
	HINT: Add or change a related_name argument to the definition for 'auth.User.groups' or 'webtoon_app.User.groups'.
auth.User.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 'auth.User.user_permissions' clashes with reverse accessor for 'webtoon_app.User.user_permissions'.
	HINT: Add or change a related_name argument to the definition for 'auth.User.user_permissions' or 'webtoon_app.User.user_permissions'.
webtoon_app.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'webtoon_app.User.groups' clashes with reverse accessor for 'auth.User.groups'.
	HINT: Add or change a related_name argument to the definition for 'webtoon_app.User.groups' or 'auth.User.groups'.
webtoon_app.User.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 'webtoon_app.User.user_permissions' clashes with reverse accessor for 'auth.User.user_permissions'.
	HINT: Add or change a related_name argument to the definition for 'webtoon_app.User.user_permissions' or 'auth.User.user_permissions'.`


 - Solution:
 ```
	AUTH_USER_MODEL = 'YourAppName.YourClassName'
 ```