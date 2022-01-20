from typing import Any, Callable, Literal, Mapping, Union

def get_platform() -> str: ...
def convert_path(pathname: str) -> str: ...
def change_root(new_root: str, pathname: str) -> str: ...
def check_environ() -> None: ...
def subst_vars(s: str, local_vars: Mapping[str, str]) -> None: ...
def split_quoted(s: str) -> list[str]: ...
def execute(
    func: Callable[..., None], args: tuple[Any, ...], msg: str | None = ..., verbose: bool = ..., dry_run: bool = ...
) -> None: ...
def strtobool(val: str) -> Union[Literal[0], Literal[1]]: ...
def byte_compile(
    py_files: list[str],
    optimize: int = ...,
    force: bool = ...,
    prefix: str | None = ...,
    base_dir: str | None = ...,
    verbose: bool = ...,
    dry_run: bool = ...,
    direct: bool | None = ...,
) -> None: ...
def rfc822_escape(header: str) -> str: ...
