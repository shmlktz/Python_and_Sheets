##Adding Contacts to Google Sheets list via a GUI in Tkinter

#Python Google Sheets connection
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import tkinter as tk

scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name("pythonsheets.json", scope)

# client = gspread.authorize(creds)

# sheet = client.open("automating_texting").sheet1 

# data = sheet.get_all_records()
#pprint(data)

#####
#Ask questions to build a new_contact list (name, number, etc)
new_contact = []
twelve_spaces = ['','','','','','','','','','','','']

def add_contact():
    add_name = input("What is the name of the entry? ")
    add_email = input("What is the email of the entry? ")
    add_phone = input("What is the primary phone number of the entry? ")
    add_hebrew_birthday = input("What is the hebrew birthday of the entry? ")
    add_gregorian_birthday = input("What is the gregorian birthday of the entry? ")
    add_alternate_email = input("What is the alternate email of the entry? ")
    add_alternate_phone = input("What is the alternate phone number of the entry? ")

    #creating a formula to add a new entry from all the questions just asked
    new_contact = [add_name, add_email, add_phone,
        add_hebrew_birthday, add_gregorian_birthday,
        add_alternate_email, add_alternate_phone]
    #new_contact.insert(3, twelve_spaces)
    new_contact = [*new_contact[:3], *twelve_spaces, *new_contact[3:]]

    print("\n"+str(new_contact),"\n")
    checking_input = input("Is this information correct? (If yes please type 'y') ") #Print the data to the user to check with the user if it is correct
    if checking_input == "y":
        sheet.insert_row(new_contact,1)
    else:
        print("OK, repeating data entry")
        add_contact()
# prompt_add_contact = input("Do you want to add a new contact? (If yes please type 'y') ")
# if prompt_add_contact == "y":
#     add_contact()

##pass it to the spreadsheet
##try passing 10 extra columns next to phone number to account for all phone emails
#####

##Allow this to be on a GUI? ##Ask if they want to use text or GUI?

window = tk.Tk()
#display = tk.Tk()
#display = tk.Label(text = "contacts")

frame = tk.Frame(master = window, relief = "sunken", borderwidth = 10)
frame.pack(side = tk.LEFT)
name_label = tk.Label(
    text="Enter name of entry",
    fg="yellow",  # Set the text color
    bg="black",  # Set the background color
    width = 16,
    height = 1,
    master = frame
)
name_entry = tk.Entry(
    fg="white",  # Set the text color
    bg="black",  # Set the background color
    width = 16,
    master = frame
)
name_label.pack()
name_entry.pack()
name_entry.insert(0, "_name_")
name = name_entry.get()

phone_label = tk.Label(
    text="Enter phone number",
    fg="yellow",  # Set the text color 
    bg="black",  # Set the background color
    width = 16,
    height = 1,
    master = frame
)
phone_entry = tk.Entry(
    fg="white",  # Set the text color
    bg="black",  # Set the background color
    width = 16,
    master = frame
)
phone_label.pack()
phone_entry.pack()

email_label = tk.Label(
    text="Enter email",
    fg="yellow",  # Set the text color 
    bg="black",  # Set the background color
    width = 16,
    height = 1,
    master = frame
)
email_entry = tk.Entry(
    fg="white",  # Set the text color
    bg="black",  # Set the background color
    width = 16,
    master = frame
)
email_label.pack()
email_entry.pack()

hebrew_birthday_label = tk.Label(
    text="Enter Hebrew Birthday",
    fg="yellow",  # Set the text color 
    bg="black",  # Set the background color
    width = 16,
    height = 1,
    master = frame
)
hebrew_birthday_entry = tk.Entry(
    fg="white",  # Set the text color
    bg="black",  # Set the background color
    width = 16,
    master = frame
)
hebrew_birthday_label.pack()
hebrew_birthday_entry.pack()

gregorian_birthday_label = tk.Label(
    text="Enter Gregorian Birthday",
    fg="yellow",  # Set the text color 
    bg="black",  # Set the background color
    width = 16,
    height = 1,
    master = frame
)
gregorian_birthday_entry = tk.Entry(
    fg="white",  # Set the text color
    bg="black",  # Set the background color
    width = 16,
    master = frame
)
gregorian_birthday_label.pack()
gregorian_birthday_entry.pack()

alternate_email_label = tk.Label(
    text="Enter alternate email",
    fg="yellow",  # Set the text color 
    bg="black",  # Set the background color
    width = 16,
    height = 1,
    master = frame
)
alternate_email_entry = tk.Entry(
    fg="white",  # Set the text color
    bg="black",  # Set the background color
    width = 16,
    master = frame
)
alternate_email_label.pack()
alternate_email_entry.pack()

alternate_phone_label = tk.Label(
    text="Enter alternate phone",
    fg="yellow",  # Set the text color 
    bg="black",  # Set the background color
    width = 16,
    height = 1,
    master = frame
)
alternate_phone_entry = tk.Entry(
    fg="white",  # Set the text color
    bg="black",  # Set the background color
    width = 16,
    master = frame
)
alternate_phone_label.pack()
alternate_phone_entry.pack()

text_box = tk.Text(
    bg = "yellow",
    fg = "black",
)
text_box.pack()
button = tk.Button(text = "Clicking")
button.pack(side = tk.LEFT)

#tk.colorchooser()
window.mainloop()

####LEARNING MATERIAL####
#########################

##insert rows
# sheet.insert_row(["this_2"],1)
# sheet.insert_row(["this_2"],1)

##deleting rows (only need to pass row or column #)
##sheet.delete_row(2)
#sheet.delete_rows(1,2)

# row = sheet.row_values(2)
# col = sheet.col_values(3)
# cell = sheet.cell(1,1).value

# insertRow = ["index_1", "index_2", "index_3", "index_4", "index_5", "index_6", "index_7", "index_8", "index_9"]
#sheet.insert_row(insertRow,1)