* * *

Stock API Documentation
========================

This document provides an overview of the endpoints and usage for the Django API.

Setting Up the Project Locally
------------------------------

### Step 1: Clone the Repository

`git clone https://github.com/chaudharypraveen98/NiftyStockTracker.git`

### Step 2: Create and Activate a Virtual Environment

Choose or create a directory for your project and navigate to it using the terminal or command prompt. Then, run the following commands to create and activate a virtual environment:

#### On Windows:

`python -m venv venv venv\Scripts\activate`

#### On macOS/Linux:

`python3 -m venv venv source venv/bin/activate`

### Step 3: Install Project Dependencies

`pip install -r requirements.txt`

### Step 4: Run Migrations

`python manage.py migrate`

### Step 5: Create Admin User to view Django Dashboard
`python manage.py createsuperuser`
Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) For admin dashboard and login with the created credentials.

### Step 6: Load Data from CSV Files Using a Management Command [Not as Bonus Task but a feature for time being]

We can implement the upload file option but it takes time. First we input file from the user, store in the in memory  process and discard the file.

For download we can use 'csv' library with response as attachment
```
response = HttpResponse(content_type='text/csv')
response['Content-Disposition'] = 'attachment; filename="stock_data.csv"'
```

But for the time being i  have implemented other way.

To efficiently populate your SQLite database with stock market data obtained from the NSE India website, we've created a custom management command named `import_data`. This command is designed to streamline the migration process, allowing you to load data from CSV files into your database effortlessly.

**Usage:**

`python manage.py import_data ./stock/data/`

*   **`python manage.py`**: Initiates a Django management command.
    
*   **`import_data`**: Specifies the name of our custom command responsible for importing data.
    
*   **`./stock/data/`**: Indicates the directory where the CSV files containing stock market information are located.
    

#### How it Works:

1.  **Script Overview:**
    
    *   The `import_data` command is meticulously crafted to handle the migration of data from CSV files seamlessly.
2.  **Data Collection:**
    
    *   CSV files are collected from the NSE India website and stored in the specified `./stock/data/` directory.
3.  **Database Loading:**
    
    *   The command iterates through each CSV file, reading its entries.
4.  **Database Entry Creation:**
    
    *   For each entry in the CSV files, a corresponding database row is created, capturing the essential stock market information.

By executing this single command, you trigger a comprehensive process where the management command systematically reads and processes the CSV files, generating individual database entries for each piece of stock market data.

This approach provides a clean and efficient way to synchronize your database with the latest stock market information, ensuring that your application's data remains up-to-date and accurate.

### Step 5: Start the Development Server

`python manage.py runserver`

### Step 6: Access the API

Visit [http://127.0.0.1:8000/v1/stock-index](http://127.0.0.1:8000/v1/stock-index) in your web browser to access the API.

**Note:** When you're done working on your project, deactivate the virtual environment using:

`deactivate`

    

STOCK PRICES API Documentation
========================

This document provides an overview of the endpoints and usage for the Django API.

Stock Index Endpoints
---------------------

## Necessary Task

### List all Stock Index Entries

**Endpoint:**

`GET /v1/stock-index`

### Filter by Stock Index Name

**Endpoint:**

`GET /v1/stock-index/?index_name__name=NIFTY-50`

### Filter by Stock Shares Traded

**Endpoint:**

`GET /v1/stock-index/?shares_traded__gte=192845545`

### Filter by Stock Low Price

**Endpoint:**

`GET /v1/stock-index/?low_price__gte=43808.46`

## Extra / Bonus Routes

### Delete a Stock Index Entry

**Endpoint:**

`DELETE /v1/stock-index/<entry_id>`

Example:

`DELETE /v1/stock-index/1`

### Create a new Stock Index Entry

**Endpoint:**

`POST /v1/stock-index`

**Request Body:**

`{     "date": "2023-12-15",     "open_price": "123.00",     "high_price": "234.00",     "low_price": "234.00",     "close_price": "454.00",     "shares_traded": 100,     "turnover": "567.00",     "index_name": "NIFTY-50" }`

### Retrieve a Stock Index Entry

**Endpoint:**

`GET /v1/stock-index/<entry_id>`

Example:

`GET /v1/stock-index/1`

### Update a Stock Index Entry

**Endpoint:**

`PUT /v1/stock-index/<entry_id>/`

**Request Body:**

`{     "date": "2023-12-16",     "open_price": "123.00",     "high_price": "234.00",     "low_price": "234.00",     "close_price": "454.00",     "shares_traded": 359,     "turnover": "567.00",     "index_name": "NIFTY-50" }`


### Pagination 

We have implemented a robust pagination feature to enhance the browsing experience when accessing the stock market data through our API. The pagination system provides a structured and organized way to navigate through large sets of data.

Key Features:
* Base Page Size:
    The default page size for paginated responses is set to 25 entries per page.

* Configurability:
    You can easily configure the number of entries per page by utilizing the page_size parameter in your API requests. like [http://127.0.0.1:8000/v1/stock-index/?page_size=5](http://127.0.0.1:8000/v1/stock-index/?page_size=5)
* * *