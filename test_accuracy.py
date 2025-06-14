import json
from app import rag_chain  # Make sure your rag_chain is accessible here
from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def evaluate_chatbot(test_file="test_data.json", threshold=0.6):
    with open(test_file, "r") as f:
        test_data = json.load(f)

    total = len(test_data)
    passed = 0

    for idx, item in enumerate(test_data, 1):
        question = item["question"]
        expected = item["answer"]

        response = rag_chain.invoke({"input": question})
        actual = response["answer"]

        score = similarity(actual, expected)

        print(f"\nTest {idx}:")
        print("Q:", question)
        print("Expected:", expected)
        print("Actual:", actual)
        print("Similarity Score:", round(score, 2))

        if score >= threshold:
            passed += 1

    accuracy = (passed / total) * 100
    print(f"\nFinal Accuracy: {accuracy:.2f}%")
    return accuracy

if __name__ == "__main__":
    evaluate_chatbot()
