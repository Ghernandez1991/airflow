#!/bin/bash

main(){

#main script is executed when the single container image is run and acts as entrypoint to container
airflow db migrate
airflow triggerer &
airflow dag-processor &
airflow scheduler &
airflow api-server --port 8080

}
main