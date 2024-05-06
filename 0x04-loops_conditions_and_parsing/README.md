# 0x04. Loops, conditions and parsing



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



## Task 6: Superstitious numbers

### Objective:
Write a Bash script that displays numbers from 1 to 20 and:
- Displays "4" and then "bad luck from China" for the 4th loop iteration.
- Displays "9" and then "bad luck from Japan" for the 9th loop iteration.
- Displays "17" and then "bad luck from Italy" for the 17th loop iteration.

The objective is to practice using while loops and the case statement in Bash scripting for different actions based on specific numbers.

### Solution Code (`6-superstitious_numbers`)
The provided Bash script utilizes a while loop to iterate from 1 to 20, displaying numbers and specific messages based on the loop iteration. Here's how the code works:

1. The script initializes a variable `x` with a value of 1: `x=1`.
2. The `while` loop is used with the condition `[ $x -le 20 ]`, which means the loop will continue as long as the value of `x` is less than or equal to 20.
3. Inside the loop, the `echo "$x"` command is used to output the current value of `x`.
4. The `case` statement checks the value of `x` and executes specific actions based on different cases:
   - Case "4": Outputs "bad luck from China".
   - Case "9": Outputs "bad luck from Japan".
   - Case "17": Outputs "bad luck from Italy".
5. The loop increments the value of `x` using `(( x++ ))` with each iteration, eventually ending the loop after 20 iterations.
6. After 20 iterations, the loop ends, having displayed numbers from 1 to 20 with specific messages for the 4th, 9th, and 17th iterations.



## Task 7: Clock

### Objective:
Write a Bash script that displays the time for 12 hours and 59 minutes by:
- Displaying hours from 0 to 12.
- Displaying minutes from 1 to 59.

The objective is to practice using while loops in Bash scripting to generate time values within a specified range.

### Solution Code (`7-clock`)
The provided Bash script utilizes nested while loops to display the time for 12 hours and 59 minutes. Here's how the code works:

1. The script initializes a variable `hour` with a value of 0: `hour=0`.
2. The outer `while` loop is used with the condition `[ $hour -le 12 ]`, which means the loop will continue as long as the value of `hour` is less than or equal to 12.
3. Inside the outer loop, the `echo "Hour: $hour"` command is used to output the current hour.
4. The inner `while` loop is nested inside the outer loop and is used with the condition `[ $min -le 59 ]`, which means the loop will continue as long as the value of `min` (minutes) is less than or equal to 59.
5. Inside the inner loop, the `echo "$min"` command is used to output the current minute.
6. The inner loop increments the value of `min` using `(( min++ ))` with each iteration, eventually ending the inner loop after 59 minutes.
7. After the inner loop completes for each hour, the outer loop increments the value of `hour` using `(( hour++ ))`, eventually ending the outer loop after 12 hours.
8. After completing both loops, the script displays the time for 12 hours and 59 minutes.

Note: In this example, only the first 70 lines of output are displayed using the `head` command.



## Task 8: For ls

### Objective:
Write a Bash script that displays:
- All regular files of the current directory.
- In a list format.
- Where only the part of the name after the first dash is displayed (refer to the example).

The objective is to practice using for loops in Bash scripting to list directory files(excluding sub_directories and hidden files) and manipulate file names.

### Solution Code (`8-for_ls`)
The provided Bash script utilizes a for loop to list all all regular files in the current directory, displaying only the part of the name after the first dash. Here's how the code works:

1. The script uses a for loop to iterate through each file (`$file`) in the current directory.
2. Inside the loop, an `if` statement checks if `$file` is a regular file (`-f "$file"`) and if it's not a hidden file (`[[ "$file" != .* ]]`). Hidden files start with a dot (`.`) in Unix-like systems.
3. If the file meets the conditions, the script extracts the part of the name after the first dash (`-`) using the `cut` command and stores it in the variable `name`.
4. The script then echoes (`echo "$name"`) the modified name, displaying it in a list format.
5. The loop continues until all files in the directory have been processed, listing only the desired parts of the file names after the first dash.



## Task 9: To file, or not to file

### Objective:
Write a Bash script that gives you information about the school file. The script should check if the file exists and print specific information based on its existence, emptiness, and regularity.

The objective is to practice using if and else statements in Bash scripting to perform file checks and provide corresponding messages.

### Solution Code (`9-to_file_or_not_to_file`)
The provided Bash script checks for the existence of the school file and prints information about it. Here's how the code works:

1. The script uses an `if` statement to check if the file "school" exists (`-e "school"`).
2. If the file exists, it prints "school file exists" and proceeds to check further conditions.
3. Inside the nested `if` statement, it checks if the file is empty using `-s "school"`. If the file is empty, it prints "school file is empty"; otherwise, it prints "school file is not empty".
4. It then checks if the file is a regular file using `-f "school"`. If it is a regular file, it prints "school is a regular file".
5. If the file does not exist, the script prints "school file does not exist".
6. The script provides information about the school file based on its existence, emptiness, and regularity as per the requirements.



## Task 10: FizzBuzz

### Objective:
Write a Bash script that displays numbers from 1 to 100 and meets the following conditions:
- Displays "FizzBuzz" when the number is a multiple of 3 and 5.
- Displays "Fizz" when the number is a multiple of 3.
- Displays "Buzz" when the number is a multiple of 5.
- Otherwise, displays the number itself.

The objective is to practice using for loops and conditional statements in Bash scripting to implement the FizzBuzz problem.

### Solution Code (`10-fizzbuzz`)
The provided Bash script utilizes a for loop to iterate from 1 to 100 and applies the FizzBuzz logic to each number. Here's how the code works:

1. The script uses a for loop with the condition `((num=1; num<=100; num++))` to iterate from 1 to 100.
2. Inside the loop, an `if` statement checks multiple conditions:
   - If the number is divisible by both 3 and 5 (`((num % 3 == 0)) && ((num % 5 == 0))`), it prints "FizzBuzz".
   - If the number is divisible by 3 (`((num % 3 == 0))`), it prints "Fizz".
   - If the number is divisible by 5 (`((num % 5 == 0))`), it prints "Buzz".
   - Otherwise, it prints the number itself (`echo "$num"`).
3. The loop continues until all numbers from 1 to 100 have been processed, printing "Fizz", "Buzz", "FizzBuzz", or the number as required by the FizzBuzz problem.

Note: The output is displayed in a list format as per the requirements.



## How to Run the Code

1. **Create a New Bash Script:**
   - Open a text editor and create a new file.
   - Copy the solution code provided for each task into the new file.
   - Save the file with a `.sh` extension (e.g., `script_name.sh`)(optional).

2. **Make the Bash Script Executable:**
   - Navigate to the directory where you saved the Bash script using the `cd` command (e.g., `cd /path/to/your/script`).
   - Use the `chmod +x script_name` command to make the script executable (replace `script_name` with the actual name of your script).

3. **Run the Bash Script:**
   - After making the script executable, you can run it using the `./script_name` command (replace `script_name` with the actual name of your script).
   - The script will execute, and you will see the output in the terminal according to the specified task objectives.

Note: Ensure you have the appropriate permissions to execute the Bash script. You may need to use `sudo` or adjust file permissions accordingly.
