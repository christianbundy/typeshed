from _typeshed import Self
from types import TracebackType
from typing import Any, Container, NamedTuple, Sequence, Text, Union

_Decimal = Union[Decimal, int]
_DecimalNew = Union[Decimal, float, Text, tuple[int, Sequence[int], int]]
_ComparableNum = Union[Decimal, float]

class DecimalTuple(NamedTuple):
    sign: int
    digits: tuple[int, ...]
    exponent: int

ROUND_DOWN: str
ROUND_HALF_UP: str
ROUND_HALF_EVEN: str
ROUND_CEILING: str
ROUND_FLOOR: str
ROUND_UP: str
ROUND_HALF_DOWN: str
ROUND_05UP: str

class DecimalException(ArithmeticError):
    def handle(self, context: Context, *args: Any) -> Decimal | None: ...

class Clamped(DecimalException): ...
class InvalidOperation(DecimalException): ...
class ConversionSyntax(InvalidOperation): ...
class DivisionByZero(DecimalException, ZeroDivisionError): ...
class DivisionImpossible(InvalidOperation): ...
class DivisionUndefined(InvalidOperation, ZeroDivisionError): ...
class Inexact(DecimalException): ...
class InvalidContext(InvalidOperation): ...
class Rounded(DecimalException): ...
class Subnormal(DecimalException): ...
class Overflow(Inexact, Rounded): ...
class Underflow(Inexact, Rounded, Subnormal): ...

def setcontext(__context: Context) -> None: ...
def getcontext() -> Context: ...
def localcontext(ctx: Context | None = ...) -> _ContextManager: ...

class Decimal(object):
    def __new__(cls: type[Self], value: _DecimalNew = ..., context: Context | None = ...) -> Self: ...
    @classmethod
    def from_float(cls, __f: float) -> Decimal: ...
    def __nonzero__(self) -> bool: ...
    def __div__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __rdiv__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __ne__(self, other: object, context: Context | None = ...) -> bool: ...
    def compare(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __hash__(self) -> int: ...
    def as_tuple(self) -> DecimalTuple: ...
    def to_eng_string(self, context: Context | None = ...) -> str: ...
    def __abs__(self, round: bool = ..., context: Context | None = ...) -> Decimal: ...
    def __add__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __divmod__(self, other: _Decimal, context: Context | None = ...) -> tuple[Decimal, Decimal]: ...
    def __eq__(self, other: object, context: Context | None = ...) -> bool: ...
    def __floordiv__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __ge__(self, other: _ComparableNum, context: Context | None = ...) -> bool: ...
    def __gt__(self, other: _ComparableNum, context: Context | None = ...) -> bool: ...
    def __le__(self, other: _ComparableNum, context: Context | None = ...) -> bool: ...
    def __lt__(self, other: _ComparableNum, context: Context | None = ...) -> bool: ...
    def __mod__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __mul__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __neg__(self, context: Context | None = ...) -> Decimal: ...
    def __pos__(self, context: Context | None = ...) -> Decimal: ...
    def __pow__(self, other: _Decimal, modulo: _Decimal | None = ..., context: Context | None = ...) -> Decimal: ...
    def __radd__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __rdivmod__(self, other: _Decimal, context: Context | None = ...) -> tuple[Decimal, Decimal]: ...
    def __rfloordiv__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __rmod__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __rmul__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __rsub__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __rtruediv__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __str__(self, eng: bool = ..., context: Context | None = ...) -> str: ...  # noqa Y029
    def __sub__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __truediv__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def remainder_near(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __float__(self) -> float: ...
    def __int__(self) -> int: ...
    def __trunc__(self) -> int: ...
    @property
    def real(self) -> Decimal: ...
    @property
    def imag(self) -> Decimal: ...
    def conjugate(self) -> Decimal: ...
    def __complex__(self) -> complex: ...
    def __long__(self) -> long: ...
    def fma(self, other: _Decimal, third: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __rpow__(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def normalize(self, context: Context | None = ...) -> Decimal: ...
    def quantize(
        self, exp: _Decimal, rounding: str | None = ..., context: Context | None = ..., watchexp: bool = ...
    ) -> Decimal: ...
    def same_quantum(self, other: _Decimal) -> bool: ...
    def to_integral_exact(self, rounding: str | None = ..., context: Context | None = ...) -> Decimal: ...
    def to_integral_value(self, rounding: str | None = ..., context: Context | None = ...) -> Decimal: ...
    def to_integral(self, rounding: str | None = ..., context: Context | None = ...) -> Decimal: ...
    def sqrt(self, context: Context | None = ...) -> Decimal: ...
    def max(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def min(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def adjusted(self) -> int: ...
    def canonical(self, context: Context | None = ...) -> Decimal: ...
    def compare_signal(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def compare_total(self, other: _Decimal) -> Decimal: ...
    def compare_total_mag(self, other: _Decimal) -> Decimal: ...
    def copy_abs(self) -> Decimal: ...
    def copy_negate(self) -> Decimal: ...
    def copy_sign(self, other: _Decimal) -> Decimal: ...
    def exp(self, context: Context | None = ...) -> Decimal: ...
    def is_canonical(self) -> bool: ...
    def is_finite(self) -> bool: ...
    def is_infinite(self) -> bool: ...
    def is_nan(self) -> bool: ...
    def is_normal(self, context: Context | None = ...) -> bool: ...
    def is_qnan(self) -> bool: ...
    def is_signed(self) -> bool: ...
    def is_snan(self) -> bool: ...
    def is_subnormal(self, context: Context | None = ...) -> bool: ...
    def is_zero(self) -> bool: ...
    def ln(self, context: Context | None = ...) -> Decimal: ...
    def log10(self, context: Context | None = ...) -> Decimal: ...
    def logb(self, context: Context | None = ...) -> Decimal: ...
    def logical_and(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def logical_invert(self, context: Context | None = ...) -> Decimal: ...
    def logical_or(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def logical_xor(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def max_mag(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def min_mag(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def next_minus(self, context: Context | None = ...) -> Decimal: ...
    def next_plus(self, context: Context | None = ...) -> Decimal: ...
    def next_toward(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def number_class(self, context: Context | None = ...) -> str: ...
    def radix(self) -> Decimal: ...
    def rotate(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def scaleb(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def shift(self, other: _Decimal, context: Context | None = ...) -> Decimal: ...
    def __reduce__(self) -> tuple[type[Decimal], tuple[str]]: ...
    def __copy__(self) -> Decimal: ...
    def __deepcopy__(self, memo: Any) -> Decimal: ...
    def __format__(self, specifier: str, context: Context | None = ...) -> str: ...

class _ContextManager(object):
    new_context: Context
    saved_context: Context
    def __init__(self, new_context: Context) -> None: ...
    def __enter__(self) -> Context: ...
    def __exit__(self, t: type[BaseException] | None, v: BaseException | None, tb: TracebackType | None) -> None: ...

_TrapType = type[DecimalException]

class Context(object):
    prec: int
    rounding: str
    Emin: int
    Emax: int
    capitals: int
    _clamp: int
    traps: dict[_TrapType, bool]
    flags: dict[_TrapType, bool]
    def __init__(
        self,
        prec: int | None = ...,
        rounding: str | None = ...,
        traps: None | dict[_TrapType, bool] | Container[_TrapType] = ...,
        flags: None | dict[_TrapType, bool] | Container[_TrapType] = ...,
        Emin: int | None = ...,
        Emax: int | None = ...,
        capitals: int | None = ...,
        _clamp: int | None = ...,
        _ignored_flags: list[_TrapType] | None = ...,
    ) -> None: ...
    def clear_flags(self) -> None: ...
    def copy(self) -> Context: ...
    def __copy__(self) -> Context: ...
    __hash__: Any = ...
    def Etiny(self) -> int: ...
    def Etop(self) -> int: ...
    def create_decimal(self, __num: _DecimalNew = ...) -> Decimal: ...
    def create_decimal_from_float(self, __f: float) -> Decimal: ...
    def abs(self, __x: _Decimal) -> Decimal: ...
    def add(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def canonical(self, __x: Decimal) -> Decimal: ...
    def compare(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def compare_signal(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def compare_total(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def compare_total_mag(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def copy_abs(self, __x: _Decimal) -> Decimal: ...
    def copy_decimal(self, __x: _Decimal) -> Decimal: ...
    def copy_negate(self, __x: _Decimal) -> Decimal: ...
    def copy_sign(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def divide(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def divide_int(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def divmod(self, __x: _Decimal, __y: _Decimal) -> tuple[Decimal, Decimal]: ...
    def exp(self, __x: _Decimal) -> Decimal: ...
    def fma(self, __x: _Decimal, __y: _Decimal, __z: _Decimal) -> Decimal: ...
    def is_canonical(self, __x: _Decimal) -> bool: ...
    def is_finite(self, __x: _Decimal) -> bool: ...
    def is_infinite(self, __x: _Decimal) -> bool: ...
    def is_nan(self, __x: _Decimal) -> bool: ...
    def is_normal(self, __x: _Decimal) -> bool: ...
    def is_qnan(self, __x: _Decimal) -> bool: ...
    def is_signed(self, __x: _Decimal) -> bool: ...
    def is_snan(self, __x: _Decimal) -> bool: ...
    def is_subnormal(self, __x: _Decimal) -> bool: ...
    def is_zero(self, __x: _Decimal) -> bool: ...
    def ln(self, __x: _Decimal) -> Decimal: ...
    def log10(self, __x: _Decimal) -> Decimal: ...
    def logb(self, __x: _Decimal) -> Decimal: ...
    def logical_and(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def logical_invert(self, __x: _Decimal) -> Decimal: ...
    def logical_or(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def logical_xor(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def max(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def max_mag(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def min(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def min_mag(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def minus(self, __x: _Decimal) -> Decimal: ...
    def multiply(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def next_minus(self, __x: _Decimal) -> Decimal: ...
    def next_plus(self, __x: _Decimal) -> Decimal: ...
    def next_toward(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def normalize(self, __x: _Decimal) -> Decimal: ...
    def number_class(self, __x: _Decimal) -> str: ...
    def plus(self, __x: _Decimal) -> Decimal: ...
    def power(self, a: _Decimal, b: _Decimal, modulo: _Decimal | None = ...) -> Decimal: ...
    def quantize(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def radix(self) -> Decimal: ...
    def remainder(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def remainder_near(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def rotate(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def same_quantum(self, __x: _Decimal, __y: _Decimal) -> bool: ...
    def scaleb(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def shift(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def sqrt(self, __x: _Decimal) -> Decimal: ...
    def subtract(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def to_eng_string(self, __x: _Decimal) -> str: ...
    def to_sci_string(self, __x: _Decimal) -> str: ...
    def to_integral_exact(self, __x: _Decimal) -> Decimal: ...
    def to_integral_value(self, __x: _Decimal) -> Decimal: ...
    def to_integral(self, __x: _Decimal) -> Decimal: ...

DefaultContext: Context
BasicContext: Context
ExtendedContext: Context
