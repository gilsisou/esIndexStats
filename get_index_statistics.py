from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
from datetime import datetime


def get_index_statistics(es, index_name):
    all_index_info = es.indices.stats(index=index_name)
    relevant_index_info = {
        "index_name": index_name,
        "number_of_shards": all_index_info["_shards"]["total"],
        "number_of_primaries_documents": all_index_info["_all"]["primaries"]["docs"]["count"],
        "number_of_total_documents": all_index_info["_all"]["total"]["docs"]["count"],
        "total_index_size_in_bytes": all_index_info["_all"]["total"]["store"]["size_in_bytes"]
    }
    print(relevant_index_info)


es = Elasticsearch(hosts=['localhost'], port=9200, http_auth=('elastic', 'changeme'))
index_name = "daily_news-{}".format(datetime.today().date())
try:
    get_index_statistics(es, index_name=index_name)
except NotFoundError as e:
    print(f"ERROR: The index {index_name} is not exists yet, insert data and try again")
