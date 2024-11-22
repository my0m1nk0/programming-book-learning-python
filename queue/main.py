
from pqueue import PQueue

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    p = PQueue()

    p.enqueue("HELLO", 1)
    p.enqueue("H", 2)
    p.enqueue("E", 5)
    p.enqueue("L", 3)
    p.enqueue("O", 3)
    p.enqueue("Sample", 9)

    # 7
    print(p.size())

    # Sample
    print(p.dequeue())

    # E
    print(p.dequeue())

    # 4
    print(p.size())

    # L
    print(p.dequeue())

    # O
    print(p.dequeue())

    # H
    print(p.dequeue())

    # 1
    print(p.size())
