import time
import threading
import os

class PomodoroClock:
    def __init__(self):
        self.work_duration = 25 * 60  # in seconds
        self.break_duration = 5 * 60  # in seconds
        self.sessions_completed = 0
        self.pause_event = threading.Event()

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def set_work_duration(self, minutes):
        self.work_duration = minutes * 60

    def set_break_duration(self, minutes):
        self.break_duration = minutes * 60

    def start_timer(self):
        def countdown(duration, session_type):
            while duration:
                self.clear_screen()

                if self.pause_event.is_set():
                    print("Timer is paused. Press Enter to continue...")
                    input()
                    self.pause_event.clear()
                    print("Timer resumed!")
                
                mins, secs = divmod(duration, 60)
                timeformat = '{:02d}:{:02d}'.format(mins, secs)
                print(session_type + " Timer:", timeformat)
                print("\n4. to Pause\n5. to Exit")
                time.sleep(1)
                duration -= 1

        print("Starting Work Session...")
        countdown(self.work_duration, "Work")
        
        print("\nTime for a break!")
        self.sessions_completed += 1

        print("Starting Break...")
        countdown(self.break_duration, "Break")

        print("\nBreak's over! Time to get back to work.")


    def display_menu(self):
        print("\n--- POMODORO CLOCK ---")
        print("1. Set Work Duration (Currently set to:", self.work_duration//60, "minutes)")
        print("2. Set Break Duration (Currently set to:", self.break_duration//60, "minutes)")
        print("3. Start the Timer")
        print("4. Pause/Resume Timer")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                minutes = int(input("Enter work duration in minutes (1-60): "))
                self.set_work_duration(minutes)
            elif choice == "2":
                minutes = int(input("Enter break duration in minutes (1-60): "))
                self.set_break_duration(minutes)
            elif choice == "3":
                thread = threading.Thread(target=self.start_timer)
                thread.daemon = True
                thread.start()
            elif choice == "4":
                self.pause_event.set()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    clock = PomodoroClock()
    clock.run()
