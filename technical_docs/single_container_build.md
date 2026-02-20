
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

    %% ---- Styling ----
    classDef user fill:#E3F2FD,stroke:#1E88E5,stroke-width:1px,color:#0D47A1;
    classDef airflow fill:#F1F8E9,stroke:#7CB342,stroke-width:1px,color:#33691E;
    classDef db fill:#FFF3E0,stroke:#FB8C00,stroke-width:1px,color:#E65100;
    classDef executor fill:#E8EAF6,stroke:#5C6BC0,stroke-width:1px,color:#1A237E;
    classDef task fill:#FCE4EC,stroke:#D81B60,stroke-width:1px,color:#880E4F;

    class User user;
    class WS,SCH,DAGs airflow;
    class DB db;
    class EXEC executor;
    class FORK task;