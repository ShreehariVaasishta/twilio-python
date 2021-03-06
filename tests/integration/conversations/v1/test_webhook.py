# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class WebhookTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.webhooks().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://conversations.twilio.com/v1/Conversations/Webhooks',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "pre_webhook_url": "https://example.com/pre",
                "post_webhook_url": "https://example.com/post",
                "method": "GET",
                "filters": [
                    "onMessageSend",
                    "onConversationUpdated"
                ],
                "target": "webhook",
                "url": "https://conversations.twilio.com/v1/Conversations/Webhooks"
            }
            '''
        ))

        actual = self.client.conversations.v1.webhooks().fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.webhooks().update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://conversations.twilio.com/v1/Conversations/Webhooks',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "pre_webhook_url": "https://example.com/pre",
                "post_webhook_url": "http://example.com/post",
                "method": "GET",
                "filters": [
                    "onConversationUpdated"
                ],
                "target": "webhook",
                "url": "https://conversations.twilio.com/v1/Conversations/Webhooks"
            }
            '''
        ))

        actual = self.client.conversations.v1.webhooks().update()

        self.assertIsNotNone(actual)
