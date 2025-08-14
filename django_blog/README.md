# 🔐 Authentication System Documentation

## Overview
This system allows users to:
- Register with username, email, and password
- Login and logout
- View and edit their profile

Built using Django's built-in auth system and custom views.

## Features

| Page | Function |
|------|---------|
| `/register/` | Custom form with email field |
| `/login/` | Django built-in `LoginView` |
| `/logout/` | Django built-in `LogoutView` |
| `/profile/` | View user details |
| `/profile/edit/` | Change email |

## Security
- All forms include `{% csrf_token %}`
- Passwords are hashed using Django's PBKDF2
- Profile editing requires login (`@login_required`)
- Logout redirects to home

## How to Test
1. Start server: `python manage.py runserver`
2. Visit `/register/` and create a user
3. Log in, view profile, edit email
4. Log out and try accessing `/profile/` → should redirect to login

## Code Structure
- **Form**: `CustomUserCreationForm` extends `UserCreationForm`
- **Views**: `register`, `profile`, `edit_profile`
- **Templates**: All in `blog/templates/blog/`
- **URLs**: Defined in `blog/urls.py`