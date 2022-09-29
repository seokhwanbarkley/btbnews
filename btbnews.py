from finnews.client import News

news_client = News()

cnbc_client = news_client.cnbc
cnbc_topn = cnbc_client.investing_feeds(topic = "investing")

cnn_client = news_client.cnn_finance
cnn_topn = cnn_client.markets()

nasdaq_client = news_client.nasdaq
nasdaq_topn = nasdaq_client.investing_feed()

sp_global_client = news_client.sp_global
sp_global_topn = sp_global_client.corporate_news()

wsj_client = news_client.wsj
wsj_topn = wsj_client.market_news()

yahoo_finance_client = news_client.yahoo_finance
yahoo_finance_topn = yahoo_finance_client.news()

f = open("news.txt", "w")

f.write("\nCNBC:\n")
for i in range(len(cnbc_topn)):
    f.write(cnbc_topn[i].get('title', None) + "\n")
    f.write(cnbc_topn[i].get('link', None) + "\n")

f.write("\nCNN:\n")
for i in range(len(cnn_topn)):
    f.write(cnn_topn[i].get('title', None)+ "\n")
    f.write(cnn_topn[i].get('link', None)+ "\n")

f.write("\nNASDAQ:\n")
for i in range(len(nasdaq_topn)):
    f.write(nasdaq_topn[i].get('title', None)+ "\n")
    f.write(nasdaq_topn[i].get('link', None)+ "\n")

f.write("\nS&P GLOBAL:\n")
for i in range(len(sp_global_topn)):
    f.write(sp_global_topn[i].get('title', None)+ "\n")
    f.write(sp_global_topn[i].get('link', None)+ "\n")

f.write("\nWSJ:\n")
for i in range(len(wsj_topn)):
    f.write(wsj_topn[i].get('title', None)+ "\n")
    f.write(wsj_topn[i].get('link', None)+ "\n")

f.write("\nYAHOO FINANCE:\n")
for i in range(len(yahoo_finance_topn)):
    f.write(yahoo_finance_topn[i].get('title', None)+ "\n")
    f.write(yahoo_finance_topn[i].get('link', None)+ "\n")
f.close()

