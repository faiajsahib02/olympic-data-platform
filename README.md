# 🏅 Olympic Data ELT Pipeline

A production-ready data engineering project that implements an **Extract, Load, Transform (ELT)** pipeline for Olympic athlete events data using modern data stack technologies.

## 📊 Project Overview

This project demonstrates an end-to-end data pipeline that:
- **Extracts** Olympic athlete events data from CSV files
- **Loads** raw data into a PostgreSQL data warehouse
- **Transforms** data into clean, analytics-ready tables
- **Orchestrates** the entire workflow using Apache Airflow
- **Containerizes** all components using Docker for reproducibility

## 🛠️ Technical Skills Demonstrated

### **Data Engineering & ETL/ELT**
- ✅ Design and implementation of ELT pipeline architecture
- ✅ Data validation and quality checks
- ✅ Bronze → Silver layer transformation pattern
- ✅ Modular, maintainable code structure

### **Workflow Orchestration**
- ✅ **Apache Airflow** DAG development
- ✅ Task dependencies and scheduling
- ✅ PythonOperator, PostgresOperator, BashOperator
- ✅ Template search paths for SQL files
- ✅ Error handling and file validation

### **Database & SQL**
- ✅ **PostgreSQL** as data warehouse
- ✅ SQL transformations (DDL/DML)
- ✅ Data modeling (raw → silver tables)
- ✅ NULL handling with COALESCE
- ✅ Connection management with SQLAlchemy

### **Python Programming**
- ✅ **Pandas** for data manipulation
- ✅ **SQLAlchemy** for database connectivity
- ✅ Modular function design
- ✅ Exception handling and logging
- ✅ Package management

### **DevOps & Infrastructure**
- ✅ **Docker Compose** multi-container orchestration
- ✅ Service health checks and dependencies
- ✅ Volume management for persistence
- ✅ Environment variable configuration
- ✅ Container networking

### **Software Engineering Best Practices**
- ✅ Modular architecture with separation of concerns
- ✅ Reusable components (`modules/extraction.py`)
- ✅ Configuration management
- ✅ Version control ready
- ✅ Clear documentation

## 🏗️ Architecture

```
┌─────────────┐
│   CSV Data  │
└──────┬──────┘
       │ Extract
       ▼
┌─────────────────────────────┐
│   Apache Airflow DAG        │
├─────────────────────────────┤
│ 1. Install Dependencies     │
│ 2. Validate File Exists     │
│ 3. Load to PostgreSQL       │
│ 4. Transform (SQL)          │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│   PostgreSQL Warehouse      │
├─────────────────────────────┤
│ - raw_athlete_events        │
│ - silver_olympic_events     │
└─────────────────────────────┘
           │
           ▼
┌─────────────────────────────┐
│   pgAdmin (Visualization)   │
└─────────────────────────────┘
```

## 🚀 Getting Started

### Prerequisites
- Docker Desktop installed
- Docker Compose installed
- At least 4GB of available RAM

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/olympic-data-platform.git
   cd olympic-data-platform
   ```

2. **Start the entire stack**
   ```bash
   docker-compose up -d
   ```

3. **Wait for services to initialize** (~2-3 minutes)
   ```bash
   docker-compose logs -f airflow-init
   ```

4. **Access the interfaces**
   - **Airflow UI**: http://localhost:8080
     - Username: `airflow`
     - Password: `airflow`
   - **pgAdmin**: http://localhost:8081
     - Email: `admin@admin.com`
     - Password: `root`

### Running the Pipeline

1. Navigate to Airflow UI (http://localhost:8080)
2. Find the `olympic_master_dag_modular` DAG
3. Toggle it ON (unpause)
4. Click "Trigger DAG" to run manually

### Viewing Results

**Option 1: pgAdmin**
1. Login to pgAdmin (http://localhost:8081)
2. Add server: Host=`postgres`, Port=`5432`, User=`airflow`, Password=`airflow`
3. Query the data:
   ```sql
   SELECT * FROM silver_olympic_events LIMIT 100;
   ```

**Option 2: Docker CLI**
```bash
docker exec -it olympic-data-platform-postgres-1 psql -U airflow
\c airflow
SELECT * FROM silver_olympic_events LIMIT 10;
```

## 📁 Project Structure

```
olympic-data-platform/
│
├── dags/
│   ├── olympic_master_dag.py          # Main Airflow DAG
│   └── modules/
│       ├── __init__.py                # Package initialization
│       ├── extraction.py              # Data validation functions
│       └── transformation.sql         # SQL transformations
│
├── data/
│   └── athlete_events.csv             # Source data
│
├── logs/                              # Airflow execution logs
├── plugins/                           # Custom Airflow plugins
│
├── docker-compose.yml                 # Multi-container setup
└── README.md                          # This file
```

## 🔄 Pipeline Flow

### Task Order
```
install_deps → check_file_exists → load_raw_data → transform_to_silver
```

### Detailed Steps

1. **Install Dependencies** (`BashOperator`)
   - Installs pandas, sqlalchemy, psycopg2-binary in the Airflow container

2. **Check File Exists** (`PythonOperator`)
   - Validates the CSV file is present
   - Logs file size
   - Raises error if missing

3. **Load Raw Data** (`PythonOperator`)
   - Reads CSV using Pandas
   - Creates `raw_athlete_events` table
   - Loads all records into PostgreSQL

4. **Transform to Silver** (`PostgresOperator`)
   - Executes `transformation.sql`
   - Creates `silver_olympic_events` table
   - Cleans data (handles NULLs, standardizes medals)

## 🧪 Data Transformation Logic

The silver layer applies these transformations:
- ✅ Standardized column names (lowercase, descriptive)
- ✅ NULL age values → 0
- ✅ NULL medals → 'No Medal'
- ✅ Type casting and normalization

## 🛑 Stopping the Pipeline

```bash
docker-compose down         # Stop services
docker-compose down -v      # Stop and remove volumes (fresh start)
```

## 📈 Potential Enhancements

- [ ] Add data quality tests (Great Expectations)
- [ ] Implement incremental loading
- [ ] Add Gold layer for aggregated metrics
- [ ] Integrate dbt for transformations
- [ ] Add monitoring with Prometheus/Grafana
- [ ] Implement CI/CD pipeline
- [ ] Add unit tests for extraction modules

## 🤝 Technologies Used

| Category | Technology |
|----------|-----------|
| Orchestration | Apache Airflow 2.7.1 |
| Database | PostgreSQL 13 |
| Data Processing | Python 3, Pandas, SQLAlchemy |
| Containerization | Docker, Docker Compose |
| Database UI | pgAdmin 4 |

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

Created as a demonstration of data engineering skills including ELT pipeline design, workflow orchestration, and containerized infrastructure.

---

**⭐ If you found this project helpful, please give it a star!**
