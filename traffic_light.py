from enum import Enum
from time import time
import threading
import logging

class LightState(Enum):
    RED = "Red"
    YELLOW = "Yellow"
    GREEN = "Green"

class TrafficLight:
    def __init__(self):
        # Default durations in seconds
        self.durations = {
            LightState.RED: 30,
            LightState.YELLOW: 5,
            LightState.GREEN: 25
        }
        
        self.current_state = LightState.RED
        self.last_change = time()
        self.running = False
        self.timer_thread = None
        
        # Setup logging
        logging.basicConfig(
            filename='traffic_light.log',
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )
        
    def start(self):
        """Start the automatic light cycle"""
        if not self.running:
            self.running = True
            self.timer_thread = threading.Thread(target=self._run_cycle)
            self.timer_thread.daemon = True
            self.timer_thread.start()
            logging.info("Traffic light cycle started")
    
    def stop(self):
        """Stop the automatic light cycle"""
        self.running = False
        if self.timer_thread:
            self.timer_thread.join()
        logging.info("Traffic light cycle stopped")
    
    def _run_cycle(self):
        """Internal method to run the automatic light cycle"""
        while self.running:
            current_time = time()
            if current_time - self.last_change >= self.durations[self.current_state]:
                self.change_light()
            threading.Event().wait(0.1)  # Small delay to prevent CPU overuse
    
    def change_light(self):
        """Automatically change to the next light in sequence"""
        if self.current_state == LightState.RED:
            self.current_state = LightState.GREEN
        elif self.current_state == LightState.GREEN:
            self.current_state = LightState.YELLOW
        else:
            self.current_state = LightState.RED
            
        self.last_change = time()
        logging.info(f"Light changed to {self.current_state.value}")
    
    def manual_change(self, state):
        """Manually change the light to a specific state"""
        if not isinstance(state, LightState):
            raise ValueError("Invalid light state")
        
        self.current_state = state
        self.last_change = time()
        logging.info(f"Light manually changed to {state.value}")
    
    def set_duration(self, state, duration):
        """Set the duration for a specific light state"""
        if not isinstance(state, LightState):
            raise ValueError("Invalid light state")
        if duration < 1:
            raise ValueError("Duration must be at least 1 second")
            
        self.durations[state] = duration
        logging.info(f"Duration for {state.value} set to {duration} seconds")
    
    def get_current_state(self):
        """Get the current state and its message"""
        messages = {
            LightState.RED: "Stop",
            LightState.YELLOW: "Prepare to stop",
            LightState.GREEN: "Go"
        }
        return self.current_state, messages[self.current_state] 