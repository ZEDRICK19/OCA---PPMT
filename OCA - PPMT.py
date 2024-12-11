import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from ttkthemes import ThemedTk
import sqlite3
from datetime import datetime
from tkinter import Frame

# Database connection and setup
def connect_db():
    conn = sqlite3.connect('performers.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS performers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            middle_name TEXT,
            address TEXT,
            date_of_birth TEXT,
            age INTEGER,
            gender TEXT,
            email TEXT,
            contact_number TEXT,
            guardian_name TEXT,
            guardian_contact TEXT,
            photo BLOB,
            campus TEXT,
            college TEXT,
            program TEXT,
            sr_code TEXT,
            year_level TEXT,
            units INTEGER,
            achievements TEXT,
            group_name TEXT
        )
    ''')
    conn.commit()
    return conn

# Global variables
tree_groups = None
selected_group_name = None

# Validate login credentials
def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        login_window.destroy()
        open_group_selection()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Open group selection window
def open_group_selection():
    global tree_groups
    group_window = ThemedTk(theme="arc")
    group_window.title("Select a Group")
    group_window.geometry("1024x768")
    group_window.configure(bg="#F5F5DC")  # Beige background

    tk.Label(group_window, text="Select a Group:", font=("Arial", 20, "bold"), bg="#F5F5DC", fg="#800000").pack(pady=10)
    
    tree_groups = ttk.Treeview(group_window, columns=("ID", "Group Name"), show='headings', height=10)
    tree_groups.heading("ID", text="ID")
    tree_groups.heading("Group Name", text="Group Name")
    tree_groups.column("ID", width=50, anchor="center")
    tree_groups.column("Group Name", width=400, anchor="center")
    tree_groups.pack(fill=tk.BOTH, expand=True, pady=20)
    
    view_groups()
    
    tk.Button(group_window, text="Select Group", command=open_member_management, bg="#800000", fg="#FFFFFF", font=("Arial", 14)).pack(pady=5)

# View groups in treeview
def view_groups():
    conn = connect_db()
    cursor = conn.cursor()
    tree_groups.delete(*tree_groups.get_children())
    cursor.execute('SELECT * FROM groups')
    for row in cursor.fetchall():
        tree_groups.insert('', 'end', values=row)
    conn.close()

# Open member management window
def open_member_management():
    global selected_group_name
    selected_item = tree_groups.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a group.")
        return
    selected_group_name = tree_groups.item(selected_item)['values'][1]
    member_window = tk.Toplevel()
    member_window.title(f"Manage Members - {selected_group_name}")
    member_window.geometry("1280x800")
    member_window.configure(bg="#F5F5DC")

    tk.Label(member_window, text=f"Members of {selected_group_name}", font=("Arial", 20, "bold"), bg="#F5F5DC", fg="#800000").pack(pady=10)

    member_tree = ttk.Treeview(member_window, columns=("ID", "Name", "Age", "Email", "Group"), show='headings', height=15)
    member_tree.heading("ID", text="ID")
    member_tree.heading("Name", text="Name")
    member_tree.heading("Age", text="Age")
    member_tree.heading("Email", text="Email")
    member_tree.heading("Group", text="Group")

    for col in ("ID", "Name", "Age", "Email", "Group"):
        member_tree.column(col, anchor="center")

    member_tree.pack(fill=tk.BOTH, expand=True, pady=20)
    
    tk.Button(member_window, text="Add Member", command=lambda: open_add_member_window(member_tree), bg="#800000", fg="#FFFFFF", font=("Arial", 14)).pack(pady=5)
    tk.Button(member_window, text="Close", command=member_window.destroy, bg="#800000", fg="#FFFFFF", font=("Arial", 14)).pack(pady=5)

# Open add member window
def add_scrollbars(parent, treeview):
    scroll_x = tk.Scrollbar(parent, orient="horizontal", command=treeview.xview)
    scroll_y = tk.Scrollbar(parent, orient="vertical", command=treeview.yview)
    treeview.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side="bottom", fill="x")
    scroll_y.pack(side="right", fill="y")

# Modify add_member_window to use scrollbars
def open_add_member_window(tree):
    add_member_window = tk.Toplevel()
    add_member_window.title("Add Member - Step 1: Personal Information")
    add_member_window.geometry("1024x768")
    add_member_window.configure(bg="#F5F5DC")

    # Create a scrollable frame
    container = Frame(add_member_window)
    container.pack(fill=tk.BOTH, expand=True)
    canvas = tk.Canvas(container, bg="#F5F5DC")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg="#F5F5DC")
    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Add your fields to scrollable_frame
    fields = [
        ("First Name", "entry_first_name"), ("Last Name", "entry_last_name"), ("Middle Name", "entry_middle_name"),
        ("Address", "entry_address"), ("Date of Birth (YYYY-MM-DD)", "entry_dob"), ("Age", "entry_age"),
        ("Gender", "entry_gender"), ("Email Address", "entry_email"), ("Contact Number", "entry_contact"),
        ("Guardian Name", "entry_guardian_name"), ("Guardian Contact", "entry_guardian_contact"), ("2x2 Picture", "entry_photo")
    ]
    entries = {}
    for label_text, var_name in fields:
        tk.Label(scrollable_frame, text=label_text, font=("Arial", 14), bg="#F5F5DC", fg="#800000").pack(pady=5)
        if "Picture" in label_text:
            entries[var_name] = tk.Button(scrollable_frame, text="Upload Picture", command=lambda: filedialog.askopenfilename())
        else:
            entries[var_name] = tk.Entry(scrollable_frame, font=("Arial", 14))
        entries[var_name].pack(pady=5)

    tk.Button(scrollable_frame, text="Next", command=lambda: open_educational_info_window(tree, entries), bg="#800000", fg="#FFFFFF", font=("Arial", 14)).pack(pady=20)

# Open educational information window
def open_educational_info_window(tree, personal_entries):
    edu_window = tk.Toplevel()
    edu_window.title("Add Member - Step 2: Educational Information")
    edu_window.geometry("1024x768")
    edu_window.configure(bg="#F5F5DC")

    fields = [
        ("Campus", "entry_campus"), ("College", "entry_college"), ("Program", "entry_program"),
        ("SR-Code", "entry_sr_code"), ("Year Level", "entry_year_level"), ("Units per Semester", "entry_units")
    ]

    entries = {}
    for label_text, var_name in fields:
        tk.Label(edu_window, text=label_text, font=("Arial", 14), bg="#F5F5DC", fg="#800000").pack(pady=5)
        entries[var_name] = tk.Entry(edu_window, font=("Arial", 14))
        entries[var_name].pack(pady=5)

    tk.Button(edu_window, text="Next", command=lambda: open_participation_window(tree, personal_entries, entries), bg="#800000", fg="#FFFFFF", font=("Arial", 14)).pack(pady=20)

# Open participation window
def open_participation_window(tree, personal_entries, edu_entries):
    part_window = tk.Toplevel()
    part_window.title("Add Member - Step 3: Participation")
    part_window.geometry("1024x768")
    part_window.configure(bg="#F5F5DC")

    tk.Label(part_window, text="Participation and Achievements", font=("Arial", 16, "bold"), bg="#F5F5DC", fg="#800000").pack(pady=10)

    part_tree = ttk.Treeview(part_window, columns=("Date", "Event", "Level", "Rank"), show='headings', height=10)
    for col in ("Date", "Event", "Level", "Rank"):
        part_tree.heading(col, text=col)
        part_tree.column(col, anchor="center")
    part_tree.pack(fill=tk.BOTH, expand=True, pady=20)

    tk.Button(part_window, text="Add Row", command=lambda: add_participation_row(part_tree), bg="#800000", fg="#FFFFFF", font=("Arial", 14)).pack(pady=5)
    tk.Button(part_window, text="Save Member", command=lambda: save_member(tree, personal_entries, edu_entries, part_tree), bg="#800000", fg="#FFFFFF", font=("Arial", 14)).pack(pady=10)

# Add row to participation table
def add_participation_row(tree):
    tree.insert('', 'end', values=("", "", "", ""))

# Save member to database
def save_member(tree, personal_entries, edu_entries, part_tree):
    conn = connect_db()
    cursor = conn.cursor()

    personal_info = {key: entry.get() if isinstance(entry, tk.Entry) else entry for key, entry in personal_entries.items()}
    edu_info = {key: entry.get() for key, entry in edu_entries.items()}
    achievements = []
    for row in part_tree.get_children():
        achievements.append(part_tree.item(row)['values'])

    cursor.execute('''
        INSERT INTO performers (first_name, last_name, middle_name, address, date_of_birth, age, gender, email, contact_number, guardian_name, guardian_contact, campus, college, program, sr_code, year_level, units, achievements, group_name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        personal_info['entry_first_name'], personal_info['entry_last_name'], personal_info['entry_middle_name'], personal_info['entry_address'],
        personal_info['entry_dob'], personal_info['entry_age'], personal_info['entry_gender'], personal_info['entry_email'], personal_info['entry_contact'],
        personal_info['entry_guardian_name'], personal_info['entry_guardian_contact'], edu_info['entry_campus'], edu_info['entry_college'],
        edu_info['entry_program'], edu_info['entry_sr_code'], edu_info['entry_year_level'], edu_info['entry_units'], str(achievements), selected_group_name
    ))
    conn.commit()
    conn.close()

    tree.insert('', 'end', values=(personal_info['entry_first_name'], personal_info['entry_last_name'], personal_info['entry_age'], personal_info['entry_email'], selected_group_name))
    messagebox.showinfo("Success", "Member added successfully!")

# Initialize login window
login_window = ThemedTk(theme="arc")
login_window.title("Admin Login")
login_window.geometry("1024x768")
login_window.configure(bg="#F5F5DC")

tk.Label(login_window, text="Username:", font=("Arial", 14), bg="#F5F5DC", fg="#800000").pack(pady=10)
username_entry = tk.Entry(login_window, font=("Arial", 14))
username_entry.pack(pady=5)

tk.Label(login_window, text="Password:", font=("Arial", 14), bg="#F5F5DC", fg="#800000").pack(pady=10)
password_entry = tk.Entry(login_window, show="*", font=("Arial", 14))
password_entry.pack(pady=5)

tk.Button(login_window, text="Login", command=validate_login, bg="#800000", fg="#FFFFFF", font=("Arial", 14)).pack(pady=20)
login_window.mainloop()
 
 