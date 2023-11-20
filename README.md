# Test Task 2

## Overview

This application is a bot designed to solve capche.

## Prerequisites

- **Required**: Python 3.x
- **For pip method**: pip
- **For poetry method**: poetry
- **For Docker method**: Docker

## Installation & Usage

---

### Method 1: Using pip

#### Step 1: Clone the repository
Execute the following command:
```
git clone https://github.com/DmitroPodolsky/test_task_2.git
```

#### Step 2: Navigate to the project directory
Execute the following command:
```
cd test_task_2
```

#### Step 3: Install required packages
Execute the following command:
```
pip install -r requirements.txt
```

#### Step 4: Run the bot
Execute the following command:
```
python -m bot
```

---

### Method 2: Using poetry

#### Step 1: Clone the repository
Execute the following command:
```
git clone https://github.com/DmitroPodolsky/test_task_2.git
```

#### Step 2: Navigate to the project directory
Execute the following command:
```
cd test_task_2
```

#### Step 3: Install the project and dependencies
Execute the following command:
```
poetry install
```

#### Step 4: Run the bot
Execute the following command:
```
poetry run python -m bot
```

---

### Method 3: Using Docker

#### Step 1: Clone the repository
Execute the following command:
```
git clone https://github.com/DmitroPodolsky/test_task_2.git
```

#### Step 2: Navigate to the project directory
Execute the following command:
```
cd test_task_2
```

#### Step 3: Place the token_session.json file in the 'data' directory
Note: The JSON file should contain {'token': your_session_token}.

#### Step 4: Build and run the Docker container
Execute the following command:
```
docker-compose up --build
```
