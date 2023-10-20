import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Implementing the comparison operators for the heapq
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

def huffman_encoding(data):
    # Step 1: Create a frequency map
    frequency = Counter(data)
    
    # Step 2: Create the priority queue (heap) from the frequency map
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)
    
    # Step 3: Build the Huffman Tree
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        merged_node = Node(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right
        
        heapq.heappush(priority_queue, merged_node)
    
    # The Huffman Tree has been built, get the root
    root = priority_queue[0]
    
    # Step 4: Create codes from the Huffman Tree
    huffman_codes = {}
    
    def build_codes(node, current_code):
        if node is None:
            return
        
        if node.char is not None:
            huffman_codes[node.char] = current_code
        
        build_codes(node.left, current_code + "0")
        build_codes(node.right, current_code + "1")
    
    build_codes(root, "")
    
    # Step 5: Encode the text
    encoded_text = "".join([huffman_codes[char] for char in data])
    
    return encoded_text, huffman_codes

def huffman_decoding(encoded_text, huffman_codes):
    # Reverse the Huffman codes
    reversed_codes = {code: char for char, code in huffman_codes.items()}
    
    decoded_text = []
    current_code = ""
    
    for bit in encoded_text:
        current_code += bit
        if current_code in reversed_codes:
            decoded_text.append(reversed_codes[current_code])
            current_code = ""
    
    return "".join(decoded_text)

# Test
data = "this is an example for huffman encoding"
encoded, codes = huffman_encoding(data)
print(f"Encoded: {encoded}")
decoded = huffman_decoding(encoded, codes)
print(f"Decoded: {decoded}")