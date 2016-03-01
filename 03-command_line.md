# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. mkdir -p, --parents: no error if existing, make parent directories as needed    
   Example: mkdir -p temp/stuff/etc
2. ls -R, --recursive: list subdirectories recursively
3. pushd: The pushd command takes your current directory and "pushes" it into a list for later, then it changes to another directory.    
   Example: pushd temp/stuff/etc    
   pushd: switches between your current directory and the last one you pushed
4. popd: The popd command takes the last directory you pushed and "pops" it off, taking you back there.
5. touch: making empty files    
   Example: touch example.txt
6. cp -R, -r, --recursive: copy directories recursively
7. Pipes and Redirection:    
   $|$: The | takes the output from the command on the left, and "pipes" it to the command on the right.    
   $<$: The < will take and send the input from the file on the right to the program on the left.     
   $>$: The > takes the output of the command on the left, then writes it to the file on the right.    
   $>>$: The >> takes the output of the command on the left, then appends it to the file on the right.
8. Wildcard matching:    
   *: none or more characters    
   ?: exactly one character
9. find . -name "*.txt" -print | less
10. dir - list directory contents    
   -r, --reverse: reverse order while sorting    
   -R, --recursive: list subdirectories recursively
11. grep file *.txt
12. apropos copy; apropos remove; etc.
13. Environment:    
   export TESTING="1 2 3"   
   echo $TESTING; echo $USER; echo $PWD   
   env -- what's in your environment: env | grep TESTING   
   unset TESTING

Bash Cheat Sheet
http://cli.learncodethehardway.org/bash_cheat_sheet.pdf created by Raphael and CC licensed.
Reference Manual
http://www.gnu.org/software/bash/manual/bashref.html


###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  : list directory contents   
`ls -a` : do not ignore entries starting with .   
`ls -l` : use a long listing format    
`ls -lh` : print sizes in human readable format (e.g., 1K 234M 2G)    
`ls -lah` : print sizes in human readable format (e.g., 1K 234M 2G) AND do not ignore entries starting with .    
`ls -t`  : sort by modification time, newest first    
`ls -p` : --indicator-style=slash; append / indicator to directories    
`ls -G` : -G, --no-group; in a long listing, don't print group names    
`ls -Glp` : use a long listing format, don't print group names and append / indicator to directories    

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 7 of your favorites:

`ls -c` :	Displays files by file timestamp.   
`ls -d` : Displays only directories.   
`ls -f` :	Interprets each name as a directory, not a file.   
`ls -m` :	Displays the names as a comma-separated list.   
`ls -r` :	Displays files in reverse order.   
`ls -R`	: Displays subdirectories as well.   
`ls -1`	: Displays each entry on a line.   

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs - build and execute command lines from standard input    
Example: find /tmp -name core -type f -print0 | xargs -0 /bin/rm -f    
Find files named core in or below the directory /tmp and delete them, processing  filenames  in  such a way that file or directory names containing spaces or newlines are correctly handled.

 

