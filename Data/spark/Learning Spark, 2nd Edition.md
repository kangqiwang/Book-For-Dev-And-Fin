# Learning Spark, 2nd Edition
this notes has been created based on [Learning Spark, 2nd Edition](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/), thanks the author [Jules S. Damji](https://www.linkedin.com/in/dmatrix/), [brooke wenig](https://brookewenig.com/),[Tathagata Das](https://www.linkedin.com/in/tathadas/),[Denny Lee](https://www.linkedin.com/in/dennyglee/)


## what is apache spark?

is a unified engine designed for large-scale distributed data processing, on premises in data centers or in the cloud.

Spark provides in-memory storage for intermediate computations, making it much faster than hadoop mapreduce. it incorporates libraries with composable APIs for machine learning(MLlib),SQL for interactive queries(Spark SQL), stream processing(structured streaming) for interacting with real-time data, and graph processing(GraphX)

1. speed
2. ease of use
3. modularity
4. extensibility

Spark Components:
1. Spark SQL
2. Spark Steaming
3. GraphX
4. Spark MLlib

### Spark SQL

```Java
// In Scala
// Read data off Amazon S3 bucket into a Spark DataFrame
spark.read.json("s3://apache_spark/data/committers.json")
  .createOrReplaceTempView("committers")
// Issue a SQL query and return the result as a Spark DataFrame
val results = spark.sql("""SELECT name, org, module, release, num_commits
    FROM committers WHERE module = 'mllib' AND num_commits > 10
    ORDER BY num_commits DESC""")
```

### Spark MLlib

```python
# In Python
from pyspark.ml.classification import LogisticRegression

training = spark.read.csv("s3://...")
test = spark.read.csv("s3://...")

# Load training data
lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)

# Fit the model
lrModel = lr.fit(training)

# Predict
lrModel.transform(test)

```

### Spark Structured Steaming

```python
# In Python
# Read a stream from a local host
from pyspark.sql.functions import explode, split
lines = (spark 
  .readStream
  .format("socket")
  .option("host", "localhost")
  .option("port", 9999)
  .load())

# Perform transformation
# Split the lines into words
words = lines.select(explode(split(lines.value, " ")).alias("word"))

# Generate running word count
word_counts = words.groupBy("word").count()

# Write out to the stream to Kafka
query = (word_counts
  .writeStream 
  .format("kafka") 
  .option("topic", "output"))


```

### GrahpX

graphx is for a a library for manipulating graphs(e.g sicuak network graphs, routes and connection points)


## Apache spark distributed execution

### spark driver

### sparkSession

### Cluster manager

### Spark executor

### Deployment modes

### distributed data and partitions


## Who use Spark

### Data Science tasks


### Data Engineering tasks

data engineers use spark because it provides a simple way to paralleize computations and hides all the complexity of distribution and fault tolerance. This leaves them free to focus on using high-level dataframe-based APIs and domain-specifice language(DSL) queries to do ETL, reading and combining data from multiple sources.

## pop Spark use cases
1. processing in parallel large data sets distributed across a cluster
2. Performing ad hoc or interactive queries to explore and visualize data sets
3. Building, training, and evaluating machine learning models using MLlib
4. Implementing end-to-end data pipelines from myriad streams of data
5. Analyzing graph data sets and social networks


## Understanding Spark Application Concepts

1. Aplication

a user program built on Spark using its APIs. it consists of a driver program and executors on the cluster

2. SparkSession

An Object that provides a point of entry to interact with underlying spark functionality and allows programming spark with its APIs. In an interactive Spark shell, the Spark driver instantiates a SparkSession for you, while in a Spark application, you create a SparkSession object yourself.

3. job

A parallel computation consisting of multiple tasks that gets spawned in response to a Spark action (e.g., save(), collect()).

4. Stage

Each job gets divided into smaller sets of tasks called stages that depend on each other.

5. Task

A single unit of work or execution will be sent to a Spark executor.





