#!/usr/bin/python

import logging
import ssl
import os
from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout
import time


class ListMessages(ClientXMPP):

    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)
        self.ssl_version = ssl.PROTOCOL_SSLv3
        self.add_event_handler("session_start", self.session_start, threaded=True)
        self.add_event_handler("message", self.message)


    def session_start(self, event):
        self.send_presence(pshow='online')
        self.get_roster()
        # Most get_*/set_* methods from plugins use Iq stanzas, which
        # can generate IqError and IqTimeout exceptions
        #
        # try:
        #     self.get_roster()
        # except IqError as err:
        #     logging.error('There was an error getting the roster')
        #     logging.error(err.iq['error']['condition'])
        #     self.disconnect()
        # except IqTimeout:
        #     logging.error('Server is taking too long to respond')
        #     self.disconnect()

    def message(self, msg):
        now = time.strftime("%H:%M")
        print('({0}) {1[from]}: {1[body]}'.format(now, msg))


if __name__ == '__main__':
    # Ideally use optparse or argparse to get JID,
    # password, and log level.

    #logging.basicConfig(level=logging.OFF,
    #                    format='%(levelname)-8s %(message)s')

    xmpp = ListMessages(os.getenv('XMPP_USER'), os.getenv('XMPP_PASS'))
    xmpp.connect((os.getenv('XMPP_SERVER'), 5223), use_tls=False, use_ssl=True)
    xmpp.process(block=True)