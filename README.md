# 📔 Digital Diary: Personal CRUD Organizer

## 📝 Overview of the Project

The **Digital Diary** is a simple yet effective application designed to help users **Create, Read, Update, and Delete (CRUD)** personal diary entries, notes, and reminders. It serves as a centralized, digital organizer for managing daily thoughts, scheduling events, and tracking personal progress. The primary goal is to provide a clean, intuitive interface for personal information management.

---

## ✨ Features

* **Create Entries:** Easily add new diary entries, notes, or tasks with a title, date, and body content.
* **Read & View:** Entries are displayed chronologically, with the ability to search and filter by date or keywords.
* **Update & Edit:** Modify existing entries instantly to correct mistakes or add more details.
* **Delete Entries:** Permanently remove old or unnecessary entries.
* **Date Stamping:** Automatic date and time stamping for every entry to ensure accurate record-keeping.
* **User Authentication (Optional/Planned):** Secure user login/registration to protect personal data.

---

## 🛠️ Technologies/Tools Used

This project is built using a modern, efficient, and widely-adopted technology stack:

* **Frontend:** **React** (or preferred frontend framework like Vue.js/Angular) for building the user interface.
    * **Styling:** **Tailwind CSS** (or Bootstrap/Styled Components) for responsive and fast styling.
* **Backend:** **Node.js** with the **Express.js** framework.
* **Database:** **MongoDB** (a NoSQL database) for flexible and scalable storage of diary entries.
* **Package Manager:** **npm** or **Yarn**.

---

## 🚀 Steps to Install & Run the Project

Follow these steps to get a copy of the project up and running on your local machine.

### Prerequisites

* Node.js (LTS recommended)
* MongoDB instance (local or Atlas connection string)
* Git

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone [repository-url]
    cd digital-diary-organizer
    ```

2.  **Install Dependencies:**
    Navigate to both the `client` (frontend) and `server` (backend) directories and install dependencies.
    ```bash
    # Install backend dependencies
    cd server
    npm install

    # Install frontend dependencies
    cd ../client
    npm install
    ```

3.  **Configure Environment Variables:**
    In the `server` directory, create a file named `.env` and add your MongoDB connection string and port:
    ```
    PORT=5000
    MONGO_URI="[Your MongoDB Connection String Here]" 
    ```

### Running the Application

1.  **Start the Backend Server:**
    Navigate to the `server` directory and run the following command:
    ```bash
    cd server
    npm start 
    # The API server will run on http://localhost:5000 (or your specified port)
    ```

2.  **Start the Frontend Client:**
    Open a new terminal, navigate to the `client` directory, and run:
    ```bash
    cd client
    npm start
    # The application will open in your browser at http://localhost:3000
    ```

---

## ✅ Instructions for Testing

The application includes unit and end-to-end tests to ensure core functionality works as expected.

### Unit Tests

Unit tests are implemented using **Jest** (or Mocha/Chai) for the backend logic and service functions.

* **Run Backend Tests:**
    ```bash
    cd server
    npm test
    ```

### End-to-End (E2E) Testing

E2E tests (using **Cypress** or similar tools) verify the entire CRUD workflow from the user's perspective.

* **Run Frontend E2E Tests:**
    ```bash
    cd client
    # Assuming Cypress is used
    npx cypress open 
    ```
    * *Note: Ensure both the frontend and backend servers are running before starting E2E tests.*

---

## 📸 Screenshots 


<img width="1021" height="581" alt="UPDATE ENTRY png" src="https://github.com/user-attachments/assets/96f7b76a-3942-4277-8931-3ed394f813fb" />
<img width="866" height="611" alt="DELETE ENTRY png" src="https://github.com/user-attachments/assets/f45952dd-3c95-47d5-9e0f-7db41912ca49" />
<img width="786" height="369" alt="READ ALL ENTRIES png" src="https://github.com/user-attachments/assets/daf401cf-a594-4e12-8ad4-505b5599383b" />
<img width="591" height="289" alt="CREATE ENTRY png" src="https://github.com/user-attachments/assets/b1304d38-33ee-41b8-99fa-1bf604e00b8a" />
<img width="690" height="288" alt="EXIT png" src="https://github.com/user-attachments/assets/34d97a08-e2c4-4627-b106-3f91a9f341ce" />
