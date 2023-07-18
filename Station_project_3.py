# HELLO MY FRIEND, NICE TO SEE YOU!!!

from time import sleep
time = input("Insert time to count down (h:m:s)->  ")

def time_count_down(time=time):
    try:
        hours = time[:time.find(":")]
        time_without_hours = time[time.find(":")+1:]
        minutes = time_without_hours[:time_without_hours.find(":")]
        seconds = time_without_hours[time_without_hours.find(":")+1:]
        all_time_in_secs = int(seconds) + int(minutes)*60 + int(hours)*3600

        if int(minutes)>60 or int(seconds)>60:                   # Warning if input minutes of seconds 
            print("Input is wrong, but I understand you!!!")     # are more then 60!!!
            sleep(1)

        while all_time_in_secs>0:
            hours_for_print = all_time_in_secs//3600
            minutes_for_print = (all_time_in_secs-hours_for_print*3600)//60
            seconds_for_print = all_time_in_secs-hours_for_print*3600-minutes_for_print*60
            print(f"{hours_for_print:02d}:{minutes_for_print:02d}:{seconds_for_print:02d}")
            all_time_in_secs-=1
            sleep(1)
        print("00:00:00 WAKE UP!!!")
    except ValueError:      # Warning and stop code running if input is in wrong format
        print("\nSomething goes wrong!!! Maybe the input is wrong\n\nRight input format is H:M:S Example 2:10:30 or 00:01:05\n\nPlease re-run the code with right input")
    except:                 # Exit without errors if you decide to stop running before program ends
        print("Goodbye")

if __name__ == "__main__":
    time_count_down()