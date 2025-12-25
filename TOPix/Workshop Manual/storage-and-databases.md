# Storage and Databases

> Learn about file storage and database options on Replit.

Using Replit's flexible storage solutions, you can quickly add the perfect
data storage your app needs to run. You can use Replit's database or object storage
for apps with the following requirements, and Agent can automatically set up and integrate both solutions:

* A game that needs to save player information such as progress or high scores
* A content platform that manages media files

## What are Replit's storage and database options

Replit offers the following data storage options:

* **Database**: stores structured data such as user profiles, game scores, and product catalogs.
  You can store or retrieve data by attributes and relationships between data points.

* **App Storage**: stores unstructured data such as images, videos, documents.
  You can store and retrieve large files and binary data.

### App Storage and database comparison

|                       | Database                                | App Storage                             |
| --------------------- | :-------------------------------------- | :-------------------------------------- |
| **Ideal data format** | Structured data with relationships      | Large files (images, videos, documents) |
| **Data model**        | Tables, rows, columns                   | Buckets, files                          |
| **Query language**    | SQL                                     | REST API                                |
| **Clients**           | PostgresSQL-compatible clients and ORMs | Replit SDKs and GCS client libraries    |
| **Billing model**     | Pay for compute time and storage space  | Pay for bandwidth and storage space     |

### Workspace tools

Learn more about the following Replit tools to set up and manage your app's data storage:

<CardGroup>
  <Card title="Database" href="/cloud-services/storage-and-databases/sql-database/" icon="database">
    Ideal for structured data and representing data relationships.
    Backed by a fully-managed PostgresSQL database that scales with your app.
  </Card>

  <Card title="App Storage" href="/cloud-services/storage-and-databases/object-storage/" icon="bucket">
    Ideal for unstructured data and large files, such as images, videos, and documents.
    Backed by Google Cloud Storage (GCS) for high availability and scalability. Agent can automatically set up App Storage with advanced authentication and access controls.
  </Card>
</CardGroup>

## Getting started

The quickest way to get started with Replit's storage solutions is to follow one of the tutorials below:

<CardGroup cols={3}>
  <Card title="Database" href="/getting-started/quickstarts/database-connection/" icon="database">
    Connect your app to a SQL database
  </Card>

  <Card title="App Storage in Python" href="/getting-started/quickstarts/object-storage-python/" icon="python">
    Manage App Storage using the Replit Python SDK
  </Card>

  <Card title="App Storage in JavaScript" href="/getting-started/quickstarts/object-storage-javascript/" icon="js">
    Manage App Storage using the Replit JavaScript SDK
  </Card>
</CardGroup>

## Use cases

The following examples show how the database and object storage tools can support your Replit Apps.

### E-commerce app

Store product information, customer profiles, and order history in the database.
Use SQL queries to filter products by category, search for items, and manage customer orders.

<Frame>
  <img src="https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/use-case-ecommerce.jpg?fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=a970847ef9253b625186bf408bde2b7f" alt="screenshot of an E-commerce app" data-og-width="1440" width="1440" data-og-height="872" height="872" data-path="images/databases/use-case-ecommerce.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/use-case-ecommerce.jpg?w=280&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=fa7a3ba735fb4994b04fb31d6c29aaee 280w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/use-case-ecommerce.jpg?w=560&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=46e0efc5e183953c92a012149e8b4fa8 560w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/use-case-ecommerce.jpg?w=840&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=7ca1e8b46ba7a9ea26f1275c341c5371 840w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/use-case-ecommerce.jpg?w=1100&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=fac391285b8d6b4cff8d53c77d5f81f8 1100w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/use-case-ecommerce.jpg?w=1650&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=0377f1616fc7178dff322a815162b922 1650w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/use-case-ecommerce.jpg?w=2500&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=5dba163fccbf233dabddce2fba173468 2500w" />
</Frame>

### File sharing app

Share large files such as images, videos, and documents using App Storage.
Use the Replit App Storage SDK to upload, download, and move files.

<Frame>
  <img src="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/use-case-fileshare.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=2556548039bb1bdfec7ce3bb3df1c9d5" alt="screenshot of a file sharing app" data-og-width="2884" width="2884" data-og-height="1974" height="1974" data-path="images/databases/use-case-fileshare.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/use-case-fileshare.png?w=280&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=c2b2cfe19a9a02b2de97ab128bc0006b 280w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/use-case-fileshare.png?w=560&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=ac06342e0709dff7f65fb9d9f0d82c85 560w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/use-case-fileshare.png?w=840&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=bec52bb816c29a3be415c525a6a735bc 840w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/use-case-fileshare.png?w=1100&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=2a476d0d63799f0100b54f91f809ca2d 1100w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/use-case-fileshare.png?w=1650&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=dc0a093d3c6b19d7bac28c3b56472cb5 1650w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/use-case-fileshare.png?w=2500&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=e4fea50c74ec7d8be6d1a1e691121a18 2500w" />
</Frame>

## Next steps

* [Database](/cloud-services/storage-and-databases/sql-database/): Learn about the database workspace tool and how to connect your Replit App to a database
* [App Storage](/cloud-services/storage-and-databases/object-storage/): Learn how to use Replit's App Storage solution


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.replit.com/llms.txt