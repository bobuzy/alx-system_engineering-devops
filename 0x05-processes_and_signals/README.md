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



## Task 2: Show your Bash PID

### Objective:
Write a Bash script that displays lines containing the word "bash" to easily retrieve the PID of your Bash process.

### Solution Code (`2-show_your_bash_pid`)
The provided Bash script uses the `ps` command to list all processes (`ps auxf`) and then filters the output using `grep` to display lines containing the word "bash."



## Task 3: Show your Bash PID made easy

### Objective:
Write a Bash script that displays the PID along with the process name of processes whose name contains the word "bash."

### Solution Code (`3-show_your_bash_pid_made_easy`)
The provided Bash script utilizes the `pgrep` command with the `-l` option to list processes whose name contains the word "bash" along with their PIDs.



## Task 4: To infinity and beyond

### Objective:
Write a Bash script that displays "To infinity and beyond" indefinitely, adding a 2-second delay between each iteration of the loop.

### Solution Code (`4-to_infinity_and_beyond`)
The provided Bash script uses a `while` loop with the condition "true" to repeatedly echo "To infinity and beyond" and adds a 2-second delay using the `sleep 2` command between each iteration.



## Task 5: Don't stop me now!

### Objective:
Write a Bash script that stops the "4-to_infinity_and_beyond" process using the `kill` command.

### Solution Code (`5-dont_stop_me_now`)
The provided Bash script utilizes the `pgrep` command to find the PID of the "4-to_infinity_and_beyond" process and then uses the `kill` command to stop it.



## Task 6: Stop me if you can

### Objective:
Write a Bash script that stops the "4-to_infinity_and_beyond" process without using `kill` or `killall`.

### Solution Code (`6-stop_me_if_you_can`)
The provided Bash script uses the `pkill` command with the `-f` option to find and stop the "4-to_infinity_and_beyond" process based on its command line.



## Task 7: Highlander

### Objective:
Write a Bash script that displays "To infinity and beyond" indefinitely, with a 2-second delay between each iteration, and outputs "I am invincible!!!" when receiving a SIGTERM signal.

### Solution Code (`7-highlander`)
The provided Bash script uses a `while` loop with the condition "true" to repeatedly echo "To infinity and beyond" with a 2-second delay using `sleep 2`. It also sets up a trap to handle the SIGTERM signal and output "I am invincible!!!" when received.



## Task 8: Beheaded process

### Objective:
Write a Bash script that kills the process "7-highlander."

### Solution Code (`8-beheaded_process`)
The provided Bash script uses the `pkill` command with the `-f` option to find and kill the process named "7-highlander" with the SIGKILL signal.
