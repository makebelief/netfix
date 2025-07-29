# Netfix

A Django-based web application for managing network services and user requests.

## Author
- Shayo Victor
- Zone01 Kisumu Student

## Description
Netfix is a web application built with Django that provides a platform for managing network services and user requests. The application includes user authentication, service management, and request handling features.

## Features
- User registration and authentication
- Service management
- Request handling
- Static file serving
- Responsive design

## Prerequisites
- Python 3.x
- pip (Python package installer)
- make (for using Makefile commands)

## Installation and Setup

1. Clone the repository
```bash
git clone https://learn.zone01kisumu.ke/git/svictor/netfix.git
cd netfix
```

2. Set up a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies and run migrations
```bash
make all
```

Or install components separately:
```bash
make install  # Install dependencies
make migrate  # Run database migrations
make run     # Start the development server
```

## Available Make Commands
- `make install` - Install Python dependencies
- `make migrate` - Run database migrations
- `make run` - Start the development server
- `make test` - Run tests
- `make shell` - Open Django shell
- `make clean` - Clean Python cache files
- `make createsuperuser` - Create a superuser account
- `make all` - Run install, migrate, and start server

## How to Contribute

1. Fork the repository on [Zone01 Kisumu Gitea](https://learn.zone01kisumu.ke/git/svictor/netfix)

2. Clone your forked repository
```bash
git clone https://learn.zone01kisumu.ke/git/YOUR_USERNAME/netfix.git
cd netfix
```

3. Create a new branch for your feature
```bash
git checkout -b feature/your-feature-name
```

4. Make your changes and commit them
```bash
git add .
git commit -m "Add your commit message"
```

5. Push to your branch
```bash
git push origin feature/your-feature-name
```

6. Create a Pull Request from your forked repository to the main repository

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
- Shayo Victor
- Platform: Zone01 Kisumu
- Repository: [https://learn.zone01kisumu.ke/git/svictor/netfix](https://learn.zone01kisumu.ke/git/svictor/netfix) 