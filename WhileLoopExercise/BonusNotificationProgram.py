from plyer import notification
fromm time import sleep

task_to_do = input("Enter the task: ")
show_after_seconds = int(input("Set the timer to (seconds): "))
# TODO: Let the user choose hours, minutes or seconds, make validations

sleep(show_after_seconds) # accepts only seconds

notification.notify(
    title="My first notification",
    message="Some random text",
    app_icon="Insert file path. If in the same dir as the .py file enter only file name" #   .ico for Windows,    .png for Mac, Linux
)