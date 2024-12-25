#!/bin/bash

if [ "$SPARK_MODE" == "master" ]; then
    # Changed from start-master.sh to start-master
    $SPARK_HOME/sbin/start-master.sh --host spark-master
    tail -f ${SPARK_HOME}/logs/spark--org.apache.spark.deploy.master.Master-1-*.out
elif [ "$SPARK_MODE" == "worker" ]; then
    # Changed from start-slave.sh to start-worker
    $SPARK_HOME/sbin/start-worker.sh $SPARK_MASTER_URL
    tail -f ${SPARK_HOME}/logs/spark--org.apache.spark.deploy.worker.Worker-1-*.out
else
    bash
fi
