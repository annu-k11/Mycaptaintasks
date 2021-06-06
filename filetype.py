database = {
                ".c" : "C and C++ source code file",
                ".cgi" : "Perl script file",
                ".pl" : "Perl script file",
                ".class" : "Java class file",
                ".cpp" : "C++ source code file",
                ".cs" : "Visual C# source code file",
                ".h" : "C, C++, and Objective-C header file",
                ".java" : "Java Source code file",
                ".php" : "PHP script file",
                ".py" : "Python script file",
                ".sh" : "Bash shell script",
                ".swift" : "Swift source code file",
                ".vb" : "Visual Basic file",
                ".txt":"Text"
            }


ext = input("Input the filename: ")
[print("The extention of the file is :'",database[i],"'") for i in database if i == ext[ext.index("."):]]
