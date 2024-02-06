import ctypes
from typing import Generic, TypeVar

T = TypeVar('T')


class DynamicArray(Generic[T]):
    def __init__(self) -> None:
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def _make_array(self, c: int) -> ctypes.Array[ctypes.py_object[T]]:
        return (c * ctypes.py_object[T])()

    def __len__(self) -> int:
        return self._n

    def __getitem__(self, k: int) -> ctypes.py_object[T]:
        if not 0 <= k < self._n:
            raise IndexError('Invalid index')
        value = self._A[k]
        return value  # type: ignore[return-value]

    def append(self, obj: T) -> None:
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, n: int) -> None:
        B = self._make_array(n)
        for k in range(self._n):
            B[k] = self._A[k]  # type: ignore[assignment]
        self._A = B
        self._capacity = n
