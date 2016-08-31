Slasher
=======

A Slack bot that sends random gifs to a channel.

* Author: Julien CHAUMONT (https://julienc.io)
* Version: 1.0
* Date: 2016-08-31
* Licence: MIT
* Url: http://github.com/julienc91/slasher

Description
-----------

This is a very poorly designed Slack bot that simply sends random gifs to a channel. Feel free to consider this stupid project as a quick overview of Slack and Giphy's APIs.


Installation
------------

Clone the repository, install the dependencies and tweak the `config.py` file at your convenience.

    git clone https://github.com/julienc91/slasher
    cd slasher
    pip install -r requirements.txt

Then simply run `slasher.py` to send a random gif according to the configuration you set.

    python3 slasher.py

You might also want to run Slasher via a crontab entry to send new images every day or every hour for instance.
