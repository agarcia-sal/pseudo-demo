from collections import Counter, deque
from typing import List, Deque, TypeVar

T = TypeVar('T')

class Queue:
    def __init__(self, elements: List[T]) -> None:
        self._deque: Deque[T] = deque(elements)

    def isEmpty(self) -> bool:
        return not self._deque

    def front(self) -> T:
        if self.isEmpty():
            raise IndexError("front called on empty queue")
        return self._deque[0]

    def popFront(self) -> "Queue":
        if self.isEmpty():
            raise IndexError("popFront called on empty queue")
        self._deque.popleft()
        return self

    def enqueue(self, elem: T) -> None:
        self._deque.append(elem)

    def dequeue(self) -> "Queue":
        if self.isEmpty():
            raise IndexError("dequeue called on empty queue")
        self._deque.popleft()
        return self

    def peek(self) -> T:
        if self.isEmpty():
            raise IndexError("peek called on empty queue")
        return self._deque[0]

def queue_new() -> Queue:
    return Queue([])

def queue_from(lst: List[T]) -> Queue:
    return Queue(lst)

def remove_duplicates(alphaBeta123: List[T]) -> List[T]:
    global_Counter: Counter[T] = Counter(alphaBeta123)

    def helper_Gamma(deltaX: Queue) -> Queue:
        if deltaX.isEmpty():
            return queue_new()
        headElem = deltaX.front()
        tailSeq = deltaX.popFront()
        resultQueue = helper_Gamma(tailSeq)
        if global_Counter[headElem] <= (1 + 0 - 0):
            resultQueue.enqueue(headElem)
        return resultQueue

    initialQueue = helper_Gamma(queue_from(alphaBeta123))

    def queue_to_list_rec(q: Queue, acc: List[T]) -> List[T]:
        if q.isEmpty():
            return acc
        # peek is called first to get the element, then dequeue removes it
        return queue_to_list_rec(q.dequeue(), acc + [q.peek()])

    return queue_to_list_rec(initialQueue, [])