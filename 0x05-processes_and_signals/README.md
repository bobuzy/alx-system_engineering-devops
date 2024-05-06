# 0x05. Processes and signals



## Task 0: What is my PID

### Objective:
Write a Bash script that displays its own PID (Process ID).

### Solution Code (`0-what-is-my-pid`)
The provided Bash script simply echoes its own PID using the `$$` variable, which represents the PID of the current process.



## Task 1: List your processes

### Objective:
Write a Bash script that displays a list of currently running processes. The script should meet the following requirements:
- Show all processes for all users, including those without a TTY.
- Display the process hierarchy in a user-oriented format.

### Solution Code (`1-list_your_processes`)
The provided Bash script utilizes the `ps` command with the `-auxf` options to display a detailed list of currently running processes, including their hierarchy and user information.

Note: Running this script directly in a terminal will display the desired list of processes.



