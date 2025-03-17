import array
from typing import Union

class Array:
    '''Retorna um novo array cujos itens são restritos por typecode, e
       que pode conter no máximo `size` elementos.

       Arrays se comportam muito como listas Python, exceto que
       o tipo de objetos armazenados neles é restrito. O tipo é especificado
       no momento da criação do objeto usando um type code, que é um único caractere.
       Os seguintes type codes são definidos:

           Type code   Tipo C             Tamanho mínimo em bytes
           'b'         inteiro com sinal  1
           'B'         inteiro sem sinal  1
           'u'         caractere Unicode  2
           'h'         inteiro com sinal  2
           'H'         inteiro sem sinal  2
           'i'         inteiro com sinal  2
           'I'         inteiro sem sinal  2
           'l'         inteiro com sinal  4
           'L'         inteiro sem sinal  4
           'q'         inteiro com sinal  8
           'Q'         inteiro sem sinal  8
           'f'         ponto flutuante    4
           'd'         ponto flutuante    8

        Parâmetros:
            max_capacity (int): O número máximo de elementos que o array pode conter.
            typecode (str, opcional): O typecode do array. O padrão é 'l' para int.

       '''

    def __init__(self, size: int, typecode: str = 'l'):
        if size <= 0:
            raise ValueError(f'Tamanho do array inválido (deve ser positivo): {size}')
        self._size = size
        self._array = array.array(typecode, [0] * size)


    def __len__(self):
        '''
        Retorna o número de elementos no array.

        Parâmetros:
            Nenhum

        Retorna:
            int: O número de elementos no array.
        '''

        return self._size


    def __getitem__(self, index: int) -> Union[int, float]:
        '''
        Obtém o valor no índice fornecido.

        Parâmetros:
            index (int): O índice para obter o valor.

        Retorna:
            Union[int, float]: O valor no índice fornecido.
        '''

        if index < 0 or index >= self._size:
            raise IndexError('índice do array fora do intervalo')
        return self._array[index]


    def __setitem__(self, index: int, val: Union[int, float]) -> None:
        '''
        Define o valor no índice fornecido.

        Parâmetros:
            index (int): O índice para definir o valor.
            val (Union[int, float]): O valor a ser definido.

        Retorna:
            Nenhum
        '''

        if index < 0 or index >= self._size:
            raise IndexError('índice de atribuição do array fora do intervalo')
        self._array[index] = val


    def __repr__(self):
        '''
        Retorna a representação em string do array.

        Parâmetros:
            Nenhum

        Retorna:
            str: A representação em string do array.
        '''

        return repr(self._array)

# Estrutura desordenada - Implementando métodos de ordenação
class UnsortedArray:
    def __init__(self, max_size=10, typecode = 'l'):
        self._array = Array(max_size, typecode)
        self._max_size = max_size
        self._size = 0
    
    def insert(self, new_entry):
        if self._size >= self._max_size:
            raise ValueError('Array está cheio')
        self._array[self._size] = new_entry
        self._size += 1
    
    def __repr__(self):
        return "UnsortedArray(size={}, array={})".format(self._size, self._array)
    
    # Implementando métodos de ordenação
    # def bubble_sort()
    # def insertion_sort()
    # def selection_sort()
    # def quick_sort()
    # def merge_sort()

    # Bubble Sort - Ordenação por bolha (Troca)
    def bubble_sort(self):
        n = self._size
        for i in range(n):
            swapped = False
            for j in range(0, n - 1 - i):

                # Swap if the element found is greater than the next element
                if self._array[j] > self._array[j + 1]:
                    self._array[j], self._array[j + 1] = self._array[j + 1], self._array[j]
                    swapped = True
            if not swapped:
                break
    
    # Insertion Sort - Ordenação por inserção
    def insertion_sort(self):
        n = len(self._array)

        if n <= 1:
            return
        
        for i in range(1, n):
            key = self._array[i]
            j = i - 1
            while j>= 0 and key < self._array[j]:
                self._array[j + 1] = self._array[j]
                j -= 1
            self._array[j + 1] = key
    
    # Selection Sort - Ordenação por seleção
    def selection_sort(self, size):
        for ind in range(size):
            min_index = ind
            
            for j in range(ind + 1, size):
                if self._array[j] < self._array[min_index]:
                    min_index = j
            
            # Swap the found minimum element with the first element
            (self._array[ind], self._array[min_index]) = (self._array[min_index], self._array[ind])
    
    # Merge Sort - Ordenação por intercalação
    def merge_sort(self, l=None, r=None):
        if l is None:
            l = 0
        if r is None:
            r = self._size - 1
        
        # Caso base: se o tamanho do array for 1 ou 0, ele já estar ordenado - então retorne nada
        if l < r:
            m = l + (r - l) // 2

            # Dividr: Ordenar a primeira e a segunda metade
            self.merge_sort(l, m)
            self.merge_sort(m + 1, r)

            # Conquistar: Juntar as metades ordenadas
            self.merge(l, m, r)
    
    def merge(self, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # Criar arrays temporários
        L = [0] * n1
        R = [0] * n2

        # Copia os dados para os arrays temporários L[] e R[]
        for i in range(n1):
            L[i] = self._array[l + i]
        
        for j in range(n2):
            R[j] = self._array[m + 1 + j]
        
        # Mesclar os arrays temporários de volta para arr[l..r]
        i = 0 # Índice inicial do primeiro subarray
        j = 0 # Índice inicial do segundo subarray
        k = l # Índice inicial do subarray mesclado

        # Enquanto houver elementos em L[] e R[], copie o menor dos dois
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                self._array[k] = L[i]
                i += 1
            else:
                self._array[k] = R[j]
                j += 1
            k += 1
        
        # Copie os elementos restantes de L[], se houver algum
        while i < n1:
            self._array[k] = L[i]
            i += 1
            k += 1
        
        # # Copie os elementos restantes de R[], se houver algum
        while j < n2:
            self._array[k] = R[j]
            j += 1
            k += 1
    
    # Quick Sort - Ordenação via Pivot
    def quick_sort(self, low=None, high=None):

        # Definir os valores padrão para low e high
        if low is None:
            low = 0
        
        if high is None:
            high = self._size - 1
        
        # Verificar se low é menor que high
        if low < high:
            pi = self.partition(low, high)

            # Ordenar os elementos antes e depois da partição
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)
    
    def partition(self, low, high):
        # Usar o último elemento como pivô
        pivot = self._array[high]
        i = low - 1

        # Iterar sobre os elementos do array
        for j in range(low, high):

            # Se o elemento atual for menor que o pivô
            if self._array[j] < pivot:
                
                # Incrementar o índice do menor elemento
                i += 1

                # Trocar o elemento atual com o elemento na posição correta
                self._array[i], self._array[j] = self._array[j], self._array[i]
        
        # Trocar o pivô com o elemento na posição correta
        self._array[i + 1], self._array[high] = self._array[high], self._array[i + 1]
        return i + 1
