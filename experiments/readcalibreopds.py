import feedparser

calibre_url = "http://edwards.hjemme.lan:8080/opds"

feed = feedparser.parse(calibre_url)

print feed.keys()
newest_url = feed.entries[0].links[0].href

newest_feed = feedparser.parse(newest_url)

print newest_feed.keys()
newest_feed_feed_links = newest_feed.feed.links
print newest_feed_feed_links
next_link = newest_feed_feed_links[len(newest_feed_feed_links) - 1]
print next_link
#print newest_feed.entries[9].keys()
#print newest_feed.entries[8]
#print newest_feed.entries[0].links
