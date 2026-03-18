class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __str__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority}, Arrival={self.arrival_time}, Deadline={self.deadline})"
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        self.heap.append(task)
        self.heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def increase_key(self, task_id, new_priority):
        for i in range(len(self.heap)):
            if self.heap[i].task_id == task_id:
                if new_priority > self.heap[i].priority:
                    self.heap[i].priority = new_priority
                    self.heapify_up(i)
                return

    def decrease_key(self, task_id, new_priority):
        for i in range(len(self.heap)):
            if self.heap[i].task_id == task_id:
                if new_priority < self.heap[i].priority:
                    self.heap[i].priority = new_priority
                    self.heapify_down(i)
                return

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index].priority > self.heap[parent].priority:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        size = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left].priority > self.heap[largest].priority:
                largest = left

            if right < size and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def display(self):
        if self.is_empty():
            print("Priority Queue is empty.")
        else:
            for task in self.heap:
                print(task)
if __name__ == "__main__":
    pq = PriorityQueue()

    t1 = Task("T1", 4, 0, 10)
    t2 = Task("T2", 7, 1, 8)
    t3 = Task("T3", 2, 2, 12)
    t4 = Task("T4", 9, 3, 6)

    print("Inserting tasks...")
    pq.insert(t1)
    pq.insert(t2)
    pq.insert(t3)
    pq.insert(t4)

    pq.display()

    print("\nIncrease priority of T3 to 8")
    pq.increase_key("T3", 8)
    pq.display()

    print("\nDecrease priority of T2 to 3")
    pq.decrease_key("T2", 3)
    pq.display()

    print("\nExecuting tasks by priority:")
    while not pq.is_empty():
        print(pq.extract_max())