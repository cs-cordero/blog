from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from django.db.models.manager import Manager

class QuerySet:
    def as_manager(self, *args: Any, **kwargs: Any) -> Any: ...
    def filter(self, *args: Any, **kwargs: Any) -> 'QuerySet': ...
    def order_by(self, *args: Any, **kwargs: Any) -> 'QuerySet': ...
    def earliest(self, *args: Any, **kwargs: Any) -> Any: ...
    def latest(self, *args: Any, **kwargs: Any) -> Any: ...
    def __len__(self) -> int: ...
    def __getitem__(self, k: int) -> Any: ...