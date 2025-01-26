from traffic_light import TrafficLight, LightState
import time

def print_menu():
    print("\nTraffic Light Control System")
    print("1. Start automatic cycle")
    print("2. Stop automatic cycle")
    print("3. Manual change")
    print("4. Set duration")
    print("5. Show current state")
    print("6. Exit")

def main():
    traffic_light = TrafficLight()
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            traffic_light.start()
            print("Automatic cycle started")
            
        elif choice == "2":
            traffic_light.stop()
            print("Automatic cycle stopped")
            
        elif choice == "3":
            print("\nSelect state:")
            print("1. Red")
            print("2. Yellow")
            print("3. Green")
            state_choice = input("Enter state (1-3): ")
            
            state_map = {
                "1": LightState.RED,
                "2": LightState.YELLOW,
                "3": LightState.GREEN
            }
            
            if state_choice in state_map:
                traffic_light.manual_change(state_map[state_choice])
                print(f"Light changed to {state_map[state_choice].value}")
            else:
                print("Invalid choice")
                
        elif choice == "4":
            print("\nSelect state to set duration:")
            print("1. Red")
            print("2. Yellow")
            print("3. Green")
            state_choice = input("Enter state (1-3): ")
            
            if state_choice in state_map:
                try:
                    duration = int(input("Enter duration in seconds: "))
                    traffic_light.set_duration(state_map[state_choice], duration)
                    print(f"Duration set for {state_map[state_choice].value}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Invalid choice")
                
        elif choice == "5":
            state, message = traffic_light.get_current_state()
            print(f"\nCurrent state: {state.value}")
            print(f"Message: {message}")
            
        elif choice == "6":
            traffic_light.stop()
            print("Exiting...")
            break
            
        else:
            print("Invalid choice")
        
        # Show current state after each action
        state, message = traffic_light.get_current_state()
        print(f"\nCurrent light: {state.value} - {message}")
        time.sleep(0.5)  # Small delay for better readability

if __name__ == "__main__":
    main() 