# Elasticsearch CNN Index Statistics

First of all, make sure you have docker installed in your machine.

Then move to "docker-elk-stack" library and run "docker-compose up -d" to bring up the ELK stack. The python script helps to gather statistics about index called cnn_news_headlines from ElasticSearch like number of shards, documents etc.

Notice you can also access Kibana through the web application on "http://localhost:5601" to query the cluster data  and metadata using the "Dev Tools" under "Management" tab in the menu.

Made by Gil Sisou