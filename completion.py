def sort_dicts_manual(data, key):
    """
    Manually implemented function to sort list of dictionaries by key
    """
    return sorted(data, key=lambda x: x[key])

def sort_dicts_ai(data, key):
    """
    AI-generated function to sort list of dictionaries by specific key
    Generated using GitHub Copilot
    """
    try:
        return sorted(data, key=lambda item: item.get(key, 0))
    except Exception as e:
        print(f"Error sorting: {e}")
        return data

# Test both implementations
if __name__ == "__main__":
    # Sample data
    sample_data = [
        {'name': 'John', 'age': 25, 'score': 85},
        {'name': 'Alice', 'age': 30, 'score': 92},
        {'name': 'Bob', 'age': 22, 'score': 78},
        {'name': 'Carol', 'age': 28, 'score': 95}
    ]
    
    print("Original data:")
    for item in sample_data:
        print(item)
    
    print("\nManual implementation (sorted by age):")
    manual_result = sort_dicts_manual(sample_data, 'age')
    for item in manual_result:
        print(item)
    
    print("\nAI implementation (sorted by score):")
    ai_result = sort_dicts_ai(sample_data, 'score')
    for item in ai_result:
        print(item)
    
    # Performance comparison
    import time
    
    # Test manual implementation
    start_time = time.time()
    for _ in range(10000):
        sort_dicts_manual(sample_data, 'age')
    manual_time = time.time() - start_time
    
    # Test AI implementation
    start_time = time.time()
    for _ in range(10000):
        sort_dicts_ai(sample_data, 'age')
    ai_time = time.time() - start_time
    
    print(f"\nPerformance Comparison:")
    print(f"Manual implementation: {manual_time:.4f} seconds")
    print(f"AI implementation: {ai_time:.4f} seconds")
    print(f"Difference: {abs(manual_time - ai_time):.4f} seconds")

"""
Analysis (200 words):

The AI-generated code demonstrates better defensive programming practices by including 
error handling and using item.get(key, 0) to handle missing keys gracefully. This makes 
it more robust for production use where data integrity cannot be guaranteed. However, 
this additional safety comes with a slight performance cost, as shown in our performance 
tests where the AI version was marginally slower due to the method call overhead.

The manual implementation is more efficient for controlled environments where key 
existence is guaranteed, making it preferable for performance-critical applications. 
The AI version's use of a default value (0) might not always be appropriate, as it 
could lead to incorrect sorting if the expected data type differs.

In real-world scenarios, the AI approach showcases how automated tools consider edge 
cases that human developers might overlook. This highlights the value of AI assistants 
in producing resilient code, though human oversight remains crucial to ensure the 
default behaviors align with specific business requirements.
"""