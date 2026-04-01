import sys
from ai.failure_analyzer import FailureAnalyzer

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m ai.cli '<error_message>'")
        return

    error_message = sys.argv[1]

    analyzer = FailureAnalyzer()
    result = analyzer.analyze(error_message)

    print("\n=== Failure Analysis ===")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()