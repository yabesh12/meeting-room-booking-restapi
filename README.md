# Meeting Room Booking System

## Overview
The Meeting Room Booking System that allows users to book meeting rooms, view available meeting rooms, and manage their bookings.

## Features

### 1. Members Login
- Endpoint: `/api/v1/login/`
- Method: POST
- Members can log in using their email and password. Self-registration is    not permitted; members are created exclusively through Django admin, and only they can access the login functionality.

### 2. List Available Meeting Rooms
- Endpoint: `/api/v1/meeting-rooms/`
- Method: GET
- Lists all available meeting rooms based on the specified time range.

### 3. Book a Meeting Room
- Endpoint: `/api/v1/meeting-rooms/book/<int:room_id>/`
- Method: POST
- Parameters:
  - `start_time` (str): Start time of the booking.
  - `end_time` (str): End time of the booking.
  - `no_of_persons` (int, optional): Number of persons for the booking (default is 1).
- Books a meeting room for the specified time range.
- After Booking mail will send to the one who booked

### 4. List My Bookings
- Endpoint: `api/v1/meeting-rooms/my-bookings/`
- Method: GET
- Lists all booked meeting rooms history for a requested user.

### 5. Cancel Meeting Room Booking
- Endpoint: `/api/v1/meeting-rooms/cancel/<int:booking_id>/`
- Method: DELETE
- Cancels a previously booked meeting room.
- Conditions:
  - The meeting room can be canceled only by the user who made the booking.
  - Cancellation is not allowed if the start time has already passed.
- After Cancellation mail will send to the one who booked


### 6. Mail send after booking and cancel booking Feature added

### 7. Unit Test cases
- To run the tests ```python manage.py test```


## Setup Instructions

### Installation
-  Clone the repository:
   ```bash
   git clone https://github.com/your-username/meeting-room-booking.git
    ```
-  Install dependencies
    ```
   cd meeting-room-booking
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py loaddata fixtures/data.json
   ```
- Note - 
  need to create user in django-admin for login

