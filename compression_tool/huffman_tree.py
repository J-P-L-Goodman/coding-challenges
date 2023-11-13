import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison methods for heapq
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq


def build_huffman_tree(char_freq):
    # Create a priority queue (min heap) for nodes
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new internal node with combined frequency
        internal_node = Node(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right

        # Push the new internal node back into the heap
        heapq.heappush(heap, internal_node)

    # The remaining node is the root of the Huffman tree
    return heap[0]
