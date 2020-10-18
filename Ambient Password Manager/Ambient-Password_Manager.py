import os

class Error:
    class InvalidInput:
        def throw(msg = "Invalid Input", solution = "try again!", err_code = "InErr"):
            print(msg + "\n")
            print("Error Code: " + err_code + "\n")
            print("Solution:\n" + solution + "\n")

    class Missing:
        class Database:
            def throw(msg = "The Database file is missing from the registered location.", solution =  "If you have moved the database, try reconfiguring the location using \"config location password_db\".\nIf you have deleted the file, there is no way you can recover your password except to restoring it from the recycle bin", err_code = "DB-404"):
                print(msg + "\n")
                print("Error Code: " + err_code + "\n")
                print("Solution:\n" + solution + "\n")
                
        class Logs:
            def throw(msg = "The log files are missing from the registered location.", solution =  "If you have moved the logs, try reconfiguring the location using \"conf location logs\".\nIf you have deleted the file, there is no way you can recover your logs except to restoring it from the recycle bin\nYou could also disable/enable logs by \"cofig [disable/enable] logs\"", err_code = "lOGS-404"):
                print(msg+ "\n")
                print("Error Code: " + err_code + "\n")
                print("Solution:\n" + solution + "\n")

    class SystemException:
        def throw(msg = "System Not Supported", solution = "Ambient password manager is currently not supported for your OS.", err_code = "SE" ):
            print(msg+ "\n")
            print("Error Code: " + err_code + "\n")
            print("Solution:\n" + solution + "\n")

class config:
    class location:
        def logs():
            pass

        def password_db():
            pass

    def encryption(algorithm):
        
