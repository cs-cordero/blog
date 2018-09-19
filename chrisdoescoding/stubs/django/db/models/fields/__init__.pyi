from django.db.models.query_utils import RegisterLookupMixin

import datetime
from typing import Any, Optional, Iterable, Tuple, Callable

# class NOT_PROVIDED: ...
#
# class _Field(RegisterLookupMixin):
#     def __init__(self,
#                  verbose_name: Optional[str] = None,
#                  name: Optional[str] = None,
#                  primary_key: bool = False,
#                  max_length: Optional[int] = None,
#                  unique: bool = False,
#                  blank: bool = False,
#                  null: bool = False,
#                  db_index: bool = False,
#                  default: Any = NOT_PROVIDED,
#                  editable: bool = True,
#                  serialize: bool = True,
#                  unique_for_date: Optional[str] = None,
#                  unique_for_month: Optional[str] = None,
#                  unique_for_year: Optional[str] = None,
#                  choices: Optional[Iterable[Tuple[Any, Any]]] = None,
#                  help_text: str = '',
#                  db_column: Optional[str] = None,
#                  db_tablespace: Optional[str] = None,
#                  auto_created: bool = False,
#                  validators: Iterable[Callable[[Any], None]] = (),
#                  error_messages: Optional[str] = None) -> None: ...
#
# class CharField(Field): ...
# class TextField(Field): ...
# class BooleanField(Field): ...
# class DateTimeCheckMixin: ...
# class DateField(DateTimeCheckMixin, Field):
#     def __init__(self,
#                  verbose_name: Optional[str] = None,
#                  name: Optional[str] = None,
#                  auto_now: bool = False,
#                  auto_now_add: bool = False,
#                  **kwargs: Any) -> None: ...
# class DateTimeField(DateField): ...

# Django's models use descriptors to return primitive python types from the
# Fields, which are difficult to type correctly, so this is an easy way out for
# now.
def Field(*args, **kwargs) -> Any: ...
def CharField(*args, **kwargs) -> str: ...
def TextField(*args, **kwargs) -> str: ...
def BooleanField(*args, **kwargs) -> bool: ...
def DateField(*args, **kwargs) -> datetime.date: ...
def DateTimeField(*args, **kwargs) -> datetime.datetime: ...
