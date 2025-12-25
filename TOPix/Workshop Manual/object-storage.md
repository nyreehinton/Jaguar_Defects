# App Storage

> App Storage is Replit's built-in file storage that lets your app easily host and save uploads like images, videos, and documents.

App Storage is Replit's built-in object storage that lets your app easily host and save uploads like images, videos, and documents.
Buckets are containers for storing objects such as files. They include access policies to limit what actions users or applications can perform on their contents.

<Info>
  We've renamed <strong>Object Storage</strong> to <strong>App Storage</strong>. Functionality has not changes and your existing buckets, permissions, and programmatic access should continue to work.
</Info>

With App Storage, you can build apps like:

* **Photo sharing platforms**: Let builders upload, store, and display images
* **Video streaming services**: Handle video uploads and serve content to viewers
* **Document management systems**: Store and organize builder files with secure access
* **Portfolio sites**: Showcase work with media files that load reliably
* **File backup services**: Provide builders with cloud storage for their important files

<Frame>
  <img src="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/cloud-services/object-storage-overview.jpg?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=c53aad8c878144b598254a49ae090bc2" alt="screenshot of the App Storage tool" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/cloud-services/object-storage-overview.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/cloud-services/object-storage-overview.jpg?w=280&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=97c0caea0cbd56151d07cd72c56ccede 280w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/cloud-services/object-storage-overview.jpg?w=560&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=55734099546f217dc4b6ea0a66bb09bc 560w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/cloud-services/object-storage-overview.jpg?w=840&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=b377c3175946457b8a634ba6245ec5b2 840w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/cloud-services/object-storage-overview.jpg?w=1100&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=9295d6e5141b45c3a90999387701fae5 1100w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/cloud-services/object-storage-overview.jpg?w=1650&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=01d9f6b44434de6ee20d24b5bec4f6da 1650w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/cloud-services/object-storage-overview.jpg?w=2500&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=f70b517f9b336142b9b9c3c73658cd8c 2500w" />
</Frame>

<Note>
  Ask **Agent** to add App Storage to your app with details on what types of files your app should handle. Agent will set up the integration, create the necessary buckets, and update your app to upload, store, and retrieve files with advanced features like authentication and access controls.
</Note>

The App Storage tool lets you seamlessly share data between your
development and production environments or with other Replit Apps.

## Features

<Info>
  App Storage is powered by Google Cloud Storage (GCS).
  This means you receive the benefits of industry-leading uptime,
  availability, and security.
</Info>

App Storage provides the following features for your Replit Apps:

* **Persistent cloud storage**: Store files that remain accessible to your published app and users
* **Scalable file handling**: Handle growing data needs without worrying about storage limits
* **Cross-app data sharing**: Share buckets across multiple Replit Apps for distributed architectures
* **Programmatic access**: Upload, download, and manage files using intuitive APIs
* **Enhanced Agent integration**: Let Agent set up App Storage with advanced configurations, inspect existing setups, and generate complete backend and frontend code with authentication and access controls

Here are a few ways you can use App Storage in your Replit Apps:

* Store builder profile pictures and media uploads
* Serve product images for e-commerce sites
* Handle document uploads for form submissions
* Create file sharing and collaboration features
* Build content management systems with media libraries

<Tip>
  **Enhanced Agent Integration**: You can prompt [Replit Agent](/replitai/agent) to automatically add App Storage to your apps! Agent can now set up object storage, inspect configurations, and generate complete backend and frontend code with advanced features like authentication and access controls. Simply mention "App Storage" or "file storage" in your prompt.

  <AiPrompt>Add App Storage to my app to store files</AiPrompt>
  <AiPrompt>Create a photo gallery app with App Storage for images</AiPrompt>
  <AiPrompt>Set up App Storage with authentication for user file uploads</AiPrompt>

  Learn more about [Agent integrations](/replitai/integrations#data-storage--management) and see all available App Storage prompts.
</Tip>

## Usage

<Note>
  Your Replit App must authenticate with Google Cloud Storage to access a bucket and its objects.
  Use the official Replit App Storage client libraries to automatically authenticate.
</Note>

You can access the App Storage tool directly in your Replit App workspace.

<Accordion title="How to access the App Storage tool">
  From the left **Tool dock**:

  1. Select <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5b2c72713cc17ac272098bcbfd624d84" alt="All tools icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/workspace-all-tools-button.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=284639f38f8e91da05d14611e44a9ae6 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d0e802a9c50a81e5c825cf1ddce00a64 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=b5c4e38a7cf923221d2412e904bbdc94 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3b43a87adf314fbb300376b404ab8a22 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a11f8a405c4156ff625219a372c2ceca 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=7c86d2f1bfa4611aeca168daf29d08ff 2500w" /> **All tools** to see a list of workspace tools.
  2. Select <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/object-storage-monoochrome-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=7f716c0fb01dcca217d1e9c61005e302" alt="App Storage icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/object-storage-monoochrome-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/object-storage-monoochrome-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=1e4c17f4ac3fd4b9bb8ca2a3289af651 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/object-storage-monoochrome-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=ae3f7db6e976d1dc358502e9b2f43626 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/object-storage-monoochrome-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=9cea36b80288f0d790a5408c5f679c9e 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/object-storage-monoochrome-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d3993deecca8670719014ac906a664c6 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/object-storage-monoochrome-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=07871609d691508876e1476057487c75 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/object-storage-monoochrome-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=790323521d9f1b9a581d9cc883457730 2500w" /> **App Storage**.

  From the **Search bar**:

  1. Select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4a0eb8f6b17ff6761d53167334a68b30" alt="magnifying glass icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/workspace-search-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=baa20919b2c8e7db2fad2562c732edd0 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5fcfa3935da89ed6c1c6f893998c4f4a 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=2a24f3fcc4dd990d9062598eab165cff 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a3258e068d5ead6bacadcbe6e5785575 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d08ebecb3063ed18a657beb563ac9c3c 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e63dd2009929a4b375b86e44ed6d7732 2500w" /> magnifying glass at the top to open the search tool.
  2. Type "App Storage" to locate the tool and select it from the results.
</Accordion>

To associate a new storage bucket with your Replit App, create a bucket.

<Accordion title="How to create a bucket">
  From the **App Storage** tool:

  1. Click on **Create new bucket**.
  2. Enter a name for the bucket in the **Name** field and select **Create bucket**.

  The App Storage tab should resemble the following screenshot:

  <Frame>
    <img src="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/object-storage-empty-bucket.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=d3ac92cbf149819e34c5a770bc71401b" alt="screenshot of the App Storage tool" data-og-width="2790" width="2790" data-og-height="1218" height="1218" data-path="images/databases/object-storage-empty-bucket.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/object-storage-empty-bucket.png?w=280&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=dc9fd2ed217f4498a5e12b56540b2b38 280w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/object-storage-empty-bucket.png?w=560&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=71ee2834a884792d4745b5a75c408e2c 560w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/object-storage-empty-bucket.png?w=840&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=0fb2fac760a20aaf8dc5fa77ec72b3c8 840w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/object-storage-empty-bucket.png?w=1100&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=4d7ff4407e92748e22aeb2578d5032c0 1100w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/object-storage-empty-bucket.png?w=1650&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=a54bd8d11432943dc0fc81fe86ab77e2 1650w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/object-storage-empty-bucket.png?w=2500&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=00186e35e89bf0cd272e0889c14c0558 2500w" />
  </Frame>

  To create additional buckets, open the bucket dropdown menu on the top left of the **App Storage** tab and select **Create new bucket**.
</Accordion>

The following sections explain the bucket and object management options in the App Storage tool.

### Select a bucket

To switch between your storage buckets, select the dropdown menu in the top left corner of the **App Storage** tab.

The selected bucket displays a check mark next to its name, as shown in the screenshot below:

<Frame>
  <img src="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/select-bucket.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=e383ae2e2e2c6d4af43922242a6068b8" alt="screenshot of bucket selection menu" data-og-width="1852" width="1852" data-og-height="704" height="704" data-path="images/databases/select-bucket.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/select-bucket.png?w=280&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=40fa6f5da3f97629908161d9967e9b48 280w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/select-bucket.png?w=560&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=44248316943b1cba65055a65e715d995 560w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/select-bucket.png?w=840&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=61f9267a3410917a4ff27a1ff00a3308 840w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/select-bucket.png?w=1100&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=8538fd5847bedf6a6c894682c5cac3fd 1100w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/select-bucket.png?w=1650&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=2739ef07d06af322e4e0f579250f8b10 1650w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/select-bucket.png?w=2500&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=55b2a13cd398499ff2241f80535f56cb 2500w" />
</Frame>

### Access the bucket ID

To view the **Bucket ID** by selecting the **Settings** view from the dropdown at the top of the **App Storage** tab.
The Bucket ID uniquely identifies the bucket, which your code must reference to perform an operation.

If you have multiple buckets, select the correct bucket from the dropdown menu in the top left corner.

The following screenshot shows the Bucket ID for the "FileVault Bucket One" bucket:

<Frame>
  <img src="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/bucket-id.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=dd5593bef5878a96c6972f3cbf94e30d" alt="screenshot of the App Storage tool" data-og-width="1596" width="1596" data-og-height="428" height="428" data-path="images/databases/bucket-id.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/bucket-id.png?w=280&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=afa30b6dbffc46daa893788f55fc3e47 280w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/bucket-id.png?w=560&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=071c3b2064913b494f6cd34dd5269d21 560w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/bucket-id.png?w=840&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=13f8d4338770e7e831bb441213e5bdd9 840w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/bucket-id.png?w=1100&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=465cde0e4319dfabefa3b3ce507688b1 1100w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/bucket-id.png?w=1650&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=2c05333b9ba6fd5a41dc58deb51851ee 1650w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/bucket-id.png?w=2500&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=2b2ccc1f78d5b1016b441392f70166f3 2500w" />
</Frame>

### Upload or download objects

To upload an object to the selected bucket:

1. Navigate to the **Objects** view in the **App Storage** tab.
2. Select <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/upload-file.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=f16946db28550c879305a27e9102b750" alt="upload file icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/upload-file.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/upload-file.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=0fb8bc57a7632c5011d5da707b3055d9 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/upload-file.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=7966c028f0aa95fb28f2cb3e6a8610d4 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/upload-file.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=22edd65a063f25dd3c45acb90d68952b 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/upload-file.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=59efc6728243b7c6e41efc6c2f2cafae 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/upload-file.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=2d3c1c9f6d39031b7a69721fdcdc91c2 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/upload-file.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=032a10ab46150f524a35b1b5c9542844 2500w" /> **Upload files**, or <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/upload-folder.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=15f810db7193eeec2c4de7f2efc305eb" alt="upload folder icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/upload-folder.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/upload-folder.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e33a2219ad6ee3ab3ee44bd9154c66e8 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/upload-folder.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=6c20bfc7987a8027f2050da94749f6c7 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/upload-folder.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=85798cde156cbaee8c799526fbaf361b 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/upload-folder.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=340c3b3c67d1fd618802633daa5a066e 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/upload-folder.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=bb62563ee586795c1cdedc57c8f01128 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/upload-folder.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4f457a93de546cb9ac34e273fc28fd01 2500w" /> **Upload folder** to upload all files from a folder.
   Then, select one or more files to upload from the file dialog.
   Alternatively, drag a file or folder into the area that lists the contents of the bucket.

To download an object from the selected bucket:

1. Navigate to the **Objects** view in the **App Storage** tab.
2. Select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/download-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=29fbdd462761fb2a2180e92a26321128" alt="download icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/download-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/download-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3e89a248c14f84a97da99877c052e26c 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/download-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=ba51d580be445aa39b8dd397e3f08705 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/download-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3b19fd72d2f81fe94c033ce543ec8f67 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/download-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=0c517f0ad96d2637ee472e003345bb4a 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/download-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d6096d896bb5a0247e450116e97c2c76 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/download-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=55ad515faec4c364624d669ad2f44617 2500w" /> download icon to the right of the file to download it.

### Organize objects in folders

To create a folder in the selected bucket:

1. Navigate to the **Objects** view in the **App Storage** tab.
2. Select <img class="icon-svg" src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-folder.svg?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=452199bae3688380c770951c4bd16260" alt="create folder icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/create-folder.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-folder.svg?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=300e99f7b4bd43373babd529e33c40b4 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-folder.svg?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=17a2a1520d878d4dee99f9bb84627755 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-folder.svg?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=1320ad3771e28a6e0647ab53b3afa4f5 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-folder.svg?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=59d0ec19cfca93a6d8c8901b6b261b14 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-folder.svg?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=8e6353198a91c90f8febf4604814ea35 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-folder.svg?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=d06c17193076edef46d32d6c89f33d0e 2500w" /> **Create Folder** in the **Objects** view.
3. Enter a name for the folder.

To add objects to a folder in the **Objects** view, drag an object to the destination folder.

To move the object to a parent folder, drag it above the header to the name of the folder above the object list.
The following animation shows moving the "product\_demo.mov" file from the "videos" folder to the parent "Objects" folder:

<Frame>
  <img src="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/object-move.webp?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=c8a78e46338a230c91fdff178165a39e" alt="animation showing moving a file to a parent folder" data-og-width="800" width="800" data-og-height="440" height="440" data-path="images/databases/object-move.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/object-move.webp?w=280&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=868c2c3d87c0056b2e3be3fa514c36d8 280w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/object-move.webp?w=560&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=88d50dc0a0dd988310f1ebaf19b01b80 560w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/object-move.webp?w=840&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=4012c72ffad0f13b0c729b5373040cc6 840w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/object-move.webp?w=1100&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=9588947080fe6cef102299b7e212cea3 1100w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/object-move.webp?w=1650&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=3e21384c864433621b7c5eacc69389d1 1650w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/object-move.webp?w=2500&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=d5568a10b88c6729d7aa8af84609d97b 2500w" />
</Frame>

### Delete objects or buckets

<Warning>
  The delete action is irreversible. Make sure to back up any essential data before proceeding.
</Warning>

To delete an object forever:

1. Navigate to the **Objects** view in the **App Storage** tab.
2. Select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/trash-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=8f151791088b8b241632ca547f90265e" alt="trash icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/trash-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/trash-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=2623b12e7af8f79729b14508489b0418 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/trash-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=31c030d2861933867568ad11b940a210 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/trash-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d3de8c448b8ab0d7b3bd8978fa346ddb 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/trash-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=70b9aaae5e97d97328752b89a2d6d963 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/trash-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=0d4a3e8a7b503e3fa067daf5d6262b88 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/trash-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3712a7908610fc2a9295f31cd2c5c0c7 2500w" /> trash icon
   next to the object you want to delete.
3. Confirm the deletion in the confirmation dialog.

To delete a bucket and all the objects it contains:

1. Navigate to the **Settings** view in the **App Storage** tab.
2. Make sure you select the bucket you want to delete in the top left bucket dropdown menu.
3. Select <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/trash-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=8f151791088b8b241632ca547f90265e" alt="trash icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/trash-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/trash-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=2623b12e7af8f79729b14508489b0418 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/trash-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=31c030d2861933867568ad11b940a210 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/trash-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d3de8c448b8ab0d7b3bd8978fa346ddb 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/trash-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=70b9aaae5e97d97328752b89a2d6d963 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/trash-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=0d4a3e8a7b503e3fa067daf5d6262b88 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/trash-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3712a7908610fc2a9295f31cd2c5c0c7 2500w" /> **Delete Bucket**.
4. Confirm the deletion in the confirmation dialog.

### Bucket access management

Replit connects all buckets you create to your account and makes them available to
all your Replit Apps. The Replit App from which you create the bucket automatically
receives access.

You can control which of your Replit Apps have access to a specific bucket, which lets you
share data efficiently and securely.

To grant your Replit App access to a bucket from another app on your account:

1. Select <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4a0eb8f6b17ff6761d53167334a68b30" alt="magnifying glass icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/workspace-search-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=baa20919b2c8e7db2fad2562c732edd0 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5fcfa3935da89ed6c1c6f893998c4f4a 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=2a24f3fcc4dd990d9062598eab165cff 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a3258e068d5ead6bacadcbe6e5785575 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d08ebecb3063ed18a657beb563ac9c3c 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e63dd2009929a4b375b86e44ed6d7732 2500w" />
   **Add an existing bucket** from the bucket menu at the top left of the App Storage tab.
2. In the **Choose a Bucket** dialog, choose the bucket you want to add and select **Add Bucket to Repl**.

<Frame>
  <img src="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/choose-bucket-dialog.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=5059d4d2490bbe37db80abdb5ac68d84" alt="screenshot of the choose bucket dialog" data-og-width="1115" width="1115" data-og-height="457" height="457" data-path="images/databases/choose-bucket-dialog.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/choose-bucket-dialog.png?w=280&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=133f517126edf59bad46b5055de78feb 280w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/choose-bucket-dialog.png?w=560&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=b6bb63379c375743fa5decc35af628eb 560w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/choose-bucket-dialog.png?w=840&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=b60e5cc5b13ccdabb18d3d3f94e09a1d 840w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/choose-bucket-dialog.png?w=1100&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=4234989b34d8ebd5439ea120880ec496 1100w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/choose-bucket-dialog.png?w=1650&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=8513c4af88652197747366034b8d98b2 1650w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/choose-bucket-dialog.png?w=2500&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=65071dea1407fe9f96d10ad3f5be1d65 2500w" />
</Frame>

To revoke your Replit App's access to a bucket:

1. Navigate to the **Settings** view in the **App Storage** tab.
2. From the bucket dropdown in the top left of the tab, select the bucket name.
3. Select **Remove Bucket from Repl** and confirm removal in the confirmation dialog.

### Programmatic access to App Storage

To access App Storage from your Replit App, use one of the following libraries:

* Replit App Storage SDK, available for JavaScript and Python
* <a href="https://cloud.google.com/storage/docs/reference/libraries" target="_blank">Google Cloud Storage client library</a>

For instructions on how to use the client libraries, see the following resources:

* [JavaScript App Storage tutorial](/getting-started/quickstarts/object-storage-javascript/): Learn how to use the Replit JavaScript App Storage client
* [JavaScript App Storage SDK](/reference/object-storage-javascript-sdk/): Client reference for the JavaScript SDK
* [Python App Storage tutorial](/getting-started/quickstarts/object-storage-python/): Learn how to use the Replit Python App Storage client
* [Python App Storage SDK](/reference/object-storage-python-sdk/): Client reference for the Python SDK
* [Google Cloud Python SDK example app](https://replit.com/@matt/GCS-Python-Uploads?v=1): Remix this app to manage objects using the Google Cloud Python SDK

## Billing and resource usage

To monitor your App Storage usage, navigate to the <a href="https://replit.com/usage/" target="_blank">Usage</a> page.

To learn more about App Storage pricing, see [App Storage Billing](/billing/object-storage-billing).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.replit.com/llms.txt