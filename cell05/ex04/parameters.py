
import sys

def main():
  
    print(sys.argv)

    num_params = len(sys.argv) - 1
    print(f"Number of parameters: {num_params}.")

if __name__ == "__main__":
    main()
