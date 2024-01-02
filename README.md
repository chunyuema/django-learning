# django-learning
![img.png](img.png)


## django template
- `{{ var }}` to add variable
- `{% ... %}` to add logic such as for loop / if clause
- `{# ... #}` for comment
- `{{ var | 过滤器}}` used to modify the variable here

## django models
```commandline
from django.db import models
```
- primary key is auto generated if not provided
- logic delete v.s. physical delete
  - logic delete is setting `is_delete` to True, the data is still present in the data base
  - physical delete means the data will be removed from the database
- common field types
  - `AutoField`
  - `CharField`
  - `TextField`
  - `IntegerField`
  - `DecimalField`
  - `FloatField`
  - `BooleanField`
  - `DateField`
  - `TimeField`
  - `DateTimeField`
  - `FieldField`: used for file (less common) => use object storage
  - `ImageField`: used for image (less common) => use object storage
- common filed type arguments: 
  - `null = True`: can be null
  - `blank = True`: 
  - `primary_key = True`: set a field to be primary key
  - `DateField.auto_now`: when the object was last modified
  - `DateField.auto_now_add`: when the object was first created
  - `choices`
  - `max_length`
  - `default`
  - `name|db_column`
  - `unique = True`
  - `db_index = True`
