## instructions

## objectives that achieved:

### Primary objectives
- Create, update and delete (CRUD) todo-lists
    Api url endpoints: `/api/todo_lists/` to `GET` Todo lists and `POST` new Todo lists 
    (when calling this endpoint, the payload will include nested attributes for todo-items as requested)
                    `/api/todo_lists/{todoList_Id}` to 1) `GET` one specific todo-list details 
                                                       2) `PUT` to update specific todo-list
                                                       3) `DELETE` to delete specific todo-list
                

- Create, update and delete todo-items, which are associated with todo-lists
    Set todo-lists as foreign key of todo-items
    Api url endpoints: `/api/todo_items/` to `GET` todo-items and `POST` new todo-items
                    `/api/todo_items/{todoItem_Id}` to 1) `GET` one specific todo-item details 
                                                       2) `PUT` to update specific todo-items
                                                       3) `DELETE` to delete specific todo-items

- Allow todo-lists to be tagged with zero or more tags.
    `Tags` field has been added to todo-lists with zero or more tags avaliable.

- Check and un-check todo-items.
    `Completed` field has been added to todo-lists and can be checked or unchecked

### Secondary objectives
- Associate todo-lists with users, such that only permitted users may operate on their own todo-lists.
    Setting `User` as foreign key of todo-lists to associtate them together
    Created a api endpoint: `/api/users/` to `GET` user lists and `POST` new user
        When you call this endpoint, the return payload will show `todo_lists` that been created by this user and also, 
        when you call `/api/todo_lists/` related endpoints the return payload will show `user.username` as the creator of the list

- Create unit tests and run them with `python manage.py test`
    unit tests includes 9 tests including testing CRUD operations of todo-lists and todo-items, and when deleting todo-list, the associated todo-items will be deleted automatically.

- Configure the admin console
    admin console endpoint: `/admin`: you are able to edit todo-lists, todo-items, and users in the console

