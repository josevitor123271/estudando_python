# Utilizando a busca binária com recursividade juntamente com a classe Array

import array
from typing import Union

class Array:
    '''Return a new array whose items are restricted by typecode, and
       that can contain at most `size` elements.

       Arrays behave very much like Python list, except that
       the type of objects stored in them is constrained. The type is specified
       at object creation time by using a type code, which is a single character.
       The following type codes are defined:

           Type code   C Type             Minimum size in bytes
           'b'         signed integer     1
           'B'         unsigned integer   1
           'u'         Unicode character  2
           'h'         signed integer     2
           'H'         unsigned integer   2
           'i'         signed integer     2
           'I'         unsigned integer   2
           'l'         signed integer     4
           'L'         unsigned integer   4
           'q'         signed integer     8
           'Q'         unsigned integer   8
           'f'         floating point     4
           'd'         floating point     8

        Parameters:
            max_capacity (int): The maximum number of elements the array can hold.
            typecode (str, optional): The typecode of the array. Defaults to 'l' for int.

       '''

    def __init__(self, size: int, typecode: str = 'l'):
        if size <= 0:
            raise ValueError(f'Invalid array size (must be positive): {size}')
        self._size = 0
        self._capacity = size
        self._array = array.array(typecode, [0] * size)


    def __len__(self):
        '''
        Return the number of elements in the array.

        Parameters:
            None

        Returns:
            int: The number of elements in the array.
        '''

        return self._size


    def __getitem__(self, index: int) -> Union[int, float]:
        '''
        Get the value at the given index.

        Parameters:
            index (int): The index to get the value from.

        Returns:
            Union[int, float]: The value at the given index.
        '''

        if index < 0 or index >= self._size:
            raise IndexError('array index out of range')
        return self._array[index]


    def __setitem__(self, index: int, val: Union[int, float]) -> None:
        '''
        Set the value at the given index.

        Parameters:
            index (int): The index to set the value at.
            val (Union[int, float]): The value to set.

        Returns:
            None
        '''

        if index < 0 or index >= self._size:
            raise IndexError('array assignment index out of range')
        self._array[index] = val


    def __repr__(self):
        '''
        Return the string representation of the array.

        Parameters:
            None

        Returns:
            str: The string representation of the array.
        '''

        return repr(self._array)
    
    def append(self, value: Union[int, float]) -> None:
        if self._size >= self._capacity:
            raise ValueError('Stack Overflow')
        self._array[self._size] = value
        self._size += 1

    def binary_search(self, key: Union[int, float]) -> int:
        def _binary_search_recursive(arr, key, left, right):
            if left > right:
                return -1 # Elemento não encontrado
        
            mid = (left+ right) // 2
            if arr[mid] == key:
                return "Elemento {} encontrado no índice: {}".format(key, mid) # Caso base: elemento encontrado
            elif arr[mid] > key:
                return _binary_search_recursive(arr, key, left, mid - 1) # Busca na metade esquerda
            else:
                return _binary_search_recursive(arr, key, mid + 1, right) # Busca na metade direita
        return _binary_search_recursive(self._array, key, 0, self._size - 1)

#  A pesquina binária tem uma complexidade de tempo de O(log n), o que significa que o espaço de pesquisa é reduzido à metade a cada etapa, reduzindo significativamente o número de comparações necessárias.