from heapq import heappop, heappush

"""Water jug solver created by me, Ta Ho Thanh Dat 20225482"""


# Perform breath-first-search by implementing a queue
class PriorityQueue:
    def __init__(self):
        self.heap = []

    # Inserts a new key 'k'
    def push(self, k):
        heappush(self.heap, k)

    # remove minimum element
    def pop(self):
        return heappop(self.heap)

    # Check if queue is empty
    def empty(self):
        if not self.heap:
            return True
        else:
            return False


class Node:
    def __init__(self):
        self.parent = None
        self.step = 0
        self.action = ""
        self.cap = None
        self.state = None

    def __lt__(self, other):
        return self.step < other.step

    def __str__(self):
        state = "<" + " ".join(map(str, self.state)) + ">"
        step = f" Step {self.step} - "
        action = self.action
        return state + step + action


def Rootnode(*cap):
    """Create root node"""
    node = Node()
    node.cap = tuple(cap)
    node.state = [0] * len(cap)
    return node


def Nextnode(node):
    """Create next node"""
    nxt_node = Node()
    nxt_node.parent = node
    nxt_node.step = node.step + 1
    nxt_node.cap = node.cap
    nxt_node.state = node.state[:]
    return nxt_node


# Action that can be performed:
def fill(queue, node, jar):
    """Fill a jar if it is empty"""
    if node.state[jar] < node.cap[jar]:
        nxt_node = Nextnode(node)
        nxt_node.action = f"Fill {jar + 1}"
        nxt_node.state[jar] = nxt_node.cap[jar]
        queue.push(nxt_node)


def empty(queue, node, jar):
    """Empty a jar if it is not full"""
    if node.state[jar] != 0:
        nxt_node = Nextnode(node)
        nxt_node.action = f"Empty {jar + 1}"
        nxt_node.state[jar] = 0
        queue.push(nxt_node)


def pour(queue, node, jar1, jar2):
    """Pour from one jar to another"""
    r = node.cap[jar2] - node.state[jar2]
    if node.state[jar1] > 0 and r > 0:
        nxt_node = Nextnode(node)
        nxt_node.action = f"Pour {jar1 + 1} to {jar2 + 1}"
        if node.state[jar1] < r:
            nxt_node.state[jar2] += nxt_node.state[jar1]
            nxt_node.state[jar1] = 0
        else:
            nxt_node.state[jar2] = nxt_node.cap[jar2]
            nxt_node.state[jar1] -= r
        queue.push(nxt_node)


# Print solution
def PrintSolution(node):
    if node.parent is None:
        print(node)
        return
    PrintSolution(node.parent)
    print(node)


# The solver
class WaterJugsSolver:
    def __init__(self):
        self._queue = PriorityQueue()
        self._exist = set()
        self._jars = None

    def SetCapacity(self, *cap):
        """Set capacity"""
        self._queue.push(Rootnode(*cap))
        self._jars = range(len(cap))

    def SetEndState(self, *state):
        """Set end state"""
        self.final = tuple(state)

    def AllState(self):
        """Print all reachable states"""
        QUEUE = self._queue
        EXIST = self._exist
        JARS = self._jars
        while not QUEUE.empty():
            cur_node = self._queue.pop()
            cur_state = tuple(cur_node.state)
            if cur_state in EXIST:
                continue
            print("<" + " ".join(map(str, cur_node.state)) + ">")
            EXIST.add(cur_state)
            for jar1 in JARS:
                fill(QUEUE, cur_node, jar1)
                empty(QUEUE, cur_node, jar1)
                for jar2 in JARS:
                    if jar1 == jar2:
                        continue
                    pour(QUEUE, cur_node, jar1, jar2)

    def Solve(self, *final):
        """Print the steps to reach the end state, if possible"""
        QUEUE = self._queue
        EXIST = self._exist
        JARS = self._jars
        FINAL = self.final
        while not QUEUE.empty():
            cur_node = self._queue.pop()
            cur_state = tuple(cur_node.state)
            if cur_state == FINAL:
                PrintSolution(cur_node)
                break
            if cur_state in EXIST:
                continue
            EXIST.add(cur_state)
            for jar1 in JARS:
                fill(QUEUE, cur_node, jar1)
                empty(QUEUE, cur_node, jar1)
                for jar2 in JARS:
                    if jar1 == jar2:
                        continue
                    pour(QUEUE, cur_node, jar1, jar2)
        else:
            print("Unreachable")

    def GetExact(self, num):
        QUEUE = self._queue
        EXIST = self._exist
        JARS = self._jars
        while not QUEUE.empty():
            cur_node = self._queue.pop()
            cur_state = tuple(cur_node.state)
            if num in cur_state:
                return cur_node.step
            if cur_state in EXIST:
                continue
            EXIST.add(cur_state)
            for jar1 in JARS:
                fill(QUEUE, cur_node, jar1)
                empty(QUEUE, cur_node, jar1)
                for jar2 in JARS:
                    if jar1 == jar2:
                        continue
                    pour(QUEUE, cur_node, jar1, jar2)
        return -1
