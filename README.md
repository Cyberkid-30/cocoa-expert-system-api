# **CocoaCare: Intelligent Crop Health Assistant API Documentation**

This API enables users to diagnose cocoa crop diseases, manage user accounts, and interact with the expert system. It uses SQLite as the database and Flask for the backend.

---

## **Base URL**

The API runs on:

```
https://cocoa-expert-system.onrender.com
```

---

## **Authentication**

All endpoints (except signup and login) require authentication via JWT tokens.  
Include the token in the `Authorization` header for protected routes:

```
Authorization: Bearer <your_access_token>
```

---

## **Endpoints**

### **1. User Authentication**

#### **1.1 Signup**

**Endpoint**: `/auth/signup`  
**Method**: `POST`  
**Description**: Create a new user account.

**Request Body**:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Response**:

- **201 Created**:
  ```json
  {
    "message": "User created successfully"
  }
  ```
- **400 Bad Request**:
  ```json
  {
    "error": "User already exists"
  }
  ```

---

#### **1.2 Login**

**Endpoint**: `/auth/login`  
**Method**: `POST`  
**Description**: Log in and receive a JWT token.

**Request Body**:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Response**:

- **200 OK**:
  ```json
  {
    "access_token": "<your_access_token>"
  }
  ```
- **401 Unauthorized**:
  ```json
  {
    "error": "Invalid credentials"
  }
  ```

---

Here’s the refactored section of the README to reflect the new structure and validation for the `/diagnose` endpoint:

---

### **2. Disease Diagnosis**

#### **2.1 Diagnose Disease and Provide Solutions**

**Endpoint**: `/diagnose`  
**Method**: `POST`  
**Description**: Diagnose a cocoa crop's condition based on input facts.

**Headers**:

```json
{
  "Authorization": "Bearer <your_access_token>"
}
```

**Request Body**:  
Provide details about the crop's condition.

```json
{
  "disease": "Damping-off",
  "growth_stage": "germination",
  "seedlings_exposed_to_sunlight": true,
  "soil_moisture": 25,
  "soil_type": "sterilized",
  "temperature": 30
}
```

**Request Validation**:

- The `disease` field must be a string matching one of the diseases available from the `/diseases` endpoint.
- The `growth_stage` must be one of the following values:
  - `"germination"`
  - `"seedling"`
  - `"nursery"`
- The `seedlings_exposed_to_sunlight` must be `true` or `false`.
- The `soil_moisture` must be a numeric value.
- The `soil_type` must be either `"sterilized"` or `"non-sterilized"`.
- The `temperature` must be a numeric value.

**Response**:

- **200 OK**:  
  Returns recommended actions based on the provided data.

  Example:

  ```json
  {
    "actions": [
      "Irrigate the plants",
      "Maintain a cool, dry environment",
      "Reduce watering and improve drainage"
    ]
  }
  ```

- **400 Bad Request**:  
  Example:

  ```json
  {
    "error": "Invalid input. Ensure 'disease' matches one from the /diseases endpoint."
  }
  ```

- **401 Unauthorized**:  
  Example:
  ```json
  {
    "error": "Missing or invalid token"
  }
  ```

**Notes**:

- Make a `GET` request to `/diseases` to retrieve the list of diseases supported by the system.

---

#### **2.2 Protected Test Endpoint**

**Endpoint**: `/api/protected`  
**Method**: `GET`  
**Description**: A test endpoint to verify authentication.

**Headers**:

```json
{
  "Authorization": "Bearer <your_access_token>"
}
```

**Response**:

- **200 OK**:
  ```json
  {
    "message": "Hello user <user_id>"
  }
  ```

---

### **3. Diseases**

**Endpoint**: `/diseases`  
**Method**: `GET`  
**Description**: Returns a reponse object with an array of the list of diseases available to the system.

---

### **4. Error Responses**

For all endpoints, common errors include:

- **400 Bad Request**: Invalid or missing data in the request body.
- **401 Unauthorized**: Missing or invalid JWT token.
- **500 Internal Server Error**: Issues with the server or database.

---

## **Example Workflow**

1. **Sign Up**:
   Send a `POST` request to `/auth/signup` with username and password.

2. **Log In**:
   Send a `POST` request to `/auth/login` to receive an access token.

3. **Diagnose Disease**:
   Use the access token in the `Authorization` header to send a `POST` request to `/api/diagnose` with facts about the crop.

---

## **Tools for Testing**

- **Postman**: For manual API testing.
- **curl**: Command-line tool for testing API requests.
- **Frontend**: Use a React frontend to interact with the API.

---

If you encounter any issues or have questions, feel free to reach out!
