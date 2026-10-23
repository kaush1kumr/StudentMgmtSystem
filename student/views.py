from django.shortcuts import render


def home(request):

    students = [
        {
            'name': 'Rahul',
            'roll': '101',
            'course': 'B.Tech CSE',
            'cgpa': 8.7
        },
        {
            'name': 'Priya',
            'roll': '102',
            'course': 'B.Tech ECE',
            'cgpa': 7.8
        },
        {
            'name': 'Aman',
            'roll': '103',
            'course': 'B.Tech CSE',
            'cgpa': 9.1
        },
        {
            'name': 'Neha',
            'roll': '104',
            'course': 'B.Tech IT',
            'cgpa': 8.2
        }
    ]

    courses = [
        'Python Programming',
        'Web Development',
        'Data Structures',
        'Database Management'
    ]

    context = {
        'students': students,
        'courses': courses
    }

    return render(request, 'student/home.html', context)