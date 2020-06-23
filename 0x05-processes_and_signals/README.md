<H1 align="center"> 0x05. Processes and signals </H1>

<p align="center">
   <a href="https://www.holbertonschool.com/co"><img src="https://user-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_1440,w_720,f_auto,q_auto/79001/368330_619080.png" width="170" height="170"/></a>

<p align="center"> 
   <b>Holberton School Bogotá D.C</b>
                
----
<H3> General </H3>
   
    What is a PID
    What is a process
    How to find a process’ PID
    How to kill a process
    What is a signal
    What are the 2 signals that cannot be ignored

### Tasks:

| Name | Description                    |
| ------------- | ------------------------------ |
| `0-what-is-my-pid`      |   Bash script that displays its own PID.  |
| `1-list_your_processes`      |    ash script that displays a list of currently running processes. |
| `2-show_your_bash_pid`   |  Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process. |
| `3-show_your_bash_pid_made_easy`      |Bash script that displays the PID, along with the process name, of processes whose name contain the word bash withou ps command|
| `4-to_infinity_and_beyond`      | Bash script that displays To infinity and beyond indefinitely.|
| ` 5-kill_me_now`      |  BBash script that kills 4-to_infinity_and_beyond process. |
| `6-kill_me_now_made_easy`      |  Bash script that kills 4-to_infinity_and_beyond process without kill command  |
| `7-highlander`      |   Bash script that displays To infinity and beyond indefinitely, With a sleep 2 in between each iteration, I am invincible!!! when receiving a SIGTERM signal |
| `8-beheaded_process`      |   Bash script that kills the process 7-highlander |
| `100-process_and_pid_file`      | Bash script that, Creates the file /var/run/holbertonscript.pid containing its PID, Displays To infinity and beyond indefinitely, Displays I hate the kill command when receiving a SIGTERM signal, Displays Y U no love me?! when receiving a SIGINT signal, Deletes the file /var/run/holbertonscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal |
| `100-read_and_cut`      |  Bash script that displays the content of the file /etc/passwd |
| `101-tell_the_story_of_passwd`      |   Bash script that displays the content of the file /etc/passwd, using the while loop + IFS |
| `102-lets_parse_apache_logs`      |   Bash script that displays the visitor IP along with the HTTP status code from the Apache log file|
| `103-dig_the-data`      |   Bash script that groups visitors by IP and HTTP status code, and displays this data.|

## Author: 
### Julian Ramirez <julianramirezch1@gmail.com>
----
[![Twitter Follow](https://img.shields.io/twitter/follow/JulianR_30.svg?style=social&label=Follow)](https://twitter.com/JulianR_30)

2020