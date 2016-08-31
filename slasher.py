#!/usr/bin/python3
# -*- coding: utf-8 -*-


import random
import utools.dicts
from http import HTTPStatus
from safygiphy import Giphy
from slackclient import SlackClient

import config


class Slasher:

    def __init__(self):
        self.giphy_client = Giphy()
        self.slack_client = SlackClient(config.SLACK_TOKEN)
        self.giphy_tags = config.GIPHY_TAGS
        
        self.channel = config.SLACK_CHANNEL
        self.username = config.SLACK_USERNAME
        self.user_icon = config.SLACK_USER_EMOJI

    def find_random_image(self):
        
        if not self.giphy_tags:
            raise ValueError("No valid giphy tag available")
            
        tag = random.choice(self.giphy_tags)
        giphy_result = self.giphy_client.random(tag=tag)
        if not giphy_result:
            # temporary unavailable
            return None
            
        status_code = utools.dicts.deep_get(giphy_result, "meta", "status")
        if status_code != HTTPStatus.OK:
            # temporary unavailable
            return None
            
        giphy_url = utools.dicts.deep_get(giphy_result, "data", "image_url")
        if not giphy_url:
            # no result on this tag, remove it from the list of available tags
            self.giphy_tags.remove(tag)
            # and try again with another tag
            return self.find_random_image()
            
        return giphy_url
        
    def send_message(self, content):

        res = self.slack_client.api_call(
            "chat.postMessage",
            channel=self.channel,
            text=content,
            as_user=False,
            username=self.username,
            icon_emoji=self.user_icon
        )
        return res.get("ok")
        
    def main(self):
        random_image = self.find_random_image()
        if not random_image:
            return False
            
        return self.send_message(random_image)


if __name__ == "__main__":
    Slasher().main()

