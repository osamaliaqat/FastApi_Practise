# FastApi_Practise


## Installation

1. Clone this repository:

   ```
   git clone https://github.com/osamaliaqat/FastApi_Practise.git
   ```
   

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Start the server:

   ```
   uvicorn app.main:app --reload
   ```

   The server should now be running at http://localhost:8000.

## API Documentation

You can find the API documentation at http://localhost:8000/docs.

The following endpoints are available:

- `GET /pets`: Get a list of all pets.
- `GET /pets/{pet_id}`: Get a single pet by its ID.
- `POST /pets`: Create a new pet.
- `PUT /pets/{pet_id}`: Update an existing pet by its ID.
- `DELETE /pets/{pet_id}`: Delete an existing pet by its ID.


## Contributing

If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
