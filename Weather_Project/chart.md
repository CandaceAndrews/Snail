### API ENDPOINT 

| HTTP Verbs | Endpoints                          | Action                                     |
| ---------- | ---------------------------------- | ------------------------------------------ |
| POST       | /login                             | Login or create new user                   |
| POST       | /logout                            | Logout user                                |
| GET        | /\<username\>/home                 | User home page                             |
| PATCH      | /\<username\>/home                 | User edits own attributes                  |
| GET        | /\<username\>/profile              | View another user's profile                |
| GET        | /\<username\>/groups               | List user's groups                         |
| GET        | /\<username\>/open-votes           | List user's events with open voting        |
| POST       | /new/group                         | Create a new group                         |
| GET        | /group/\<group_id\>                | Group home page                            |
| PATCH      | /group/\<group_id\>                | Edit group home page                       |
| PATCH      | /join/\<group_id\>                 | Add user to group                          |
| PATCH      | /leave/\<group_id\>                | User leaves a group                        |
| POST       | /new/event                         | Create a new event for the group           |
| GET        | /event/\<event_id\>                | Event home page                            |
| PATCH      | /event/\<event_id\>                | Update an event                            |
| DELETE     | /event/\<event_id\>                | Delete an event                            |
| PATCH      | /attend/\<event_id\>               | User adds to attending list                |
| PATCH      | /remove-attend/\<event_id\>        | User removes from attending list           |
| POST       | /new/activity                      | Create a new activity for the event        |
| GET        | /activity/\<activity_id\>          | Activity home page                         |
| PATCH      | /activity/\<activity_id\>          | Update an activity                         |
| DELETE     | /activity/\<activity_id\>          | Delete an activity                         |
| PATCH      | /vote/\<vote_id\>                  | User can change vote                       |
| POST       | /submit-vote/                      | User submits votes for an event            |
| POST       | /new/pending-activity              | Create a new pending activity for the user |
| GET        | /pending/<int:pending_activity_id> | Get pending activity                       |
| PATCH      | /pending/<int:pending_activity_id> | Update a pending activity                  |
| DELETE     | /pending/<int:pending_activity_id> | Delete a pending activity                  |