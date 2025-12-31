#!/bin/bash

main(){


airflow db migrate
airflow triggerer &
airflow dag-processor &
airflow scheduler &
airflow api-server --port 8080

}
main