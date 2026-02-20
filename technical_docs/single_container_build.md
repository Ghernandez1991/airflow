
```mermaid
flowchart TB
    subgraph DockerContainer["Docker Container: 8080"]
        subgraph Airflow["Apache Airflow"]
            WS[Webserver]
            SCH[Scheduler]
            DB[(SQLite)]
            DAGs[Baked-in DAGs in Image]
            EXEC[LocalExecutor]
            FORK[Task Process]
        end
    end

    User -->|Access UI via exposed port| WS
    WS -->|Gets task and dag state| DB
    SCH <-->|Determine if a task is runnable| DB
    SCH -->|Reads DAGs /opt/airflow/dags| DAGs
    SCH -->|Queues Tasks| EXEC
    EXEC -->|Runs Tasks via Fork| FORK
    FORK --> |Updates Status in DB| DB