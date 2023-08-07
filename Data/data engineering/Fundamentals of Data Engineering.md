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
8. Is the storage system schema-agnostic (object storage)? Flexible schema (Cassandra)? Enforced schema (a cloud data warehouse)?
9. How are you tracking master data, golden records data quality, and data lineage for data governance? (We have more to say on these in “Data Management”.)
10. How are you handling regulatory compliance and data sovereignty? for example, can you store your data in certain geographical locations but not others.



understanding data access frequency
data that is most frequently accessed is called hot data.
Lukewarm data might be accessed every so often-say, every week or month
cold data is seldom queried and is appropriate for storing in an archival system.

#### ingestion

the next stage of the data engineering lifecycle is data ingestion from source systems

source systems and ingestion represent the most significant bottlenecks of the data engineering lifecycle. 
1. what are the use cases for the data i am ingesting? can I reuse this data rather than create multiple versions of the same dataset?
2. are the systems generating and ingesting this data reliably, and is the data available when i need it ?
3. what is the data destination after ingestion?
4. how frequntly will I need to access the data ?
5. in what volume will the data typically arrive?
6. what format is the data in ? can my downstream storage and transformation systems handle this format?
7. is the source data in good shape for immediate downstream use? if so, for how long, and what may cause it to be unusable?
8. if the data is from a streaming source, does it need to be transformed before reaching its destination ? would an in-flight transformation be appropriate, where the data is transformed within the stream itself?


batch versus streaming 

batch ingestion is simple a specialized and convenient way of processing this stream in large chunks- for example, handling a full day's worth of data in a single batch.

streaming ingestion allows us to provide data to downstream systems - whether other applications, databases, or analytics systems- in a continuous, real-time fashion.

because of limitation of legacy systems, batch was for a long time the default way to ingest data. batch processing remains an extremely popular way to ingest data for downstream consumption, particularly in analytics and ML.

however, the separation of storage and compute in many systems and the ubiquity of event-streaming and processing platforms make the continuous processing of data streams much more accessible and increasingly popular.the choice largely depends on the use case and expectations for data timeliness.

#### batch vs steam ingestion

1. if I ingest the data in real time, can downstream storage systems handle the rate of data flow?
2. do I need millisecond real-time data ingestion? or would a micro-batch approach work, accumulating and ingesting data, say, every minute?
3. what are my use case for streaming ingestion ? what specific benefits do i realize by implementing streaming? if I get data in real time, what actions can I take on that data that would be an improvement upon batch?
4. will my streaming-first approach cost more in terms of time, money, maintenance, downtime, and opportunity cost than simply doing batch?
5. are my streaming pipeline and ystem reliable and redundant if infrastructure fails?
6. What tools are most appropriate for the use case? Should I use a managed service (Amazon Kinesis, Google Cloud Pub/Sub, Google Cloud Dataflow) or stand up my own instances of Kafka, Flink, Spark, Pulsar, etc.? If I do the latter, who will manage it? What are the costs and trade-offs?
7. if I am deploying an ML model, what benefits do I have with online predictions and possibly contiuous traning?
8. Am I getting data from a live production instance ? if so, what's impact of my ingestion process on this source system?

steaming-firsty might seem like a good idea, but it's not always straightforward

#### push vs pull

in the push modelof data ingestion, a source system writes data out to a target whether a database, object store, or filesystem. In the pull model, data is retrieved from the source system.


#### tranformation

data needs to be changed from its original form into something useful for downstream use cases. without proper transformations, data will sit inert, and not be in a usefyl form for reports, analysis, or ML. Typically, the transformations stage is where data begins to create value for downstream user consumption

1. what's the cost and return on investment(ROI) of the transformation? what is the associated business value?
2. is the transformation as simple and self-isolated as possible?
3. what business rules do the transformations support?


#### Serving Data

1. analytics
it is core of most data endeavors. Once your data is stored and transformed, you are ready to generate reports or dashboards and do ad hoc analysis on the data.
    - Business intelligence
    - Operational analytics
    - Embedded analytics

2. Machine Learning
    - Is the data of sufficient quality to perform reliable feature engineering? Quality requirements and assessments are developed in close collaboration with teams consuming the data.
    - Is the data discoverable? Can data scientists and ML engineers easily find valuable data?
    - Where are the technical and organizational boundaries between data engineering and ML engineering? This organizational question has significant architectural implications.
    - Does the dataset properly represent ground truth? Is it unfairly biased?

3. Reverse ELT


#### Undercurrent across data engineering lifecycle

1. Security

data engineer must  understand both data and access security, exercising the principle of least privilege. it means giving a user or system access to only the essential data and resources to perform an intended function.

People and organizational structure are always the biggest security vulnerabilities in any company. When we hear about major security breaches in the media, it often turns out that someone in the company ignored basic precautions, fell victim to a phishing attack, or otherwise acted irresponsibly. The first line of defense for data security is to create a culture of security that permeates the organization. All individuals who have access to data must understand their responsibility in protecting the company’s sensitive data and its customers.

Data security is also about timing—providing data access to exactly the people and systems that need to access it and only for the duration necessary to perform their work. Data should be protected from unwanted visibility, both in flight and at rest, by using encryption, tokenization, data masking, obfuscation, and simple, robust access controls.


2. Data management

Data management is the development, execution, and supervision of plans, policies, programs, and practices that deliver, control, protect, and enhance the value of data and information assets throughout their lifecycle.


 - Data governance:a business analyst gets a reques for a report but doesn't know what data to use to answer the question.core: discoverability, security, and accountability
  

 - Metadata:business metadata, technical metadata, operational metadata, reference metadata

 - Data accountability:

 - Data quality: accuracy , completeness, timelines

 - Data modeling and design:

 - Data lineage:

 - data integration and interoperability:

 - data lifecycle management:

 - Ethics and privacy: mask personally identifiable information(PII) and other sensitive information, data regulations, such as GDPR, CCPA



3. DataOps

DataOps maps the best practices of Agile methodology, DevOps, and statistical process control to data. Whereas DevOps aims to improve the release and quality of software products, DataOps does the same thing for data products.

- Rapid innovation and experimentation delivering new insights to customers with increasing velocity
- Extremely high data quality and very low error rates
- Collaboration across complex arrays of people, technology, and environments
- Clear measurement, monitoring, and transparency of results


 - Automation
 - Observability and monitoring
 - Incident response
Lean practices (such as lead time reduction and minimizing defects) and the resulting improvements to quality and productivity are things we are glad to see gaining momentum both in software and data operations.

4. Data architecture



5. Orchestration

orchestration systems also build job history capabilities, visulization and alerting, Airflow


6. Software Engineering

- cire data processing code
- development of open source frameworks
- streaming
- Infrastructure as code
- Pipelines as code
- General-purpose problem solving


## designing good data architecture

### principles of good data architecture

#### choose common conponents wisely

#### plan for failure


#### architecture for scalability



#### architecture is leadership

#### always be architecting


#### build loosely coupled systems

systems are broken into many small components, these systems interface with other services through abstraction layers, such as a messageing bus or an API

#### make reversible decisions


#### prioritize seurity


#### embrace finops


## data Generation is source systems

### files and unstructured Data

### APIs

### Application Database(OLTP systems)

online transaction processing system

#### ACID

atomicity, consistency, isolation, and durability

### online analytical processing system


### change data capture

### logs

1. binary-encoded logs
2. semistructured logs
3. plain-text (unstructured) logs

### Database Logs

### CRUD

### Insert-Only

### messages and streams


### types of times

[types of time](../../img/types_of_times.PNG)


### Apis

#### REST api

#### GraphQL

#### Webhooks 