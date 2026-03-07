
## 🚀 Pipeline Execution

This project follows an **MLOps pipeline architecture** where data is automatically fetched from **MongoDB**, processed, and prepared for machine learning.

run the pipeline.

---

### 🌐 Step 1 — Configure MongoDB Connection

Before running the pipeline, set the MongoDB connection string as an **environment variable**.

#### Linux 

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/?appName=Cluster0"
````

#### Windows (PowerShell)

```powershell
$env:MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/?appName=Cluster0"
```

This variable allows the project to securely connect to **MongoDB Atlas** without hardcoding credentials in the codebase.

---

### ⚡ Step 2 — Run the Pipeline

Execute the demo script to start the **data ingestion pipeline**.

```bash
python demo.py
```

---

### 🧠 What Happens During Execution?

When the pipeline runs, it performs the following steps automatically:

1.  Connects to **MongoDB Atlas**
2.  Extracts visa application data
3.  Stores the dataset in the **Feature Store**
4.  Splits the dataset into **Training and Testing sets**
5.  Saves artifacts for the next pipeline stages

---

### 📂 Generated Artifacts

After execution, the project will create the following structure:

```
artifact/
 └── timestamp/
      └── data_ingestion/
           ├── feature_store/
           │     └── visa.csv
           │
           └── ingested/
                 ├── train.csv
                 └── test.csv
```

Each pipeline run creates a **new timestamped artifact folder**, ensuring experiment reproducibility.

---

### 📚 References

* MongoDB Connection Strings
  [https://www.mongodb.com/docs/manual/reference/connection-string/](https://www.mongodb.com/docs/manual/reference/connection-string/)

* Python Environment Variables
  [https://docs.python.org/3/library/os.html#os.environ](https://docs.python.org/3/library/os.html#os.environ)

```
```
