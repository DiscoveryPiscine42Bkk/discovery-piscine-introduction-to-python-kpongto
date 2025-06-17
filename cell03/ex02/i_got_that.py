
def main():
    
    while True:
        user_input = input("Say something (type 'STOP' to quit): ")
        
        
        if user_input == "STOP":
            print("Goodbye!")
            break  
        
        
        print(f"I got that: {user_input}")

if __name__ == "__main__":
    main()
