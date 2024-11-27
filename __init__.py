# __init__.py
memory = None
history = []

def show_history():
    if history:
        print("\nCalculation history:")
        for entry in history:
            print(entry)
    else:
        print("No calculations yet.")
