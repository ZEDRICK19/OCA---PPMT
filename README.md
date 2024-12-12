# OFFICE OF CULTURE AND ARTS - PERFORMER'S PROFILE AND  MEMBERSHIP TRACKER

**OVERVIEW**

	The Office of Culture and Arts - Performer's Profile and Membership Tracker (OCA-PPMT) is an centralized system designed exclusively for the administrative staff of the Office of Culture and Arts at Batangas State University - The National Engineering University Alangilan Campus. This system focuses on managing and tracking the profiles of select cultural groups, allowing for a more personalized and effective management system that caters specifically to their unique needs. The OCA-PPMT simplifies and organizes the process of inputting and updating essential information including personal details, educational backgrounds, artistic achievements and group affiliations. This focused approach ensures that the data remains accurate and relevant,  facilitating better communication and collaboration among staff members.

	Additionally, the OCA-PPMT is designed for administrative use, it also supports the preservation and promotion of diverse cultural traditions. By documenting performances, workshops, and other activities, the system helps staff showcase the artistic diversity,  making it easier for the office to manage performers’ talents, facilitate engagement, and highlight the richness of cultural diversity through its members. This not only highlights individual performers' accomplishments but also fosters a sense of community and collaboration among students, faculty, and staff.

	The OCA-PPMT also enhances institutional integrity by ensuring that all data is managed ethically. The system is designed with strict data management practices that safeguard member information while promoting accountability within the Office of Culture and Arts. By providing a reliable framework for tracking profiles, affiliations, and achievements, OCA-PPMT strengthens the office's role as a trustworthy entity within the university.


	In summary, the Office of Culture and Arts - Performer's Profile and Membership Tracker (OCA - PPMT) is an essential tool for the administrative staff at Batangas State University. By streamlining data management processes focused on select cultural groups, promoting cultural engagement, and ensuring ethical data practices, OCA-PPMT empowers staff to support performers effectively. This innovative platform not only enhances operational efficiency but also nurtures an inclusive environment where artistic expression can thrive, enriching the cultural landscape of the university community.

**EXPLANATION OF HOW PYTHON CONCEPTS, LIBRARIES, ETC. WERE APPLIED**

	For the Office of Culture and Arts - Performer’s Profile and Membership Tracker (OCA - PPMT), I used Python in Visual Studio Code to create an organized, web-based system for tracking performances, achievements, and group memberships. This project wants to help the long-term development of artistic talent by making data more accessible and manageable.

	The Office of Culture and Arts - Performer’s Profile and Membership Tracker (OCA - PPMT) leverages various Python concepts and libraries to deliver a fit and user-friendly application. The Tkinter library, the standard GUI library for Python, was employed to create a visually appealing interface with windows, labels, buttons, entry widgets, scrollbars, and treeviews. This enabled the development of a comprehensive user interface that facilitates effortless interaction with the application. Additionally, the SQLite3 database was used to store and manage performer data, allowing for efficient data retrieval and manipulation. 

	Python's modular design principles were applied through the creation of well-defined functions to handle various tasks, such as validating login credentials, managing group selections, adding members, inputting educational details, and recording participation information. Global variables like tree_groups and selected_group_name were used to maintain essential data across functions and windows. The application also utilized Python's built-in features, such as functions and data types, to effectively manage data and perform complex operations. The Treeview widget was used to display tabular data in a hierarchical structure, enabling users to easily navigate and visualize performer information. Overall, the application showcases a thoughtful application of Python concepts, libraries, and features to deliver a comprehensive and efficient performer tracking solution for the Office of Culture and Arts.

**SUSTAINABLE DEVELOPMENT GOALS**

	The Sustainable Development Goals are actively promoted by the Office of Culture and Arts - Performer's Profile and Membership Tracker (OCA-PPMT), which promotes an inclusive and organized approach to managing the development of cultural talents. Specifically focusing on SDG 4 (Quality Education), SDG 11 (Sustainable Cities and Communities), and SDG 16 (Peace, Justice, and Strong Institutions). OCA-PPMT helps Batangas State University maintain a sustainable, well-organized, and culturally lively educational environment by managing memberships and handling data in an effective way.

SDG 4 (Quality Education)
	OCA - PPMT supports lifelong learning in the arts by making it simple to track each member's information, from academic performance to cultural contributions. When an individual joins, we gather data about their educational background and artistic achievements to create a comprehensive picture of their artistic career. By tracking members' development over time, the Office of Culture and Arts can help performers achieve their full potential while recognizing their efforts and promoting continuous learning in the arts.

SDG 11 (Sustainable Cities and Communities)
	Culture is at the heart of every community, and our institution is successful in preserving it by commemorating the outstanding achievements that each cultural group undertakes at Batangas State University - The National Engineering University. From dance performances to visual art shows, we maintain chronological documentation of all cultural contributions, allowing us to reflect on and appreciate each group's unique traits. By gathering and continuing to preserve this cultural information, OCA- PPMT ensures that the legacy of these talents remains accessible, promoting a lasting connection to culture and arts for current and future students alike.

SDG 16 (Peace, Justice, and Strong Institution)
Creating a transparent, organized system for managing member data strengthens the institution's cultural basis by ensuring that all data is handled ethically and clearly. OCA-PPMT provides the Office of Culture and Arts with an effective tool for storing profiles, tracking member affiliations, and managing achievements, enhancing the Office of Culture and Arts’ reliability as a trustworthy entity within the university. This commitment to ethical data management promotes accountability in institutional practices.

	In conclusion, the OCA-PPMT is not only beneficial for the administration and staff of the Office of Culture and Arts but also significantly contributes to achieving key Sustainable Development Goals by creating an environment that welcomes everyone and helps with learning, keeps cultural traditions alive, and ensures honesty in our institution.

**INSTRUCTIONS FOR RUNNING THE PROGRAM**

To run the Office of Culture and Arts - Performer’s Profile and Membership Tracker (OCA - PPMT) application, follow these instructions: 

1. Install Python: Ensure that Python is installed on your system. You can download the latest version of Python from the official website at https://www.python.org/downloads/. 
2. Library Installation: Before running the application, install the required libraries using the following commands in the terminal: ``` pip install tk pip install sqlite3 ``` 
3. Download the Code: Download the source code files for the OCA - PPMT application to your local system.
4. Open the Code: Open the main Python file (e.g., `main.py`) in your preferred Integrated Development Environment (IDE) or text editor. 
5. Run the Program: Run the Python script by executing the following command in the terminal: ``` python main.py ``` 
6. Explore the Application: Once the application launches, you can navigate through the user interface to manage performers' profiles, achievements, and group memberships efficiently. Use the provided features, buttons, and functionalities to input, store, and retrieve performer data seamlessly. 
7. Interact with the Interface: Explore the various functionalities of the application, such as adding performers, managing group affiliations, inputting educational details, and recording participation information. Follow the on-screen instructions and prompts to utilize the features effectively. 
8. Exit the Program: To exit the application, close the window or use the provided exit button within the user interface. By following these steps, you can successfully run the OCA - PPMT application and utilize its features to track and manage performers' profiles and memberships effectively within the Office of Culture and Arts organization.

Follow these steps to run the program effectively:

Login Function: 
INPUT
Username
Password
Input the username as "admin" and the password as "password" to log in and access the system. 

Upon successful login, you will be welcomed as the admin and redirected to the group selection window. 

Group Selection: 
SELECT GROUP
Select Group
Select a group from the list displayed in the window by clicking on it. 
Click on the "Select Group" button to manage the members of the selected group.

Member Management: 
INPUT
Add Member
In the member management window, you can view the members of the selected group along with their details such as name, age, and email. 
Click on the "Add Member" button to add a new member to the group. 

Add Member Window:
INPUT
First Name
Last Name
Middle Name
Address
Date-of-Birth
Age
Gender
Email Address
Contact Number
Guardian Name
Guardian Contact
2x2 Picture
In the "Add Member - Step 1: Personal Information" window, fill in the personal details of the new member such as first name, last name, address, date of birth, etc. 

Click on the "Next" button to move to the next step for educational information. 

Educational Information Window: 
INPUT
Campus
College
Program
SR-code
Year Level
Units per Semester
Enter the educational details of the member including campus, college, program, SR-Code, year level, and units per semester. 

Click on the "Next" button to proceed to the participation window. 

Participation Window: 
INPUT
Add Row
Event Date
Event Name
Level (Local, National, International)
Rank (Place)
Add participation details for the member by clicking on the "Add Row" button to include information such as event date, event name, level, and rank. 

Once all information is added, click on the "Save Member" button to save the member to the database. 

Successful Member Addition: 
The system will display a success message confirming that the member has been added successfully. 
VIEW FUNCTION
View Members
The member's information will be visible in the member management window under the selected group. To add, view, and save performer information within specified groups using the GUI interface provided in the code. This structured approach will help you navigate through the system and manage performers efficiently.
