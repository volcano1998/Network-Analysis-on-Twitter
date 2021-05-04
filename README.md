# Network-Analysis-on-Twitter

Religious right group is known as conservative, and they don’t publicly admit that they have
connection with hate groups or they are influenced by hate group. In this study, we want to measure
the interaction between those groups on Twitter , and prove there exists strong connection between
known hate group and right wings organization.

Specifically, we tagged 21 hate accounts from white nationalist, neo-natzi in SPLC official
website1 and 172 religious right accounts from 4 websites2 . Then we scraped the information of who
follows who on twitter API. After getting the data, I implemented the analysis aiming at answering 4
questions:

### How far away are right accounts from tagged hate accounts in the network?

### Who in right are following tagged hate actively?

### Who in right are being followed by tagged hate passively?

### Who are contributing to the indirect connection between tagged hate and right groups?

After scraping relevant data from twitter, we are able to answer the above questions. The analyzing process in shown in the code.

Here is the structure of the repo:

**-Data**

  here contains all of the data you need for the analysis, since the data is too large, I uploaded the compressed version, you need to uncompress them in your machine.
  
  - 2020-12-31-2021-01-19.zip  the tweets information from 2020-12-31 to 2021-01-19
  - friends.zip the information of who follow who
  - retweet.txt retweet information from 2020-12-31 to 2021-01-19

**-01-Data-scraping**
  here is the code of how I scraped the data through Twitter API, to run the code, you need your own twitter developer account and the tokens.
  
**-02-Data-Analysis**
  here contains the code of all data wrangling, analysis and visualization for answering targeted questions.
