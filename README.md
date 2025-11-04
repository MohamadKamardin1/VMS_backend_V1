# VMS Project

## Installation

1. Clone the repository:
```
git clone https://github.com/MohamadKamardin1/VMS_backend_V1.git
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Apply the database migrations:
```
python manage.py migrate
```

5. Start the development server:
```
python manage.py runserver
```

## Usage

The VMS project is a Django-based Visitor Management System. It provides an API for managing visitor information and authentication.

## API

The VMS API is documented using the Spectacular library. You can access the API documentation at `/api/schema/swagger-ui/` when the development server is running.

The API supports the following endpoints:

- `/api/visitors/`: CRUD operations for visitor information.
- `/api/auth/`: Authentication endpoints for obtaining and refreshing JWT tokens.

## Contributing

Contributions to the VMS project are welcome. Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

## License

The VMS project is licensed under the [MIT License](LICENSE).

## Testing

To run the tests, use the following command:

```
python manage.py test
```

This will run the test suite for the VMS project.
