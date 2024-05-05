# 0x04-loops_conditions_and_parsing

## Task 0: Create a SSH RSA key pair

### Objective:
This task involves creating an SSH RSA key pair for accessing remote servers securely. The objective is to set up RSA public and private keys for SSH access to remote servers.

### Solution Code (`0-RSA_public_key.pub`)


## Task 1: For Best School loop

### Objective:
This task requires writing a Bash script that uses a for loop to display "Best School" 10 times. The objective is to practice using loops in Bash scripting for repetitive tasks efficiently.

### Solution Code (`1-for_best_school`)
The provided Bash script utilizes a for loop to iterate 10 times, each time echoing the string "Best School". Here's how the code works:

1. The `for` loop is initialized with the syntax `for (( i = 0; i < 10; i++ ))`, where `i` is the loop variable starting from 0 and incrementing by 1 in each iteration until it reaches 9 (10 iterations in total).
2. Inside the loop, the `echo "Best School"` command is used to output the text "Best School" to the terminal.
3. After the loop completes all iterations, the script ends, having displayed "Best School" 10 times in the terminal.


## Task 2: While Best School loop

### Objective:
Write a Bash script that displays "Best School" 10 times using a while loop. The objective is to practice using while loops in Bash scripting for repetitive tasks efficiently.

### Solution Code (`2-while_best_school`)
The provided Bash script utilizes a while loop to display "Best School" 10 times. Here's how the code works:

1. The script initializes a variable `x` with a value of 1: `x=1`.
2. The `while` loop is used with the condition `[ $x -le 10 ]`, which means the loop will continue as long as the value of `x` is less than or equal to 10.
3. Inside the loop, the `echo "Best School"` command is used to output the text "Best School" to the terminal.
4. The loop also increments the value of `x` using `(( x++ ))`, ensuring that the loop will eventually terminate after 10 iterations.
5. After 10 iterations, the loop ends, having displayed "Best School" 10 times in the terminal.


## Task 3: Until Best School loop

### Objective:
Write a Bash script that displays "Best School" 10 times using an until loop. The objective is to practice using until loops in Bash scripting for repetitive tasks efficiently.

### Solution Code (`3-until_best_school`)
The provided Bash script utilizes an until loop to display "Best School" 10 times. Here's how the code works:

1. The script initializes a variable `x` with a value of 0: `x=0`.
2. The `until` loop is used with the condition `[ $x -eq 10 ]`, which means the loop will continue until the value of `x` equals 10.
3. Inside the loop, the `echo "Best School"` command is used to output the text "Best School" to the terminal.
4. The loop increments the value of `x` using `(( x++ ))` with each iteration, eventually reaching 10 and ending the loop.
5. After 10 iterations, the loop ends, having displayed "Best School" 10 times in the terminal.


## Task 4: If 9, say Hi!

### Objective:
Write a Bash script that displays "Best School" 10 times, but for the 9th iteration, displays "Best School" and then "Hi" on a new line. The objective is to practice using while loops and if statements in Bash scripting for conditional execution.

### Solution Code (`4-if_9_say_hi`)
The provided Bash script utilizes a while loop to display "Best School" 10 times, with a condition to display "Hi" on the 9th iteration. Here's how the code works:

1. The script initializes a variable `x` with a value of 1: `x=1`.
2. The `while` loop is used with the condition `[ $x -le 10 ]`, which means the loop will continue as long as the value of `x` is less than or equal to 10.
3. Inside the loop, the `echo "Best School"` command is used to output the text "Best School" to the terminal.
4. An `if` statement checks if `x` is equal to 9 using the condition `[ $x -eq 9 ]`. If true, it executes the `echo "Hi"` command to output "Hi" on a new line.
5. The loop increments the value of `x` using `(( x++ ))` with each iteration, eventually ending the loop after 10 iterations.
6. After 10 iterations, the loop ends, having displayed "Best School" 10 times with "Hi" on a new line during the 9th iteration.


## Task 5: 4 bad luck, 8 is your chance

### Objective:
Write a Bash script that loops from 1 to 10 and displays "bad luck" for the 4th loop iteration, "good luck" for the 8th loop iteration, and "Best School" for the other iterations. The objective is to practice using while loops and conditional statements (if, elif, else) in Bash scripting for different actions based on conditions.

### Solution Code (`5-4_bad_luck_8_is_your_chance`)
The provided Bash script utilizes a while loop to iterate from 1 to 10, displaying different messages based on the loop iteration. Here's how the code works:

1. The script initializes a variable `x` with a value of 1: `x=1`.
2. The `while` loop is used with the condition `[ $x -le 10 ]`, which means the loop will continue as long as the value of `x` is less than or equal to 10.
3. Inside the loop, an `if` statement checks if `x` is equal to 4 using the condition `[ $x -eq 4 ]`. If true, it executes the `echo "bad luck"` command to output "bad luck".
4. An `elif` statement checks if `x` is equal to 8 using the condition `[ $x -eq 8 ]`. If true, it executes the `echo "good luck"` command to output "good luck".
5. If neither of the above conditions is met, the `else` statement executes the `echo "Best School"` command to output "Best School".
6. The loop increments the value of `x` using `(( x++ ))` with each iteration, eventually ending the loop after 10 iterations.
7. After 10 iterations, the loop ends, having displayed "bad luck" for the 4th iteration, "good luck" for the 8th iteration, and "Best School" for the other iterations.


