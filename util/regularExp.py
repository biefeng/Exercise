import re

pattern = re.compile('(Query_time: .*?)', re.DOTALL & re.M)

with open(
        r"C:\Users\BieFeNg\Documents\WXWork\1688853141501"
        r"948\Cache\File\2019-08\b9bd1aeae7774f1cb536aef43ba55f08_slowlog_download_20190815082739258") as sql:
    pattern.search()
