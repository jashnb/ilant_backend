## Getting Started

Clone the repository on your local machine

```bash
git clone https://github.com/jashnb/ilant_backend.git
```

### Installation

1. Python
    
    Download and install Python 3.11 from their [official website](https://www.python.org/downloads) 
2. Create virtual environment

    ```bash
    cd ilant_backend
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install requirements

    ```bash
    pip install -r requirements.txt
    ```

### Run the Fast API Application

```bash
uvicorn main:app --reload
```

The server will be running on [http://localhost:8000](http://localhost:8000)

### Access the endpoint

Once the server is running, you can access the search endpoint by navigating to `http://127.0.0.1/8000/api/search-books/?query=python&page=1&itemsPerPage=10`

## Endpoint documentation

To test out the endpoint, or to verify the documentation of the API please visit [here](http://127.0.0.1:8000/docs)