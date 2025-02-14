import time

class TransformerNode:
    def __init__(self, name):
        self.name = name

    def process(self, data):
        # Simulate an expensive computation (e.g., heavy transformation)
        time.sleep(0.1)
        result = f"{data} -> processed by {self.name}"
        return result

class CachingNode(TransformerNode):
    def __init__(self, name):
        super().__init__(name)
        self.cache = {}

    def process(self, data):
        # Check if the result is already in the cache
        if data in self.cache:
            print(f"[{self.name}] Returning cached result.")
            return self.cache[data]
        # Simulate an expensive computation
        time.sleep(0.2)
        result = f"{data} -> processed by {self.name}"
        self.cache[data] = result
        print(f"[{self.name}] Caching result for future use.")
        return result

class Pipeline:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def run(self, data):
        for node in self.nodes:
            data = node.process(data)
        return data

def main():
    # Instantiate the pipeline
    pipeline = Pipeline()

    # Create pipeline nodes
    preprocessor = TransformerNode("Preprocessor")
    transformer = TransformerNode("Transformer")
    caching_node = CachingNode("CachingNode")  # BUG: This node is instantiated but not added to the pipeline

    # Add nodes to the pipeline
    pipeline.add_node(preprocessor)
    pipeline.add_node(transformer)
    # TODO: The caching_node should be added here to optimize performance.
    # For example: pipeline.add_node(caching_node)

    # Run the pipeline multiple times with the same input to observe performance differences.
    input_data = "raw data"
    print("First run:")
    result1 = pipeline.run(input_data)
    print("Result:", result1)

    print("\nSecond run (should benefit from caching if CachingNode were included):")
    result2 = pipeline.run(input_data)
    print("Result:", result2)

if __name__ == "__main__":
    main()
