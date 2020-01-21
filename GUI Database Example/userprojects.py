import sqlite3
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QLineEdit,QLabel,QPushButton,QListWidget,QTableWidget,QTableWidgetItem,QTextEdit,QCheckBox
from PyQt5.QtCore import QTimer

# Main Window #################################################################

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250,50)
        self.setWindowTitle("Users and Projects")
        self.usersWin = None
        self.projecstWin = None
        self.assignProject = None

        con = sqlite3.connect("userprojectsDB.db")
        c = con.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (ID integer PRIMARY KEY, name text, department text);")
        c.execute("CREATE TABLE IF NOT EXISTS projects (ID integer PRIMARY KEY, name text, duedate text, details text);")
        c.execute("""CREATE TABLE IF NOT EXISTS connections
                  (userID integer NOT NULL, projectID integer NOT NULL,
                  FOREIGN KEY (userID) REFERENCES users (ID),
                  FOREIGN KEY (projectID) REFERENCES projects (ID));""")
        con.commit()
        c.close()
        con.close()

        #Widgets+Connections
        self.head = QLabel("Overview about users and projects")
        self.head.setStyleSheet("color: blue; font-size: 18px; font-weight: bold; qproperty-alignment: AlignCenter; margin-bottom: 15px;")

        self.usersButton = QPushButton("Users")
        self.usersButton.clicked.connect(self.usersWindow)

        self.projectsButton = QPushButton("Projects")
        self.projectsButton.clicked.connect(self.projectsWindow)

        #layout
        outerLayout = QVBoxLayout()

        innerLayout = QHBoxLayout()
        innerLayout.addWidget(self.usersButton)
        innerLayout.addWidget(self.projectsButton)

        outerLayout.addWidget(self.head)
        outerLayout.addLayout(innerLayout)

        self.setLayout(outerLayout)

        self.show()

    def usersWindow(self):
        self.usersWin = UsersWindow()
        self.usersWin.show()

    def projectsWindow(self):
        self.projecstWin = ProjectsWindow()
        self.projecstWin.show()

# Users Window #################################################################

class UsersWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250,400)
        self.setWindowTitle("Users")
        self.editWin = None
        self.newWin = None
        self.projectsWin = None

        #Widgets
        self.userDB=self.createTable("users")
        self.userDB.itemSelectionChanged.connect(self.activateButtons)

        self.newUserButton = QPushButton("New User")
        self.newUserButton.clicked.connect(self.newUserWindow)
        self.editUserButton = QPushButton("Edit User")
        self.editUserButton.setEnabled(False)
        self.editUserButton.clicked.connect(self.editUserWindow)
        self.deleteUserButton = QPushButton("Delete User")
        self.deleteUserButton.setEnabled(False)
        self.deleteUserButton.clicked.connect(self.deleteUser)
        self.showProjectsButton = QPushButton("Show User Projects")
        self.showProjectsButton.setEnabled(False)
        self.showProjectsButton.clicked.connect(self.projectsWindow)
        self.assignProjectsButton = QPushButton("Assign Project to user")
        self.assignProjectsButton.setEnabled(False)
        self.assignProjectsButton.clicked.connect(self.assignProject)
        #layout
        outerLayout = QVBoxLayout()

        userButtonLayout = QHBoxLayout()
        userButtonLayout.addWidget(self.newUserButton)
        userButtonLayout.addWidget(self.editUserButton)
        userButtonLayout.addWidget(self.deleteUserButton)

        projectButtonLayout = QHBoxLayout()
        projectButtonLayout.addWidget(self.showProjectsButton)
        projectButtonLayout.addWidget(self.assignProjectsButton)

        outerLayout.addWidget(self.userDB)
        outerLayout.addLayout(userButtonLayout)
        outerLayout.addLayout(projectButtonLayout)

        self.setLayout(outerLayout)

# open new window to do user entries
    def newUserWindow(self):
        self.newWin = NewUserWindow(self.userDB)
        self.newWin.show()
#open die window to edit the entry - it takes over the old entries
    def editUserWindow(self):
        self.editWin = EditUserWindow(self.getID(self.userDB),self.userDB.item(self.userDB.currentRow(),1).text(),self.userDB.item(self.userDB.currentRow(),2).text(),self.userDB)
        self.editWin.show()
# open window which shows all projects per user
    def projectsWindow(self):
        ID=self.getID(self.userDB)
        self.projectsWin = UserProjectsWindow(ID)
        self.projectsWin.show()
# open window to assign project to user
    def assignProject(self):
        ID=self.getID(self.userDB)
        self.assignProject = AssignProjectWindow(ID)
        self.assignProject.show()
# get the ID of the currently selected item
    def getID(self,table):
            return int(table.item(table.currentRow(),0).text())
#delete user
    def deleteUser(self):
        ID=int(self.getID(self.userDB))
        con = sqlite3.connect("userprojectsDB.db")
        c = con.cursor()
        c.execute("DELETE FROM users WHERE ID = ?",(ID,))
        c.execute("DELETE FROM connections WHERE userID = ?",(ID,))
        con.commit()
        c.close()
        con.close()
        self.userDB.removeRow(self.userDB.currentRow())
# enable buttons when something is chosen
    def activateButtons(self):
                self.editUserButton.setEnabled(True)
                self.deleteUserButton.setEnabled(True)
                self.showProjectsButton.setEnabled(True)
                self.assignProjectsButton.setEnabled(True)

# creating table for users or projects depending on var table
    def createTable(self,table):
        con = sqlite3.connect("userprojectsDB.db")
        c = con.cursor()

        c.execute("SELECT* FROM users")
        DB=QTableWidget(0,3)
        ID = QTableWidgetItem("ID")
        DB.setHorizontalHeaderItem(0,ID)
        Name = QTableWidgetItem("Name")
        DB.setHorizontalHeaderItem(1,Name)
        Department = QTableWidgetItem("Department")
        DB.setHorizontalHeaderItem(2,Department)

        j=0
        for x in c:
            addRow = DB.rowCount()
            DB.insertRow(addRow)
            for i in range(len(x)):
                val = QTableWidgetItem(str(x[i]))
                DB.setItem(j,i,val)
            j+=1
        c.close()
        con.close()
        DB.hideColumn(0)

        return DB

# to create new entry
class NewUserWindow(QWidget):
    def __init__(self,DB):
        super().__init__()
        self.resize(250,50)
        self.setWindowTitle("New Entry")
        self.userDB=DB
        #Widgets
        self.name = QLineEdit()
        self.name.setPlaceholderText("Name")

        self.department = QLineEdit()
        self.department.setPlaceholderText("Department")

        self.submitButton = QPushButton("Submit")
        self.submitButton.clicked.connect(self.createEntry)
        #layout
        Layout = QVBoxLayout()
        Layout.addWidget(self.name)
        Layout.addWidget(self.department)
        Layout.addWidget(self.submitButton)
        self.setLayout(Layout)


#  create new entry
    def createEntry(self):
        con = sqlite3.connect("userprojectsDB.db")
        c = con.cursor()
        c.execute("INSERT INTO users(name,department) VALUES (?,?);",(self.name.text(),self.department.text()))
        c.execute("SELECT max(ID) FROM users")
        for x in c:
            id=x[0]
        con.commit()
        c.close()
        con.close()
    # change object in showwindow
        addRow = self.userDB.rowCount()
        self.userDB.insertRow(addRow)
        id=QTableWidgetItem(str(id))
        name=QTableWidgetItem(self.name.text())
        department=QTableWidgetItem(self.department.text())
        self.userDB.setItem(addRow, 0,id)
        self.userDB.setItem(addRow, 1,name)
        self.userDB.setItem(addRow, 2,department)
        self.close()

# Edit Window #################################################################
# to edit entry
class EditUserWindow(QWidget):
    def __init__(self,ID,oldName,oldDepartment,DB):
        super().__init__()
        self.resize(250,50)
        self.setWindowTitle("Edit Entry")
        self.ID=ID
        self.oldName= oldName
        self.oldDepartment=oldDepartment
        self.userDB=DB

        #Widgets
        self.name = QLineEdit(self.oldName)
        self.department = QLineEdit(self.oldDepartment)

        self.submitButton = QPushButton("Submit")
        self.submitButton.clicked.connect(self.updateEntry)

        #layout
        Layout = QVBoxLayout()
        Layout.addWidget(self.name)
        Layout.addWidget(self.department)
        Layout.addWidget(self.submitButton)
        self.setLayout(Layout)

#edit entry in database
    def updateEntry(self):
        con = sqlite3.connect("userprojectsDB.db")
        c = con.cursor()
        c.execute("UPDATE users SET name=?,department=? WHERE ID = ?;",(self.name.text(),self.department.text(),self.ID))
        con.commit()
        c.close()
        con.close()
        self.close()
# change object in showwindow
        name=QTableWidgetItem(self.name.text())
        department=QTableWidgetItem(self.department.text())
        self.userDB.setItem(self.userDB.currentRow(), 1,name)
        self.userDB.setItem(self.userDB.currentRow(), 2,department)

class AssignProjectWindow(QWidget):
    def __init__(self,user):
        super().__init__()
        self.resize(250,50)
        self.setWindowTitle("Assign Projects")
        self.ID=user
        self.projects =[]
        self.oldProjects = []

        self.submitButton = QPushButton("Submit")
        self.submitButton.clicked.connect(self.setConnection)

# Getting username (Label)
        con = sqlite3.connect("userprojectsDB.db")
        c = con.cursor()
        c.execute("SELECT name FROM users WHERE ID = ?;",(self.ID,))
        self.name=c.fetchall()[0][0]
        c.close()
        con.close()
        self.nameLabel = QLabel(self.name)
# getting old checked projects
        con = sqlite3.connect("userprojectsDB.db")
        c = con.cursor()
        c.execute("SELECT projectID FROM connections WHERE userID = ?", (self.ID,))
        for x in c:
            self.oldProjects.append(x)
        c.close()
        con.close()
# getting Projects (Checkboxes)
        con = sqlite3.connect("userprojectsDB.db")
        c = con.cursor()
        c.execute("SELECT ID,name FROM projects")
        for x in c:
            a = QCheckBox(x[1])
            for y in self.oldProjects:
                if y[0] == x[0]:
                    a.setChecked(True)
            self.projects.append((int(x[0]),a))

        c.close()
        con.close()

# Layout
        baseLayout = QHBoxLayout()
        projectOptions = QVBoxLayout()
        for x in self.projects:
            projectOptions.addWidget(x[1])
        baseLayout.addWidget(self.nameLabel)
        baseLayout.addLayout(projectOptions)
        baseLayout.addWidget(self.submitButton)
        self.setLayout(baseLayout)

# set connection from user to his projects
    def setConnection(self):
        con = sqlite3.connect("userprojectsDB.db")
        c = con.cursor()
        c.execute("DELETE from connections WHERE userID =?",(self.ID,))
        for x in self.projects:
            if x[1].isChecked():
                c.execute("INSERT INTO connections(userID,projectID) VALUES (?,?);",(self.ID,x[0]))
        con.commit()
        c.close()
        con.close()

        self.close()

class UserProjectsWindow(QWidget):
    def __init__(self,user=None,project=None):
        super().__init__()
        self.resize(250,50)
        if user!=None:
            self.setWindowTitle("User Projects")
        if project!= None:
            self.setWindowTitle("Users for Project")
        self.userID = user
        self.projectID = project
        self.projects = []
        self.user = None
        self.users = []
        self.project = None
        self.projectShow = []
        self.checkLayout = []
        self.details = []
# create all projects per user or user per project
        if user!=None:
            con = sqlite3.connect("userprojectsDB.db")
            c = con.cursor()
            c.execute("""
                    SELECT users.name AS username, projects.name AS projectname, projects.details as details
                    FROM connections
                    INNER JOIN users
                    ON connections.userID = users.ID AND users.ID= ?
                    INNER JOIN projects
                    ON connections.projectID = projects.ID;""",(self.userID,))
            for x in c:
                self.projects.append(x[1])
                self.details.append(x[2])
                self.user=x[0]
#            con.commit()
            c.close()
            con.close()
        if project!=None:
            con = sqlite3.connect("userprojectsDB.db")
            c = con.cursor()
            c.execute("""
                    SELECT projects.name AS projectname, users.name AS username
                    FROM connections
                    INNER JOIN projects
                    ON connections.projectID = projects.ID AND projects.ID= ?
                    INNER JOIN users
                    ON connections.userID = users.ID;""",(self.projectID,))
            for x in c:
                self.users.append(x[0])
                self.project=x[1]
#            con.commit()
            c.close()
            con.close()

# Widgets
        self.userlabel = QLabel(self.user)
        #self.userlabel.setStyleSheet("font-size: 24px; font-weight: bold; qproperty-alignment: AlignCenter; margin-bottom: 15px;")
        self.nameLabel = QLabel("Name")
        self.projectsLabel = QLabel("Projects")
        for i in range(len(self.projects)):
            b= QLabel(self.projects[i])
            b.setToolTip(self.details[i])
            self.projectShow.append(b)

# layout
        self.baseLayout=QVBoxLayout()

        self.userprojlabel=QHBoxLayout()
        self.userprojlabel.addWidget(self.nameLabel)
        self.userprojlabel.addWidget(self.projectsLabel)

        self.projectLayout=QVBoxLayout()
        for x in self.projectShow:
            self.projectLayout.addWidget(x)
        self.showlabel=QHBoxLayout()
        self.showlabel.addWidget(self.userlabel)
        self.showlabel.addLayout(self.projectLayout)

        self.baseLayout.addLayout(self.userprojlabel)
        self.baseLayout.addLayout(self.showlabel)

        self.setLayout(self.baseLayout)

#####################################################################################
#####################################################################################
class ProjectsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250,400)
        self.setWindowTitle("Projects")
        self.editWin = None
        self.newWin = None
        self.userWin = None

        #Widgets
        self.projectDB=self.createTable()

        self.newProjectButton = QPushButton("New Project")
        self.newProjectButton.clicked.connect(self.newProjectWindow)
        self.editProjectButton = QPushButton("Edit Project")
        self.editProjectButton.clicked.connect(self.editProjectWindow)
        self.deleteProjectButton = QPushButton("Delete Project")
        self.deleteProjectButton.clicked.connect(self.deleteProject)

        #layout
        outerLayout = QVBoxLayout()

        projectButtonLayout = QHBoxLayout()
        projectButtonLayout.addWidget(self.newProjectButton)
        projectButtonLayout.addWidget(self.editProjectButton)
        projectButtonLayout.addWidget(self.deleteProjectButton)

        outerLayout.addWidget(self.projectDB)
        outerLayout.addLayout(projectButtonLayout)


        self.setLayout(outerLayout)

# open new window to do project entries
    def newProjectWindow(self):
        self.newWin = NewProjectWindow(self.projectDB)
        self.newWin.show()
#open die window to edit the entry - it takes over the old entries
    def editProjectWindow(self):
        self.editWin = EditProjectWindow(self.getID(self.projectDB),self.projectDB.item(self.projectDB.currentRow(),1).text(),self.projectDB.item(self.projectDB.currentRow(),2).text(),self.projectDB.item(self.projectDB.currentRow(),3).text(),self.projectDB)
        self.editWin.show()
# get the ID of the currently selected item
    def getID(self,table):
            return int(table.item(table.currentRow(),0).text())

# delete project
    def deleteProject(self):
        ID=self.getID(self.projectDB)
        con = sqlite3.connect("userprojectsDB.db")
        c = con.cursor()
        c.execute("DELETE FROM projects WHERE ID = ?",(ID,))
        c.execute("DELETE FROM connections WHERE projectID = ?",(ID,))
        con.commit()
        c.close()
        con.close()
        self.projectDB.removeRow(self.projectDB.currentRow())

# creating table for users or projects depending on var table
    def createTable(self):
        con = sqlite3.connect("userprojectsDB.db")
        c = con.cursor()

        c.execute("SELECT* FROM projects")
        DB=QTableWidget(0,4)
        ID = QTableWidgetItem("ID")
        DB.setHorizontalHeaderItem(0,ID)
        Name = QTableWidgetItem("Name")
        DB.setHorizontalHeaderItem(1,Name)
        duedate = QTableWidgetItem("Due Date")
        DB.setHorizontalHeaderItem(2,duedate)
        details = QTableWidgetItem("Details")
        DB.setHorizontalHeaderItem(3,details)
        j=0
        for x in c:
            addRow = DB.rowCount()
            DB.insertRow(addRow)
            for i in range(len(x)):
                val = QTableWidgetItem(str(x[i]))
                DB.setItem(j,i,val)
            j+=1
        c.close()
        con.close()
        DB.hideColumn(0)
        DB.hideColumn(3)
        return DB


# to create new entry
class NewProjectWindow(QWidget):
    def __init__(self,DB):
        super().__init__()
        self.resize(250,50)
        self.setWindowTitle("New Entry")
        self.projectDB = DB
        #Widgets
        self.name = QLineEdit()
        self.name.setPlaceholderText("Name")
        self.duedate = QLineEdit()
        self.duedate.setPlaceholderText("Due Date")
        self.details = QTextEdit()
        self.details.setPlaceholderText("Details")

        self.submitButton = QPushButton("Submit")
        self.submitButton.clicked.connect(self.createEntry)
        #layout
        Layout = QVBoxLayout()
        Layout.addWidget(self.name)
        Layout.addWidget(self.duedate)
        Layout.addWidget(self.details)
        Layout.addWidget(self.submitButton)
        self.setLayout(Layout)

#  create new entry
    def createEntry(self):
        con = sqlite3.connect("userprojectsDB.db")
        c = con.cursor()
        c.execute("INSERT INTO projects(name,duedate,details) VALUES (?,?,?);",(self.name.text(),self.duedate.text(),self.details.toPlainText()))
        c.execute("SELECT max(ID) FROM projects)")
        for x in c:
            id=x[0]
        con.commit()
        c.close()
        con.close()
    # change object in showwindow
        addRow = self.projectDB.rowCount()
        self.projectDB.insertRow(addRow)
        id=QTableWidgetItem(str(id))
        name=QTableWidgetItem(self.name.text())
        duedate=QTableWidgetItem(self.duedate.text())
        details=QTableWidgetItem(self.details.toPlainText())
        self.projectDB.setItem(addRow, 0,id)
        self.projectDB.setItem(addRow, 1,name)
        self.projectDB.setItem(addRow, 2,duedate)
        self.projectDB.setItem(addRow, 2,details)
        self.close()

# Edit Window #################################################################
# to edit entry
class EditProjectWindow(QWidget):
    def __init__(self,ID,oldName,oldDuedate,odlDetails,DB):
        super().__init__()
        self.resize(250,50)
        self.setWindowTitle("Edit Entry")
        self.ID=ID
        self.projectDB=DB
        self.oldName= oldName
        self.oldDuedate=oldDuedate
        self.odlDetails = odlDetails
        #Widgets
        self.name = QLineEdit(self.oldName)
        self.duedate = QLineEdit(self.oldDuedate)
        self.details = QTextEdit(self.odlDetails)

        self.submitButton = QPushButton("Submit")
        self.submitButton.clicked.connect(self.updateEntry)

        #layout
        Layout = QVBoxLayout()
        Layout.addWidget(self.name)
        Layout.addWidget(self.duedate)
        Layout.addWidget(self.details)
        Layout.addWidget(self.submitButton)
        self.setLayout(Layout)

# edit entry in database
    def updateEntry(self):
        con = sqlite3.connect("userprojectsDB.db")
        c = con.cursor()
        c.execute("UPDATE projects SET name=?,duedate=?,details=? WHERE ID = ?;",(self.name.text(),self.duedate.text(),self.details.toPlainText(),self.ID))
        con.commit()
        c.close()
        con.close()
        self.close()
# edit in object
        name=QTableWidgetItem(self.name.text())
        duedate=QTableWidgetItem(self.duedate.text())
        details= QTableWidgetItem(self.details.toPlainText())
        self.projectDB.setItem(self.projectDB.currentRow(), 1,name)
        self.projectDB.setItem(self.projectDB.currentRow(), 2,duedate)
        self.projectDB.setItem(self.projectDB.currentRow(), 3,details)


# Hauptprogramm
app = QApplication(sys.argv)
main = MainWindow()
sys.exit(app.exec_())
