# Production Databases

> Learn how to safely manage and publish database changes in production environments.

Production databases are dedicated for your live data that powers your published Replit Apps. Unlike development databases where you experiment and build features, production databases keep your real-world data safe while you continue building, ensuring reliability, and performance.

Understanding how to work with production databases is essential for building robust applications that can evolve and scale without disrupting your users.

<Frame>
  <img src="https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/production-databases.jpg?fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=b60de03dc3f59d971894d1795033cc6b" alt="Production database management interface" data-og-width="1080" width="1080" data-og-height="471" height="471" data-path="images/databases/production-databases.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/production-databases.jpg?w=280&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=c7e38f666c10fa4c407c781f7a1915c4 280w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/production-databases.jpg?w=560&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=80be528d28251dbc338094b89adf9ee3 560w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/production-databases.jpg?w=840&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=5487a8c72d065f3521a7c4632b429b9c 840w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/production-databases.jpg?w=1100&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=dc467bfc53651217e7ae1e4b3043432d 1100w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/production-databases.jpg?w=1650&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=0f85a54f7810be6c055a392dbf46bc00 1650w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/production-databases.jpg?w=2500&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=6acdced6010ccf0f3df1ec291998c4d5 2500w" />
</Frame>

## What are Production Databases?

Production databases are the live, operational databases that serve real users and their data. They differ significantly from development databases in several key ways:

### Production vs Development Databases

| Aspect          | Development Database                     | Production Database                                                  |
| --------------- | ---------------------------------------- | -------------------------------------------------------------------- |
| **Purpose**     | Experimentation and feature development  | Serving real users and storing business data                         |
| **Data**        | Test data, dummy records, small datasets | Real user data, business-critical information                        |
| **Performance** | Optimized for development speed          | Optimized for reliability and user experience                        |
| **Changes**     | Frequent schema changes, rapid iteration | Careful, planned changes via data migrations and rollback strategies |
| **Downtime**    | Acceptable during development            | Must be minimized or eliminated                                      |
| **Backup**      | Optional for testing                     | Critical for business continuity                                     |

<Note>
  Agent is not able to modify the production database, this restriction is in place so that your production database stays safe.

  Agent can make edits to your development database. At the time of publishing, any changes you’ve made with the agent to the structure of your development database (i.e. adding and deleting columns / tables) will be applied over to your production database.

  You are manually able to edit your production data at anytime by going to database pane > production database > My data and toggling **Edit**
</Note>

## Database Technology and Infrastructure

Production databases in Replit are built on the same robust foundation as our standard [SQL Database](/cloud-services/storage-and-databases/sql-database) offering. They use PostgreSQL 16 hosted on [Neon](https://neon.tech), providing enterprise-grade reliability and performance.

### Relationship to Replit SQL Database

Production databases share the same core technology stack as Replit's SQL Database:

* **PostgreSQL 16**: Industry-standard relational database with advanced features
* **Neon Infrastructure**: Serverless database platform that provides automatic scaling and cost optimization
* **Built-in Tools**: Access to SQL runner, Drizzle Studio, and visual data management tools
* **Environment Variables**: Secure connection management through automatically generated credentials

<Info>
  For detailed information about database features, connection setup, and
  technical specifications, see the [SQL
  Database](/cloud-services/storage-and-databases/sql-database) documentation.
</Info>

## Making safe changes to your production database

When you publish updates to your Replit App that include database changes, you may encounter scenarios where careful planning is essential to avoid downtime or data loss.

### Non-Backward Compatible Changes

Some database changes can break compatibility with your existing application code. These changes require special handling to ensure smooth deployments.

<Info>
  You may notice a brief downtime for your published app during publishing. This downtime occurs because database changes sometimes require stopping your app temporarily to prevent conflicts and ensure safe updates. Stopping the app during these updates helps protect your data from loss or corruption while the changes are applied.
</Info>

### Common Non-Backward Compatible Changes

The following types of changes typically require careful publishing strategies:

* **Removing database columns** that your application code still references
* **Changing column data types** in ways that existing code cannot handle
* **Adding required fields** without default values to existing tables
* **Renaming tables or columns** that break existing queries
* **Modifying constraints** that could reject existing application logic

## Deployment Previews

Before publishing database changes to production, Replit provides tools to test your changes safely in a preview environment.

A deployment preview is a temporary, isolated copy of your production environment where you can test database changes and application updates before they affect real users.
This preview environment mirrors your production setup but operates independently.
It can help you catch potential issues early and ensure your changes work correctly before going live.

Testing your deployment in the preview environment is crucial for identifying issues before they impact your users. Follow these steps to ensure your database changes work correctly:

**1. Functional Testing**

* Verify that your app still works properly with the database changes applied
* Test all major user flows to ensure functionality remains intact
* Check that data displays correctly after the schema modifications

**2. Data Integrity Verification**

* Confirm that existing data has been properly migrated or transformed
* Verify that new fields contain expected values or appropriate defaults
* Test edge cases where data might not conform to new constraints

**3. Performance Validation**

* Monitor query response times in the preview environment
* Check that new indexes are being used effectively
* Verify that the changes don't introduce performance regressions

## Point-in-time restore

For production databases, you can restore your database to a specific point in time using the point-in-time restore feature.

<Frame>
  <img src="https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-rollbacks.jpg?fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=bef4a8570506fea11823cba941ad89a4" alt="Database rollbacks interface showing rollback options" data-og-width="1082" width="1082" data-og-height="708" height="708" data-path="images/databases/database-rollbacks.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-rollbacks.jpg?w=280&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=daa37d119de0ce38d8d247e43b33d3e4 280w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-rollbacks.jpg?w=560&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=29ec55e03a19ea415ba2a58edc58b724 560w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-rollbacks.jpg?w=840&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=3c2ae1800c15cbdeddea4195f419be3a 840w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-rollbacks.jpg?w=1100&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=58788af843c717bdc0242e7cb6d24812 1100w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-rollbacks.jpg?w=1650&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=7ab7378b89edc366434a6040387b2161 1650w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-rollbacks.jpg?w=2500&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=cbfdefc89e5396e3661ce2fb90888b7e 2500w" />
</Frame>

Note that this will only restore your production database to the state it was at the time of the checkpoint. It will not restore your app to the state it was at the time of the checkpoint.

To restore your app to the state it was at the time of the checkpoint, you will need to roll back to the checkpoint using the [rollback feature](/replitai/checkpoints-and-rollbacks/) and republish your app.

## Billing and resource usage

Production databases are billed based on usage through Neon, a serverless database provider.

Neon's serverless capabilities include the following:

* Zero infrastructure setup or maintenance
* Automatic scaling to handle your usage needs
* Compute time billing only when the database is active

The database enters an idle state after five minutes of inactivity, pausing compute time billing.
It instantly reactivates when it receives a query.

<Tip>
  To learn more about this serverless database technology, see the
  <a href="https://neon.tech/docs/introduction/compute-lifecycle" target="_blank">Neon Compute lifecycle</a> documentation.
</Tip>

Replit provides real-time tracking of your database usage.
You can view the breakdown of compute time and storage usage for the current Replit App
or for each Replit App on your account.

<Accordion title="How to access database usage">
  To view your database compute time and storage usage for the current billing period, follow the steps below:

  From the **Replit Database** tool:

  1. Navigate to the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3cf383ef9ff4e8b5bad4792121dd6769" alt="PostgresSQL database icon" data-og-width="24" width="24" data-og-height="24" height="24" data-path="images/icons/postgres.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=17b80617d665ef3812021c0fdb3b43cf 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=10bdd7a13380255ddf3af617d08c9220 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a5cacd83bc584eca88ddf943cc98b52f 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=cfa8597cf0b3622644faedce574dae7d 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5cf63513422bdc89684306e71bc0d267 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=14b4db671a736545614e0140edff2fdd 2500w" /> **Replit Database** tool in your workspace
  2. In the database dropdown menu, select **Production**
  3. Select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=39c5a0a4872b7416378ddad9f2bef608" alt="gear icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/settings-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e0a36e6a9a2078c02467d2abf0b8ba9e 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3be97f139b63f478d536ccaa51518c9a 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4eba230fefbe9836ffd37672275aa7d1 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=97e5099639faf4a5490d8e000c00149a 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4d9552209cee3306d2bc2a02e747ecb6 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d84a81284c0c9af295e0b86273d5c291 2500w" /> **Settings** tab
  4. The **Storage Used** section shows the total storage used by your database for the current billing period.

  To view for every Replit App on your account from the **Account resource usage** section, follow the steps below:

  1. Select **View account resource limits** to open the **Usage** page
  2. Scroll to **Resource usage** section
  3. Expand the **PostgresSQL Storage** and **PostgresSQL Compute** rows for details on each Replit App
</Accordion>

To learn how Replit charges for database usage, see [Deployments and Database Billing](/billing/about-usage-based-billing#databases).

## Troubleshooting Common Issues

### Publishing Failures

If your publishing fails due to database issues:

1. **Check the publishing logs** for specific error messages about database connectivity or schema conflicts
2. **Verify your database connection credentials** are correct and accessible from the published app environment
3. **Review recent schema changes** for potential conflicts with existing application code
4. **Test your changes in a preview environment** before attempting to republish

## Removing a production database

<Warning>
  The remove action is irreversible after a retention period of 7 days. Make sure to back up any important data before proceeding.
  Databases have a 7 soft delete period where databases can be restored. Reach out to support if you need assistance. After 7 days, the database is hard deleted and will be unrecoverable.
</Warning>

If you no longer need a database for your Replit App, you can remove it and all its data.

<Accordion title="How to remove a database">
  From the **Replit Database** tool:

  1. Select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=39c5a0a4872b7416378ddad9f2bef608" alt="gear icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/settings-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e0a36e6a9a2078c02467d2abf0b8ba9e 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3be97f139b63f478d536ccaa51518c9a 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4eba230fefbe9836ffd37672275aa7d1 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=97e5099639faf4a5490d8e000c00149a 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4d9552209cee3306d2bc2a02e747ecb6 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d84a81284c0c9af295e0b86273d5c291 2500w" /> **Settings** tab
  2. Select **Remove database** and confirm by selecting **Yes, Remove database**
</Accordion>

## Next Steps

To learn more about database management on Replit:

* [SQL Database](/cloud-services/storage-and-databases/sql-database): Learn about Replit's managed PostgreSQL database service
* [Key-Value Store](/cloud-services/storage-and-databases/replit-database): Explore Replit's simple key-value database option
* [Deployments](/cloud-services/deployments/about-deployments): Understand how deployments work with database changes
* [Object Storage](/cloud-services/storage-and-databases/object-storage): Learn about storing files and assets in the cloud


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.replit.com/llms.txt