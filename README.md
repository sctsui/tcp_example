Usage
python network.py NW
python main_thread.py P1
python main_thread.py P2
python main_thread.py P3

The 1st argument from sys is the ID used in process_config.json to identify the process

From the main thread, enter the ID of which process to send the message.
The message gets routed through the NW process, and forwarded to the destination process specified by the user.
