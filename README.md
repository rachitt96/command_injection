# command_injection
This is a web-based application for demostrating the command injection attack. To exploit this vulnerability, an attacker will try to inject any unwanted (not intented by the developers) system command by modyfying the user input. By injecting a particular command, an attacker can able do anything he wants, like obtaining any sensitive information from the machine or removing any file, etc. So, while developing an secure web-based application, the developers should take care of this vulnerability.

In this project, first-of-all, I developed a web-based application (using Python) that is vulnerable to command-injection attack. Then, I modified a function to mitigate this vulnerability and to make an application non-vulnerable while also achieving the primary functionality.  

### Primary Functionality ###
The main functionality of this application is to show the content of any of three files (a.txt, b.txt and c.txt) present in the same folder as main application based on the user's choice. So, if user wants to see the content of "a.txt", he will need to put the file name in the user input box.

### Vulnerable Application ###
For executing the main functionality, I used Python subprocess module (https://docs.python.org/2/library/subprocess.html) to execute the "cat" command from Python program. subprocess.call() or subprocess.check_output() function accepts two arguments, first is "command" and second is "shell". As mentioned in Python official documention, setting up "shell" parameter to "True" can make the application vulnerable.

In vulnerable application, I used "subprocess.check_output(command, shell=True)" which makes the application vulnerable. To execute any additional command, an attacker can inject another command with existing one using (";"). The attacker may pass an input like:
##### a.txt; ls #####
By passing this input through user-input box, the syatem will also execute "ls" command. Instead of "ls", it can be any dangerous command.

### Non Vulnerable Application ###

In order to mitigate the vulnerability explained above, Python documentation suggests that, we should set the value of "shell" parameter to "False" in subprocess.check_output() function. So, in non-vulnetable function, I used the code "subprocess.check_output(command, shell=False)". So, after injecting the user input like (a.txt; ls), the application gives error instead of showing the result of command.

An application was still able to run as intended, means primary functionalities of the project is not compromised. So, after giving the input like (a.txt), the application shows the content of the file. 
