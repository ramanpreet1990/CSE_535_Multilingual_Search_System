<p align="center">Information Retrieval</br>Multilingual Search System for Social Network</br>CSE 535 - Fall 2016
==========================================================================================

<p align="center">[![Img_1](https://raw.githubusercontent.com/ramanpreet1990/CSE_535_Multilingual_Search_System/master/Resources/3.png)](https://www.youtube.com/watch?v=t9ZassrDA40&feature=youtu.be)


Goal
------
The goal of this project is to build a multilingual [faceted search](https://en.wikipedia.org/wiki/Faceted_search) system, including a front end that allows users to search and browse multilingual data based on various criteria: topic, location, person, etc.


Projected Design
---------------
![Search_UI_Part_1] (https://cloud.githubusercontent.com/assets/11690982/11394811/63e58d9c-9335-11e5-847c-4d5ef01fafb9.PNG)
![Search_UI_Part_2] (https://cloud.githubusercontent.com/assets/11690982/11394825/750533c0-9335-11e5-975d-607701e41a69.PNG)


Highlights of our Search System
---------------
> - A pure **multilingual faceted search** system
> - Can handle queries in **5 different languages**- English, Russian, German, French and Arabic
> - Based on twitter data corpus with data of around **0.1 million tweets**
> - Data spans more than **120 countries**

#### For detailed design refer below: -</br>
https://github.com/ramanpreet1990/CSE_535_Multilingual_Search_System/blob/master/documents/report.pdf


Components that we implemented
----
### 1. Faceted Search
This option involves leveraging the faceted search capability provided by Solr to allow various types of drill-down. Facets include people, topics, locations etc.

### 2. Cross-Document Analytics 
This option involves computing various analytics that provide insight into the data.

Examples include: volume of tweets by region/topic/hashtag, sentiment analysis, analytics illustrating cultural differences, etc. 

### 3. Cross-Lingual Retrieval/Analysis 
In this option, we demonstrates cross-lingual capabilities. This can take on many aspects: one example involves cross-lingual queries, and automatic translation of resulting foreign language snippets.

For example, a search for a particular individual/place/organization should take place simultaneously in multiple languages –achieved by automatically tagging and normalizing entities across languages. 

### 4. Ranking tweets 
This option involves coming up with a novel ranking algorithm for tweets that balances recency with importance of content when presenting tweets. It could also take into account the popularity of a tweet, or the influence of a person tweeting, the location of the user, their interests etc...

### 5. Graphical Analysis 
This option involves inferring some graphical structure from the tweets, based on entities mentioned, topics discussed etc. Graph structures (or relationships between tweets) could also be inferred through connection of topics reflected in the tweets


References
------
We have taken reference from below sources to design this search system: -</br>
1. [Introduction to Information Retrieval](http://nlp.stanford.edu/IR-book/)</br>
2. [Course by Oresoft LWC](https://www.youtube.com/watch?v=q0srNT_XM_Y&list=PL0ZVw5-GryEkGAQT7lX7oIHqyDPeUyOMQ)
3. [Apache Solr Tutorials](http://lucene.apache.org/solr/quickstart.html)</br>
4. [Apache Solr Wiki](https://wiki.apache.org/solr/FrontPage)</br>
5. [Apache Solr Reference Guide](https://cwiki.apache.org/confluence/display/solr/Apache+Solr+Reference+Guide)

Credits
-------
This project uses below open source api's. We are grateful for their contribution: -

> 1. Language Detection Api of [detectlanguage.com](https://detectlanguage.com/) 
> 2. [Microsoft Bing Language Translation Api](https://github.com/boatmeme/microsoft-translator-java-api)

We also acknowledge and grateful to [**Professor Rohini K. Srihari**](http://www.cedar.buffalo.edu/~rohini/) and TAs [**James Clay**](http://www.cse.buffalo.edu/people/?u=jnclay), [**Nikhil Londhe**](http://www.cse.buffalo.edu/people/?u=nikhillo), [**Chuishi Meng**](http://www.cse.buffalo.edu/people/?u=chuishim) and [**Ruhan Sa**](http://www.cse.buffalo.edu/people/?u=ruhansa) for their continuous support throughout the Course ([**CSE 535**](http://www.cse.buffalo.edu/shared/course.php?e=CSE&n=535&t=Information+Retrieval)) that helped us learn the skills of Information Retrieval and build a Multilingual Search System.


Contributors
---------
Ramanpreet Singh Khinda (rkhinda@buffalo.edu)</br>
[![website](https://raw.githubusercontent.com/ramanpreet1990/CSE_586_Simplified_Amazon_Dynamo/master/Resources/ic_website.png)](https://branded.me/ramanpreet1990)		[![googleplay](https://raw.githubusercontent.com/ramanpreet1990/CSE_586_Simplified_Amazon_Dynamo/master/Resources/ic_google_play.png)](https://play.google.com/store/apps/details?id=suny.buffalo.mis.research&hl=en)		[![twitter](https://raw.githubusercontent.com/ramanpreet1990/CSE_586_Simplified_Amazon_Dynamo/master/Resources/ic_twitter.png)](https://twitter.com/dk_sunny1)		[![linkedin](https://raw.githubusercontent.com/ramanpreet1990/CSE_586_Simplified_Amazon_Dynamo/master/Resources/ic_linkedin.png)](https://www.linkedin.com/in/ramanpreet1990)

[Alexander Simeonov](https://www.linkedin.com/in/agsimeonov) , [Akash Desai](https://www.linkedin.com/in/akash101192) , [Riaz Munshi](https://www.linkedin.com/in/riazmunshi) and [Karanjeet Singh](https://www.linkedin.com/in/karanjeet-singh-34a7836b) 

License
----------
Copyright {2016} 
{Ramanpreet Singh Khinda rkhinda@buffalo.edu, Alexander Simeonov agsimeon@buffalo.edu, Akash Desai akash101192@gmail.com, Riaz Munshi riazmuns@buffalo.edu and Karanjeet Singh karanjee@buffalo.edu} 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
