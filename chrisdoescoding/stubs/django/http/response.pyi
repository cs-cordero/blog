from typing import Any, Optional, Union

class HttpResponseBase:
    def __init__(
        self,
        content_type: Optional[str] = None,
        status: Optional[int] = None,
        reason: Optional[str] = None,
        charset: Optional[str] = None,
    ) -> None: ...

class HttpResponse(HttpResponseBase):
    def __init__(
        self, content: Union[str, bytes] = b"", *args: Any, **kwargs: Any
    ) -> None: ...

class HttpResponseRedirectBase(HttpResponse): ...
class HttpResponseRedirect(HttpResponseRedirectBase): ...
class Http404(Exception): ...
