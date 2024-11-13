# Cat API Test Suite

This is a basic test suite for validating the image retrieval feature of [The Cat API](https://thecatapi.com/) using
Python's Requests and Pytest libraries.

## Setup

1. Clone the repository.
2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Obtain an API key from [The Cat API](https://thecatapi.com/).
5. Create a `.env` file in the root directory with your API key and other settings:

   ```plaintext
   CAT_API_KEY=YOUR_API_KEY
   CAT_API_URL=https://api.thecatapi.com/v1
   LOG_LEVEL=DEBUG
   ```

## Running Tests

To run tests and generate an HTML report, use:

```bash
pytest
```
Default report location is under [report](report) directory.

You can run also specific levels, and specify different report name, for example:

```bash
pytest -m smoke --html=report/smoke_report.html
```
```bash
pytest -m regression --html=report/regression_report.html
```


## Test Scenarios

1. **Get a Single Image**: Verify a single image can be retrieved with a URL.
2. **Get Multiple Images**: Retrieve multiple images with different limits using parameterized values (5, 10, 15).
3. **Handle Negative Image Limits**: Validate handling of negative limits by expecting a fallback to 1 image.
4. **Get Images by Specific Breed**: Test retrieving images for different breeds (e.g., `beng`, `abys`, `siam`).
5. **Get Images with Unknown Breed ID**: Confirm no results are returned for unknown breed IDs.

## Configurations

- **CAT_API_KEY**: Required for authentication with The Cat API.
- **CAT_API_URL**: Base URL for The Cat API.
- **LOG_LEVEL**: Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).

---
