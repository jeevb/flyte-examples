FROM apache/spark-py:v3.4.0

ENV PYTHONPATH /root
WORKDIR /root

USER root

# Hadoop
ADD https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-common/3.3.4/hadoop-common-3.3.4.jar ${SPARK_HOME}/jars

# S3
ADD https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar ${SPARK_HOME}/jars
ADD https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar ${SPARK_HOME}/jars

# Google Cloud Storage
ADD https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/download/v2.2.18/gcs-connector-hadoop3-2.2.18-shaded.jar ${SPARK_HOME}/jars

# Azure Blob Storage
ADD https://repo1.maven.org/maven2/com/microsoft/azure/azure-storage/7.0.1/azure-storage-7.0.1.jar ${SPARK_HOME}/jars
ADD https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-azure/3.3.4/hadoop-azure-3.3.4.jar ${SPARK_HOME}/jars

RUN pip install flytekit flytekitplugins-spark

COPY wf.py /root/

RUN chown -R ${spark_uid}:${spark_uid} /root
USER ${spark_uid}
