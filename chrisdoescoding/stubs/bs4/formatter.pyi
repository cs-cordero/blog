from typing import Any, Optional

from bs4.dammit import EntitySubstitution as EntitySubstitution

class Formatter(EntitySubstitution):
    XML_FORMATTERS: Any = ...
    HTML_FORMATTERS: Any = ...
    HTML: str = ...
    XML: str = ...
    HTML_DEFAULTS: Any = ...
    language: Any = ...
    entity_substitution: Any = ...
    void_element_close_prefix: Any = ...
    cdata_containing_tags: Any = ...
    def __init__(
        self,
        language: Optional[Any] = ...,
        entity_substitution: Optional[Any] = ...,
        void_element_close_prefix: str = ...,
        cdata_containing_tags: Optional[Any] = ...,
    ) -> None: ...
    def substitute(self, ns: Any): ...
    def attribute_value(self, value: Any): ...
    def attributes(self, tag: Any): ...

class HTMLFormatter(Formatter):
    REGISTRY: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class XMLFormatter(Formatter):
    REGISTRY: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...