# encoding=utf-8

import stomp
import time
import logging
import sys

logging.basicConfig()


class PythonMQ(object):
    message = []

    def __init__(self):
        pass

    def on_message(self, headers, message):
        PythonMQ.message.append(message)

    def connectMQ(self, ip, port, username, password, destination):

        print("start connect")
        try:
            conn = stomp.Connection10([(ip, int(port))])

            logging.info("ip is %s, port is %d" % (ip, int(port)))
            conn.set_listener('MyListener', PythonMQ())

            conn.start()

            conn.connect(username=username, passcode=password, wait=True)

            # conn.connect(login=username, password=password)
            conn.subscribe(destination)
            time.sleep(1)
        except BaseException as e:
            logging.error("mq error:%s" % e.message)
        finally:
            conn.disconnect()


class MQMessage(object):

    def getMessage(self, ip, port, username, password, destination):
        """

        :param ip: str ip
        :param port: int port
        :param username: str username
        :param password: str password
        :param destination: str destination
        :return: message
        """

        PythonMQ().connectMQ(ip, port, username, password, destination)
        return PythonMQ.message
