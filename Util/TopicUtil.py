

def flipChannelTopicMap(channelTopicMap):
    topicChannelMap = {}
    for channel in channelTopicMap.keys():
        topicList = channelTopicMap[channel]

        for topic in topicList:
            if(topic in topicChannelMap):
                topicChannelMap[topic].append(channel)
            else:
                topicChannelMap[topic] = [channel]

    return topicChannelMap

