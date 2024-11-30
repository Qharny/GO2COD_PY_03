import datetime
import time
import winsound

def set_alarm(alarm_time):
    """
    Set an alarm for a specific time
    alarm_time: string in 'HH:MM' format (24-hour)
    """
    print("Alarm is set. Press Ctrl+C at any time to stop the alarm.")
    try:
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            
            if current_time == alarm_time:
                print("\nTime to wake up!")
                print("Press Ctrl+C to stop the alarm!")
                try:
                    # Beep continuously until interrupted
                    while True:
                        winsound.Beep(1000, 20000)
                except KeyboardInterrupt:
                    print("\nAlarm stopped!")
                    break
                
            # Check every 60 seconds
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nAlarm canceled!")

def main():
    # Get alarm time from user
    print("Set the alarm time (24-hour format, HH:MM): ")
    alarm_time = input()
    
    print(f"Alarm set for {alarm_time}")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
