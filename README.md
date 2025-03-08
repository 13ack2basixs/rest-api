# Student Management REST API

## Scenario Overview

This REST API is designed to manage student records, including their cumulative GPA and reassignments of teachers to students. It allows:

1. Retrieving all students with their respective teacher and cumulative GPA.
2. Filtering students' GPA data based on a specific timeframe (semester range).
3. Reassigning a student to a different teacher.

This API is built using **Flask**. The database is managed using **PostgreSQL** by [**Neon**](https://neon.tech/).

---

## Database Structure

The database consists of four main tables:

### Student Table (`student`)

| Column       | Type     | Description                 |
| ------------ | -------- | --------------------------- |
| `id`         | INT (PK) | Unique student ID           |
| `name`       | STRING   | Name of the student         |
| `teacher_id` | INT (FK) | Foreign key to `teacher.id` |

### Teacher Table (`teacher`)

| Column | Type     | Description         |
| ------ | -------- | ------------------- |
| `id`   | INT (PK) | Unique teacher ID   |
| `name` | STRING   | Name of the teacher |

### Grade Table (`grade`)

| Column        | Type     | Description                  |
| ------------- | -------- | ---------------------------- |
| `id`          | INT (PK) | Unique grade ID              |
| `student_id`  | INT (FK) | Foreign key to `student.id`  |
| `semester_id` | INT (FK) | Foreign key to `semester.id` |
| `gpa`         | FLOAT    | GPA for the semester         |

### Semester Table (`semester`)

| Column          | Type     | Description                                 |
| --------------- | -------- | ------------------------------------------- |
| `id`            | INT (PK) | Unique semester ID                          |
| `semester_name` | STRING   | Name of the semester (e.g., `2023-2024_S1`) |

---

## REST API Endpoints

### **1. Get All Students with Cumulative GPA**

- **Endpoint:** `GET /api/students`
- **Description:** Retrieves all students, their assigned teacher, and their cumulative GPA.
- **Response Example:**

  ```json
  [
    {
      "Name": "Alice",
      "Teacher's Name": "Prof. Sanka",
      "cGPA": 3.5
    },
    {
      "Name": "Bob",
      "Teacher's Name": "Prof. Henry",
      "cGPA": 2.8
    }
  ]
  ```

- **Error Responses:**

> | Status Code | Message               | Reason                           |
> | ----------- | --------------------- | -------------------------------- |
> | `404`       | `"No students found"` | If no students exist in database |

### **2. Reassign a Student's Teacher**

- **Endpoint:** `PUT /api/students/<int:student_id>/reassign`
- **Description:** Reassigns a student to a different teacher.
- **Path Parameters:**

| Parameter    | Type | Description       | Example |
| ------------ | ---- | ----------------- | ------- |
| `student_id` | INT  | Unique student ID | `1`     |

- **Response Example:**

  ```json
  {
    "message": "Student reassigned successfully",
    "student": "Alice",
    "updated_teacher": "Prof. Sanka"
  }
  ```

- **Error Responses:**

> | Status Code | Message                                    | Reason                                  |
> | ----------- | ------------------------------------------ | --------------------------------------- |
> | `400`       | `"Invalid Student ID"`                     | If student ID doesn't exist in database |
> | `400`       | `"No available teachers for reassignment"` | If no other teachers exist in database  |

### **3. Get Students' cGPA for a Specific Timeframe**

- **Endpoint:** `GET /api/students/cgpa-timeframe/<string:start_sem>/<string:end_sem>`
- **Description:** Retrieves the cumulative GPA of all students for a specific semester range.
- **Path Parameters:**

| Parameter   | Type   | Description    | Example        |
| ----------- | ------ | -------------- | -------------- |
| `start_sem` | STRING | Start semester | `2024-2025_S1` |
| `end_sem`   | STRING | End semester   | `2024-2025_S2` |

- **Response Example:**

  ```json
  [
    {
      "Name": "Alice",
      "Teacher's Name": "Prof. Sanka",
      "cGPA": 4.0
    },
    {
      "Name": "Bob",
      "Teacher's Name": "Prof. Sanka",
      "cGPA": 3.8
    }
  ]
  ```

- **Error Responses:**

> | Status Code | Message                             | Reason                                              |
> | ----------- | ----------------------------------- | --------------------------------------------------- |
> | 400         | `"Invalid semester names provided"` | If the semester name is incorrect or does not exist |
> | 400         | `"Invalid timeframe selected."`     | If no grades exist for the selected timeframe       |
> | 404         | `"No students found"`               | If no students are found in the database            |
