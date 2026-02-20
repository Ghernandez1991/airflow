
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

    User a1@-->|Access UI via exposed port| WS
    a1@{ animate: true }
    WS b1@-->|Gets task and dag state| DB
    b1@{ animate: true }
    SCH c1@<-->|Determine if a task is runnable| DB
    c1@{ animate: true }
    SCH d1@-->|Reads DAGs /opt/airflow/dags| DAGs
    d1@{ animate: true }
    SCH e1@-->|Queues Tasks| EXEC
    e1@{ animate: true }
    EXEC f1@-->|Runs Tasks via Fork| FORK
    f1@{ animate: true }
    FORK g1@--> |Updates Status in DB| DB
    g1@{ animate: true }

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