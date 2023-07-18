# Fundamentals of Data Engineering
this notes has been created based on [Fundamentals of Data Engineering](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/), thanks the author [Joe Reis](https://www.linkedin.com/in/josephreis/) and [Matt Housley](https://www.linkedin.com/in/housleymatthew/)

## Data Engineering Described

1. fistly, data engineering is SQL-focused. The work and primary storage of the data is in relational databases.
2. secondly, data engineering is Big Data-focused. The work and primary storage like Hadoop, Cassandra, and HBase. All of the data processing is done in Big Data framework like MapReduce, Spark, And Flink.


Data engineering is the development, implementation, and maintenance of systems and processes that take in raw data and produce high-quality, consistent information that supports downstream use cases, such as analysis and machine learning. Data engineering is the intersection of security, data management, DataOps, data architecture, orchestration, and software engineering. A data engineer manages the data engineering lifecycle, beginning with getting data from source systems and ending with serving data for use cases, such as analysis or machine learning.





1. generation
2. storage
3. ingestion
4. transformation
5. serving


undercurrents of the data engineering
1. security
2. data management
3. dataOps
4. data architecture
5. Orchestration
6. Software Engineer

languages:
1. SQK
2. Python
3. Java
4. bash

may need to proficiency:
1. R
2. Javascript
3. C++




## the data engineering lifecycle
![Data Engineer Lifecycle](/img/data_engineer_lifecycle.png)

### generation: source systems
a source system is the origin of the data used in the data engineering lifecycle. for example, a source system could be an IoT device, an message queue, or a transactional database. frequency and velocity of the data

#### source system

1. What are the essential characteristics of the data source? Is it an application? A swarm of IoT devices?
2. How is data persisted in the source system? Is data persisted long term, or is it temporary and quickly deleted
3. At what rate is data generated? How many events per second? How many gigabytes per hour
4. What level of consistency can data engineers expect from the output data? If you’re running data-quality checks against the output data, how often do data inconsistencies occur—nulls where they aren’t expected, lousy formatting, etc
5. how often do errors occurs
6. will the data contain duplocates?
7. will some data values arrive late, possibly much later than other messages produced simultaneously?
8. what is the schema of the ingested data ? will data engineers need to join across several tables or even several systems to gete a complete pictire of data?
9. if schema changes ( a new column is added), how is this dealt with and communicated to downstream stakeholders
10. how frequently should data be pulled from the source system
11. For stateful systems (e.g., a database tracking customer account information), is data provided as periodic snapshots or update events from change data capture (CDC)? What’s the logic for how changes are performed, and how are these tracked in the source database?
12. Who/what is the data provider that will transmit the data for downstream consumption?
13. Will reading from a data source impact its performance?
14. Does the source system have upstream data dependencies? What are the characteristics of these upstream systems?
15. Are data-quality checks in place to check for late or missing data?


#### storage

1. Is this storage solution compatible with the architecture’s required write and read speeds?
2. Will storage create a bottleneck for downstream processes?
3. Do you understand how this storage technology works? Are you utilizing the storage system optimally or committing unnatural acts? For instance, are you applying a high rate of random access updates in an object storage system? (This is an antipattern with significant performance overhead.)
4. Will this storage system handle anticipated future scale? You should consider all capacity limits on the storage system: total available storage, read operation rate, write volume, etc
5. Will downstream users and processes be able to retrieve data in the required service-level agreement (SLA)?
6. Are you capturing metadata about schema evolution, data flows, data lineage, and so forth? Metadata has a significant impact on the utility of data. Metadata represents an investment in the future, dramatically enhancing discoverability and institutional knowledge to streamline future projects and architecture changes.
7. Is this a pure storage solution (object storage), or does it support complex query patterns (i.e., a cloud data warehouse)?
8. 




