# API Documentation

## Overview
This API allows users to generate recipes and search for images based on a query.

## Endpoints

### 1. Generate Response
- **URL**: `/prompt`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Request Body**:
    ```json
    {
        "prompt": "your_prompt_here"
    }
    ```

### 2. Search Images
- **URL**: `/search_images`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Request Body**:
    ```json
    {
        "query": "your_search_term"
    }
    ```

## Using the `/search_images` Endpoint in Postman

To use the `/search_images` endpoint in Postman, follow these steps:

1. **Open Postman**: Launch the Postman application.

2. **Create a New Request**:
   - Click on the "New" button or the "+" tab to create a new request.

3. **Set the Request Type**:
   - Change the request type from "GET" to "POST" using the dropdown menu.

4. **Enter the URL**:
   - In the URL field, enter the endpoint URL, which is typically `http://localhost:5000/search_images` (adjust the port if your Flask app is running on a different one).

5. **Set the Headers**:
   - Click on the "Headers" tab.
   - Add a new header with the key `Content-Type` and the value `application/json`.

6. **Add the JSON Body**:
   - Click on the "Body" tab.
   - Select the "raw" radio button.
   - Choose "JSON" from the dropdown menu that appears next to the "raw" option.
   - Enter your JSON data in the text area. For example:
     ```json
     {
         "query": "cats"
     }
     ```
   - Replace `"cats"` with the actual term you want to search for.

7. **Send the Request**:
   - Click the "Send" button to send the request to your Flask app.

8. **View the Response**:
   - After sending the request, you will see the response from the server in the lower section of Postman. If successful, it will show the images returned by the endpoint. If there is an error, it will display the error message.

## Example JSON Body
To search for images related to "cats":
