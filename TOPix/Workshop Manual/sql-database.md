# Database

> Replit Database is a SQL database built-in to your Replit App. It allows you to store and retrieve data for your app and users.

export const YouTubeEmbed = ({videoId, title = "YouTube video", startAt}) => {
  if (!videoId) {
    return null;
  }
  let url = "https://www.youtube.com/embed/" + videoId;
  if (startAt) {
    url = url + "?start=" + startAt;
  }
  return <Frame>
      <iframe src={url} title={title} allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>
    </Frame>;
};

Replit Database uses a fully-managed SQL database that lets you add persistent data storage to your Replit App from the Workspace.

<Note>
  The fastest way to get started is to ask **Agent** to add a database to your app. Agent will set up the integration, create the database schema, and update your app to store and retrieve data.
</Note>

<Frame>
  <img src="https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-editor.jpg?fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=18a9293165cc5d42db6c61ea572780d1" alt="screenshot of the database editor" data-og-width="1389" width="1389" data-og-height="871" height="871" data-path="images/databases/database-editor.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-editor.jpg?w=280&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=e0a3605b1dc65f59835c8ae679bedf19 280w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-editor.jpg?w=560&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=234edd06bfd92bec78056c4b19f7155f 560w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-editor.jpg?w=840&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=8916f9b91cab6a9f611a14a1f6637500 840w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-editor.jpg?w=1100&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=b379169990c261ced1a7b928546c3716 1100w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-editor.jpg?w=1650&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=3df79e6935801081074215c456d0e537 1650w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-editor.jpg?w=2500&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=8e0a70842ab956a1a2121d476c299ac4 2500w" />
</Frame>

## Features

The Replit Database tool provides the following features:

* **Database tools**: Run queries, manage database schema, and visualize data with the built-in SQL tools
* **Time travel**: Restore your database to any **Agent** checkpoint using the [rollback feature](/replitai/checkpoints-and-rollbacks/)
* **Free storage**: Includes 10GB of free storage for every Replit App.
* **Environment variables**: Use environment variables in your Replit App to securely access the database

<Info>
  Prior to December 4th, 2025, the development database was hosted on Neon and has a few crucial differences.
  See the [Legacy Neon Development Database](#legacy-development-database) section for more details.
</Info>

## Usage

<YouTubeEmbed videoId="zbyRuoPNIc8" />

You can access the Replit Database tool directly in your Replit App Workspace.
The following sections guide you through setting up and managing your Database.

<Accordion title="How to access the Replit Database tool">
  From the left **Tool dock**:

  1. Select <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5b2c72713cc17ac272098bcbfd624d84" alt="All tools icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/workspace-all-tools-button.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=284639f38f8e91da05d14611e44a9ae6 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d0e802a9c50a81e5c825cf1ddce00a64 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=b5c4e38a7cf923221d2412e904bbdc94 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3b43a87adf314fbb300376b404ab8a22 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a11f8a405c4156ff625219a372c2ceca 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=7c86d2f1bfa4611aeca168daf29d08ff 2500w" /> **All tools** to see a list of workspace tools.
  2. Select <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3cf383ef9ff4e8b5bad4792121dd6769" alt="PostgresSQL database icon" data-og-width="24" width="24" data-og-height="24" height="24" data-path="images/icons/postgres.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=17b80617d665ef3812021c0fdb3b43cf 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=10bdd7a13380255ddf3af617d08c9220 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a5cacd83bc584eca88ddf943cc98b52f 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=cfa8597cf0b3622644faedce574dae7d 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5cf63513422bdc89684306e71bc0d267 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=14b4db671a736545614e0140edff2fdd 2500w" /> **Database**.

  From the **Search bar**:

  1. Select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4a0eb8f6b17ff6761d53167334a68b30" alt="magnifying glass icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/workspace-search-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=baa20919b2c8e7db2fad2562c732edd0 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5fcfa3935da89ed6c1c6f893998c4f4a 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=2a24f3fcc4dd990d9062598eab165cff 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a3258e068d5ead6bacadcbe6e5785575 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d08ebecb3063ed18a657beb563ac9c3c 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e63dd2009929a4b375b86e44ed6d7732 2500w" /> magnifying glass at the top to open the search tool
  2. Type "Replit Database" to locate the tool and select it from the results.
</Accordion>

### Add a database

All Replit Apps come with a database by default. You can access it by selecting the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3cf383ef9ff4e8b5bad4792121dd6769" alt="PostgresSQL database icon" data-og-width="24" width="24" data-og-height="24" height="24" data-path="images/icons/postgres.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=17b80617d665ef3812021c0fdb3b43cf 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=10bdd7a13380255ddf3af617d08c9220 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a5cacd83bc584eca88ddf943cc98b52f 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=cfa8597cf0b3622644faedce574dae7d 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5cf63513422bdc89684306e71bc0d267 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=14b4db671a736545614e0140edff2fdd 2500w" /> **Database** tool in your workspace.

You can integrate the database with your Replit App by asking the **Agent** to add a PostgreSQL database to your Replit App,
including details on what data your Replit App should store. The Agent will create the database schema
and update your app to communicate with the database.

### Restore your database to a previous state

You can revert your app and database to a previous state using the [rollback feature](/replitai/checkpoints-and-rollbacks/).
This feature allows you to restore your database to any checkpoint created by **Agent** or **Assistant**.

<Frame>
  <img src="https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/replitai/checkpoint-rollback.png?fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=f9594eb28458309b2759e8698b8535ce" alt="Checkpoint rollback interface showing rollback options" data-og-width="3154" width="3154" data-og-height="2366" height="2366" data-path="images/replitai/checkpoint-rollback.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/replitai/checkpoint-rollback.png?w=280&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=112089f863c2158c488149819567b671 280w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/replitai/checkpoint-rollback.png?w=560&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=a71d2a32088a71dcfeadb3efb580ace3 560w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/replitai/checkpoint-rollback.png?w=840&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=919aea71632283d5991940a4915a0e13 840w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/replitai/checkpoint-rollback.png?w=1100&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=3f8a002c4b552d8676a3c6689f4b4db2 1100w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/replitai/checkpoint-rollback.png?w=1650&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=82ed52eecc051fb414eeab474e5da5f1 1650w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/replitai/checkpoint-rollback.png?w=2500&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=8ea66e449ef9f90db03a323c8741caab 2500w" />
</Frame>

<Info>
  Make sure to select "Database" under "Additional rollback options" when restoring to the state of a checkpoint. This will restore your database to the state it was at the time of the checkpoint.
</Info>

### Run database commands

The SQL runner is a Workspace tool that lets you run SQL commands on your database and view the results.

<Accordion title="How to access SQL runner">
  From the **Replit Database** tool:

  1. Select the **My Data** tab
  2. Select <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-runner-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4f2e172b249503888506d56a5f7ba6b8" alt="SQL runner icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/sql-runner-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-runner-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=cea74a96d54872b6fca9a0e2894fa758 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-runner-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=7938d3c944b60a72ac89b2ee545627bb 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-runner-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=76c11cfa82562777d3d6fd6caac08b90 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-runner-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d85752c4c2569041cfa4d5a74f71aa26 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-runner-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=801bbcdcf3475a4f95c7fb7ab674e7d3 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-runner-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5d63171cf521aa1938952f3a7571765b 2500w" /> **SQL runner**
</Accordion>

To run a query, enter the SQL statement in the text area and select the
adjacent <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-play.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=09a71d59110569ebe7d0d4def83e24ac" alt="sql run icon" data-og-width="18" width="18" data-og-height="18" height="18" data-path="images/icons/sql-play.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-play.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=42205b2701320867d3c30bb9470413ee 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-play.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=30ad9ca945dc61541836549ed1dd9fe5 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-play.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=bcd637e207a19d4f546211a6f56c4452 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-play.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=b86f39281a91c06102265a51bf7a8f2e 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-play.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=fbd1089a57f148f2cbe008471bfe0f63 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-play.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=66624797f8cff119e8d719723f80bba7 2500w" /> run button
as shown below:

<Frame>
  <img src="https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/sql-runner-run.jpg?fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=258c6ac51524a21e6a6e2070c7cefd3c" alt="screenshot of the SQL runner and run button" data-og-width="1390" width="1390" data-og-height="608" height="608" data-path="images/databases/sql-runner-run.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/sql-runner-run.jpg?w=280&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=13c7b714530562a85b601ce81f4f9ede 280w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/sql-runner-run.jpg?w=560&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=739541a9e147fa3ccc81698da03a17a5 560w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/sql-runner-run.jpg?w=840&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=154f61e3fade1f0bd9efc77a8637ac75 840w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/sql-runner-run.jpg?w=1100&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=606a4e0474ce23f94ad18a35074d194a 1100w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/sql-runner-run.jpg?w=1650&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=0c0a6e2a77dc41290ea472b076e4d774 1650w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/sql-runner-run.jpg?w=2500&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=64843bada9d59d6edd02921b4b4b352b 2500w" />
</Frame>

### Browse and modify data visually

The Replit Database tool includes <a href="https://orm.drizzle.team/drizzle-studio/overview" target="_blank">Drizzle Studio</a>,
a tool that lets you browse and modify data visually.

These visual tools help you avoid syntax errors and offer the following functionality:

* Filter and sort data to focus on specific information
* Export data to a file for external use
* Insert or modify row data
* Create and manage schema, tables, views, and enums

You can access these tools in the **My Data** tab in the **Replit Database** tool.

The following image shows a view from the Drizzle Studio builder interface:

<Frame>
  <img src="https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-editor.jpg?fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=18a9293165cc5d42db6c61ea572780d1" alt="image of the table structure editor" data-og-width="1389" width="1389" data-og-height="871" height="871" data-path="images/databases/database-editor.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-editor.jpg?w=280&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=e0a3605b1dc65f59835c8ae679bedf19 280w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-editor.jpg?w=560&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=234edd06bfd92bec78056c4b19f7155f 560w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-editor.jpg?w=840&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=8916f9b91cab6a9f611a14a1f6637500 840w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-editor.jpg?w=1100&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=b379169990c261ced1a7b928546c3716 1100w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-editor.jpg?w=1650&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=3df79e6935801081074215c456d0e537 1650w, https://mintcdn.com/replit/tlGd6oyGOaUUeRxr/images/databases/database-editor.jpg?w=2500&fit=max&auto=format&n=tlGd6oyGOaUUeRxr&q=85&s=8e0a70842ab956a1a2121d476c299ac4 2500w" />
</Frame>

<Tip>
  You can connect to your database using any PostgresSQL-compatible SQL client using the connection string
  found in your [environment variables](#environment-variables).
</Tip>

### View connection credentials and usage

Your database connection credentials are stored as environment variables in your Replit App.
These credentials are used by your app to securely connect to the database and run commands.

<Accordion title="How to access your database connection credentials">
  1. Navigate to the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3cf383ef9ff4e8b5bad4792121dd6769" alt="PostgresSQL database icon" data-og-width="24" width="24" data-og-height="24" height="24" data-path="images/icons/postgres.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=17b80617d665ef3812021c0fdb3b43cf 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=10bdd7a13380255ddf3af617d08c9220 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a5cacd83bc584eca88ddf943cc98b52f 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=cfa8597cf0b3622644faedce574dae7d 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5cf63513422bdc89684306e71bc0d267 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=14b4db671a736545614e0140edff2fdd 2500w" /> **Replit Database** tool in your workspace
  2. Select either the Development or Production database
  3. Select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=39c5a0a4872b7416378ddad9f2bef608" alt="gear icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/settings-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e0a36e6a9a2078c02467d2abf0b8ba9e 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3be97f139b63f478d536ccaa51518c9a 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4eba230fefbe9836ffd37672275aa7d1 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=97e5099639faf4a5490d8e000c00149a 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4d9552209cee3306d2bc2a02e747ecb6 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d84a81284c0c9af295e0b86273d5c291 2500w" /> **Settings** tab (the gear icon). This tab shows the connection credentials and storage usage for your database.
</Accordion>

#### Environment variables

The following environment variables are available:

* `DATABASE_URL`: how to connect and authenticate to the database
* `PGHOST`: database hostname
* `PGUSER`: database username
* `PGPASSWORD`: database password
* `PGDATABASE`: database name
* `PGPORT`: database port

This `DATABASE_URL` can only be used by your app and even if leaked, it cannot be used by anyone else to access and modify your database.

To learn how to use these credentials in your code, see [Connect your app to a SQL database](/getting-started/quickstarts/database-connection/).

<Info>
  Because this `DATABASE_URL` is scoped to your app, your development database cannot be accessed by other apps, even ones you own or external database viewers.
  This separation follows security best practices and prevents unauthorized access to your database.

  If you need multiple Replit Apps to share a single database, you can expose it as a REST API. See the tutorial on [sharing a database across multiple apps](/tutorials/share-database-across-apps) to learn how to set up a secure database API service.
</Info>

<Warning>
  If you are still on the [legacy Neon development database](#legacy-development-database), do not share your `DATABASE_URL`.
  It contains your database credentials which could be used by anyone to access and modify your database.
  Never paste it in public places or support tickets.
</Warning>

### Security features

When you add a database integration using **Agent**, it adds an Object-Relational Mapper (ORM)
that handles all database communications with built-in security.

This ORM layer, combined with Agent's security best practice implementation, protects your app from
exploits through the following features:

* **Schema validation**: Verifies data conforms to expected formats
* **Data sanitization**: Automatically cleans up builder input to prevent SQL injection attacks

## Legacy Development Database

Prior to December 4th, 2025, the development database was hosted on <a href="https://neon.com/" target="_blank">Neon</a>.
This database is now deprecated and all new development databases are hosted on Replit's own database infrastructure.

You can see if your development database is hosted on Neon by checking the `DATABASE_URL` [environment variable](#view-connection-credentials-and-usage).

<Info>
  If `DATABASE_URL` contains `neon.tech/neondb`, then your development database is still hosted on Neon.
  Otherwise if it contains `helium/heliumdb` then your development database is now hosted on Replit.
</Info>

The following are the key differences between the legacy Neon development database and the new Replit development database:

| **Feature**             | **Replit (current)**                                                                                                                                              | **Neon (legacy)**                                                                                                          |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Hosting**             | Hosted on Replit's own infrastructure                                                                                                                             | Hosted on Neon (third-party provider)                                                                                      |
| **Billing**             | Included for free with every Replit App                                                                                                                           | Usage-based billing. See [Publishing and Database Billing](/billing/about-usage-based-billing#databases) for more details. |
| **Restore capability**  | Restore your database to any checkpoint using the [rollback feature](/replitai/checkpoints-and-rollbacks/)                                                        | Point-in-time restore (PITR)—recover to any point within backup retention window.                                          |
| **Connection security** | Only accessible from within your app; never exposed publicly.                                                                                                     | Used a full connection string—if leaked, anyone could access and modify your database.                                     |
| **Remixing behavior**   | [Remixing](/getting-started/quickstarts/remix-an-app) creates a new development database with copied data for isolation and security.                             | Remixing reuses the same database for all copies, so changes in remixes could affect the original app.                     |
| **Database creation**   | Automatically created for each Replit App.                                                                                                                        | Required explicit setup.                                                                                                   |
| **Publishing workflow** | Deploying or publishing requires creating a [production database](/cloud-services/storage-and-databases/production-databases) for isolation between environments. | Development and production shared the same database, so unintended development changes could affect production apps.       |


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.replit.com/llms.txt