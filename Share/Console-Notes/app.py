import os
from datetime import datetime


class Notes:
    def __init__(self) -> None:
        self.default_path = "C:/Users/Neha/Desktop/"
        self.current_working_directory = self.default_path
        self.working_file = None
        self.recently_created = None
        self.exit = False
    
    def clear_terminal(self):
        os.system('cls')
        print(f"HEADER : [Screen Cleared] At {datetime.now()}")
        print('-'*55,'\n')

    def close_app(self):
        print("DETAILS :- [App Closed - Please Rerun If Needed]")

    def pause_and_conitnue(self):
        print('\n' + '-' * 55)
        input("Press 'ENTER' : ")

    def welcome_user(self):
        self.clear_terminal()
        print("\n| CONSOLE NOTES |\n")

    def choose_actions(self):
        self.clear_terminal()
        print('\n' + "-"*65)
        print("DETAILS :- [Currrent Working Directory] : ", self.current_working_directory)

        print("\n  1 - Create New File *")
        print("  2 - Create New Folder")
        print("  3 - Open Recently Created File")
        print("  4 - Open Files From Current Directory")
        print("  5 - Change Path")
        print("  6 - View Tasks History")
        print("  7 - Quit App\n")

        choice = input("Choose(any option number): ")
        if not choice:
            choice = '1'
        return choice

  
    def start_working(self, choice:str):
        self.clear_terminal()
        if choice == '1':
            self.create_new_file()
        elif choice == '2':
            self.create_new_folder()
        elif choice == '3':
            self.open_recent_file()
            if self.recently_created:
                self.write_notes()
        elif choice == '4':
            self.open_existing_file()
            if self.working_file:
                self.write_notes()
        elif choice == '5':
            self.change_path()
        elif choice == '6':
            print("OPTION HELP : [This Feature Is Not Yet Available]")
        else:
            self.close_app()
            self.exit = True
        
        self.pause_and_conitnue()

  
    def create_new_file(self) -> None:
        file_name = input("New File Name: ").removeprefix('txt') + ".txt"

        if file_name in os.listdir(self.current_working_directory):
            print(f"\nTASK REJECTED :- [File '{file_name}' Already Exists]")
        else:
            print(f"\nTASK ACCEPTED :- [File '{file_name}' Created]")
            self.recently_created = file_name
            open(self.current_working_directory+file_name, 'w').close()


  def create_new_folder(self) -> None:
        folder_name = input("Enter new folder name: ").removeprefix('/')

        if folder_name in os.listdir(self.current_working_directory):
            print(f"\nTASK REJECTED :- [Folder '{folder_name}' Already Exists]")
        else:
            print(f"\nTASK ACCEPTED :- [Folder '{folder_name}' Created - Your Current Directory Path Changed]")
            self.current_working_directory += (folder_name + '/')
            os.mkdir(self.current_working_directory)


    def change_path(self) -> None:
        new_absolute_path = input("Enter absolute path: ").removesuffix('/')

        if os.path.isdir(new_absolute_path):
            print("\nTASK ACCEPTED :- [Current Working Directory Path Changed]")
            self.current_working_directory = (new_absolute_path + '/')            
        else:
            print("\nTASK REJECTED :- [Not Valid Path]")


    def open_existing_file(self) -> None:
        files = [file for file in os.listdir(self.current_working_directory) if file.endswith(".txt")]
        if files:
            print("DETAILS :- Current Working Directory Files:")
            print('-'*50, *files, '-'*50, sep='\n')
            file_name = input("Enter file name: ").removesuffix('.txt') + ".txt"
            self.clear_terminal()
            if file_name in files:
                print(f"TASK ACCEPTED :- [File '{file_name}' Opened]")
                self.working_file = open(self.current_working_directory+file_name, 'a+')
            else:
                print(f"TASK REJECTED :- [File '{file_name}' does not exist!]")
        
        else:
            print("DETAILS :- Directory Is Empty")


    def open_recent_file(self) -> None:
        if self.recently_created:
            print(f"TASK ACCEPTED :- [File {self.recently_created} Opened]")
            self.working_file = open(self.current_working_directory+self.recently_created, 'a+')
        else:
            print(f"TASK REJECTED :- [No Recent File Created]")
    
    
    def write_notes(self):
        new_content = ""
        line = ""
        self.working_file.seek(0)
        content = self.working_file.read()
        if content:
            print("\nNotebook Content", '-'*100, content, '-'*100, sep='\n')
            print("\n\nGUIDE :- [Continue Notes Below - (Enter '<quit>' On A New Line When Done)]")
        else:
            print("\n\nGUIDE :- [Start Writing Below - (Enter '<quit>' On A New Line When Done)]")

        print('-'*100)
        while True:
            line = input("----| ")
            if line in ("<QUIT>","<quit>"):
                break
            elif not line:
                line = '\n'
            else:
                line += '\n'
            new_content += line
        print('-'*100)

        self.working_file.write(new_content)
        self.working_file.close()
        self.working_file = None
        print("\nDETAILS :- [Noteboook Saved And Closed]")


    @classmethod
    def run(self):
        app = Notes()
        app.welcome_user()
        while not app.exit:
            app.start_working(app.choose_actions())


if __name__ == '__main__':
    Notes.run()
