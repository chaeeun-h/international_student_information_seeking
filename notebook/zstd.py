import pandas as pd
import zstandard as zstd
import json

def zstd_reader(path):
    file = open(path, 'rb')
    decompressor = zstd.ZstdDecompressor()
    reader = decompressor.stream_reader(file)
    df = pd.read_csv(reader, delimiter='\t', header = None)
    file.close()
    return df

def unpack_submssion(df):

    columns = ['post_author', 'name','num_comments','post_score', 'title','post_created_utc', 'selftext']
    data = []
    for row in df.iterrows():
        json_data = json.loads(row[1][0])

        author = json_data.get('author', None)
        name = json_data.get('name', None)
        num_comments = json_data.get('num_comments', None)
        score = json_data.get('score', None)
        title = json_data.get('title', None)
        created_utc = pd.to_datetime(json_data.get('created_utc', None), unit='s')
        selftext = json_data.get('selftext', None)

        data.append([author, name, num_comments, score, title, created_utc, selftext])

    new_df = pd.DataFrame(data, columns=columns)

    return new_df

def unpack_comment(df):

    columns = ['comment_score', 'comment_created_utc', 'comment_author', 'id', 'body', 'link_id', 'parent_id']
    data = []
    for row in df.iterrows():
        json_data = json.loads(row[1][0])

        score = json_data.get('score', None)
        created_utc = pd.to_datetime(json_data.get('created_utc', None), unit='s')
        author = json_data.get('author', None)
        id = json_data.get('id', None)
        body = json_data.get('body', None)
        link_id = json_data.get('link_id', None)
        parent_id = json_data.get('parent_id', None)

        data.append([score, created_utc, author, id, body, link_id, parent_id])

    new_df = pd.DataFrame(data, columns=columns)

    return new_df