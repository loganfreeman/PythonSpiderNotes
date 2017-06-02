'''
GUI TEST RUNNER
Run by Typing: "python gui_test_runner.py"
'''

from Tkinter import Tk, Frame, Button, Label
import os


class App:

    def __init__(self, master):
        frame = Frame()
        frame.pack()
        root.title("Select Test Job To Run")
        self.label = Label(root, width=40).pack()
        self.title = Label(frame, text="", fg="black").pack()
        self.title1 = Label(
            frame, text="Basic Test Run in Chrome:", fg="blue").pack()
        self.run1 = Button(
            frame, command=self.run_1,
            text=("nosetests my_first_test.py --with-selenium"
                  " --browser=chrome")).pack()
        self.title2 = Label(
            frame, text="Basic Test Run in Firefox:", fg="blue").pack()
        self.run2 = Button(
            frame, command=self.run_2,
            text=("nosetests my_first_test.py"
                  " --with-selenium --browser=firefox")).pack()
        self.title3 = Label(
            frame, text="Basic Test Run in Demo Mode:", fg="blue").pack()
        self.run3 = Button(
            frame, command=self.run_3,
            text=("nosetests my_first_test.py"
                  " --with-selenium --browser=chrome --demo_mode")).pack()
        self.title4 = Label(
            frame,
            text="Basic Failing Test Run with Screenshots:",
            fg="blue").pack()
        self.run4 = Button(
            frame, command=self.run_4,
            text=("nosetests test_fail.py --with-selenium --browser=chrome"
                  " --with-testing_base --demo_mode")).pack()
        self.title5 = Label(
            frame,
            text="Basic Failing Test Suite Run with Test Report:",
            fg="blue").pack()
        self.run5 = Button(
            frame, command=self.run_5,
            text=("nosetests my_test_suite.py --with-selenium"
                  " --browser=chrome --with-testing_base --report")).pack()
        self.title6 = Label(
            frame,
            text="Basic Failing Test Run showing the Multiple-Checks feature:",
            fg="blue").pack()
        self.run6 = Button(
            frame, command=self.run_6,
            text=("nosetests non_terminating_checks_test.py"
                  " --browser=chrome --with-selenium")).pack()
        self.title7 = Label(
            frame,
            text="MySQL DB Reporting Tests: (See ReadMe.md for Setup Steps!)",
            fg="blue").pack()
        self.run7 = Button(
            frame, command=self.run_7,
            text=("nosetests my_test_suite.py --with-selenium"
                  " --browser=chrome --with-db_reporting")).pack()
        self.end_title = Label(frame, text="", fg="black").pack()
        self.quit = Button(frame, text="QUIT", command=frame.quit).pack()

    def run_1(self):
        os.system(
            'nosetests my_first_test.py --with-selenium --browser=chrome')

    def run_2(self):
        os.system(
            'nosetests my_first_test.py --with-selenium --browser=firefox')

    def run_3(self):
        os.system(
            'nosetests my_first_test.py --with-selenium --demo_mode'
            ' --browser=chrome')

    def run_4(self):
        os.system(
            'nosetests test_fail.py --with-selenium'
            ' --browser=chrome --with-testing_base --demo_mode')

    def run_5(self):
        os.system(
            'nosetests my_test_suite.py --with-selenium'
            ' --browser=chrome --with-testing_base --report')

    def run_6(self):
        os.system(
            'nosetests non_terminating_checks_test.py --with-selenium'
            ' --browser=chrome')

    def run_7(self):
        os.system(
            'nosetests my_test_suite.py --with-selenium'
            ' --browser=chrome --with-db_reporting')


if __name__ == "__main__":
    root = Tk()
    root.minsize(612, 444)
    app = App(root)
    root.mainloop()
