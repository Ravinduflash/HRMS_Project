# StreamlineHR - HRMS Project

## About This Repository

Welcome to the **StreamlineHR** repository, housing the source code for a comprehensive **Human Resource Management System (HRMS)**. Developed as part of the Business Application Development Module in the Bachelor of Business Science degree program, StreamlineHR is tailored to facilitate HR functions, automate workflows, and improve efficiency within organizations.

## Project Overview

StreamlineHR is a robust, scalable HRMS designed to streamline various HR processes through an intuitive and user-friendly interface. The application includes dedicated dashboards for **HR Managers** and **Employees**, ensuring role-specific access and functionality for a seamless experience. The key functionalities provided in StreamlineHR include:

- **Employee Profile Management**: Maintain comprehensive profiles for each employee, including personal details, employment history, and skills.
- **Leave Management**: Automate the leave application and approval process, ensuring transparency and efficiency.
- **Attendance Tracking**: Record attendance data, track employee hours, and generate reports to assist in payroll calculations.
- **Payroll Management**: Automate payroll processing, calculate deductions, and generate payslips.
- **Performance Reviews**: Facilitate employee evaluations, enabling HR managers to track and review performance.
- **Training Management**: Organize and manage training programs, track participation, and store certification records.
- **Document Management**: Securely store and manage employee documents, such as contracts, ID proofs, and certifications.
- **Task Management**: Assign and track tasks across teams, ensuring accountability and clear communication.
- **Announcements and News**: Share important updates, announcements, and company news with employees through a centralized system.

## Key Features

StreamlineHR is built with several essential features to meet modern HR needs:

- **User Authentication and Role-based Access Control**: Secure login with separate access controls for HR managers and employees.
- **Interactive Dashboards**: Real-time data updates and insights tailored to the user’s role (HR manager or employee).
- **Employee Data Management**: A centralized repository for all employee-related data, easily accessible for HR managers.
- **Leave Request and Approval System**: Employees can submit leave requests, while HR managers review and approve them in an organized workflow.
- **Integrated Chatbot**: Provides on-demand assistance, answering common questions and guiding users through the application.
- **Responsive Design**: Built to adapt to various screen sizes and devices for seamless accessibility.

## Technology Stack

The application is built using a robust technology stack to ensure security, performance, and scalability:

- **Backend**: Django (Python), providing a strong foundation with Django’s ORM and security features.
- **Frontend**: HTML, CSS, JavaScript for creating a clean and user-friendly interface.
- **UI Framework**: Bootstrap, offering responsive design capabilities and a consistent look and feel.
- **Database**: [SQLite] to store and manage HR data.
- **Additional Libraries**:
  - Django REST Framework for building APIs
  - [Chatbot API]

## Getting Started

To set up the StreamlineHR project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/streamlinehr.git
   cd streamlinehr
   ```

2. **Install Dependencies**:
   Ensure you have Python and pip installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the Database**:
   Configure your database settings in `settings.py`, and ensure the database is running.

4. **Run Migrations**:
   Apply migrations to set up the database tables:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser** (optional for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the Development Server**:
   Launch the application locally:
   ```bash
   python manage.py runserver
   ```
   The application will be available at `http://127.0.0.1:8000`.

## Usage

- **Access the Application**: Log in with an HR manager or employee account.
- **Navigation**: Use the sidebar to navigate between modules such as **Employee Profiles**, **Leave Management**, **Payroll**, and **Tasks**.
- **Admin Panel**: For administrative users, access to the Django admin panel provides additional data management capabilities.

## Contributing

This project is part of an academic program, and external contributions are currently restricted. However, feedback and suggestions are highly appreciated. Feel free to open an issue if you have any insights or improvement ideas.

## License

This project is licensed under the [MIT License](LICENSE), allowing for both academic and personal use. Please review the license file for more details.

## Acknowledgments

- Thanks to the open-source community for libraries, tools, and resources that made this project possible.
- Special recognition to Django, Bootstrap, and all additional libraries and resources integrated into the project.

## Contact

For further inquiries, support, or project-related discussions, please contact [dulshanravindu505@gmail.com] or open an issue in this repository. We appreciate your interest and look forward to any valuable insights you may offer!
```

