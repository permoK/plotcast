# Sacco Management API

## Prerequisites
- Python 3.8+
- Django 3.2+
- Django REST Framework
- Django REST Framework Token Authentication

## Installation

1. Clone the repository
```bash
git clone your-repo-url
cd sacco-management
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure Database
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

## Authentication Flow

### 1. Sacco Owner Registration
- First user registers as a Sacco owner
- Creates both user and Sacco simultaneously
- Receives authentication token

### 2. Member Registration
- Only Sacco owners can register new members
- Members are added to the owner's Sacco
- Owner must be authenticated

### 3. Login
- Authenticate using phone number and 4-digit PIN
- Receive authentication token
- Token used for subsequent authenticated requests

## Security Features
- PIN-based authentication
- Token-based access control
- Secure PIN hashing with salt
- Permissions-based access to endpoints

## Postman Testing

### Environment Variables
Set up the following in Postman:
- `base_url`: Your API base URL
- `token`: Authentication token (updated after login)

### Test Sequence
1. Owner Registration
2. Owner Login
3. Register Members
4. Member Login
5. Logout

## Common Validations
- Phone number: +999999999 format
- PIN: Exactly 4 digits
- Unique phone numbers
- Active user status check

## Deployment Recommendations
- Use HTTPS
- Implement rate limiting
- Add comprehensive logging
- Secure secret keys and settings
- Use environment-based configuration

## Troubleshooting
- Ensure all dependencies are installed
- Check database migrations
- Verify authentication token handling
- Review permission configurations

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
[Specify Your License]
