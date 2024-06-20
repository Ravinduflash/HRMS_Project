from django.shortcuts import render

def hr_manager_dashboard(request):
    # Mock data for demonstration purposes
    context = {
        'num_employees': 120,
        'num_leave_requests': 15,
        'num_attendance_records': 110,
        'num_payroll_records': 10,
        'upcoming_birthdays': [
            {'name': 'John Doe', 'date': '2024-06-25'},
            {'name': 'Jane Smith', 'date': '2024-07-01'},
        ],
        'new_leave_requests': [
            {'employee_name': 'Alice Johnson', 'request_date': '2024-06-19'},
            {'employee_name': 'Bob Brown', 'request_date': '2024-06-18'},
        ]
    }
    return render(request, 'dashboard/hr_manager_dashboard.html' ,context)

def employee_dashboard(request):
    # Mock data for demonstration purposes
    context = {
        'num_employees': 120,
        'num_leave_requests': 15,
        'num_attendance_records': 110,
        'num_payroll_records': 10,
        'upcoming_birthdays': [
            {'name': 'John Doe', 'date': '2024-06-25'},
            {'name': 'Jane Smith', 'date': '2024-07-01'},
        ],
        'new_leave_requests': [
            {'employee_name': 'Alice Johnson', 'request_date': '2024-06-19'},
            {'employee_name': 'Bob Brown', 'request_date': '2024-06-18'},
        ]
    }
    return render(request, 'dashboard/employee_dashboard.html', context)
