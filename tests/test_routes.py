"""Unit tests for the counter service."""
import unittest

from service import app
from service.routes import COUNTERS


class TestCounterService(unittest.TestCase):
    """Test cases for counter routes."""

    def setUp(self):
        COUNTERS.clear()
        self.client = app.test_client()

    def test_index(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_health(self):
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)

    def test_create_counter(self):
        resp = self.client.post("/counters/foo")
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.get_json()["counter"], 0)

    def test_create_duplicate_counter(self):
        self.client.post("/counters/foo")
        resp = self.client.post("/counters/foo")
        self.assertEqual(resp.status_code, 409)

    def test_update_counter(self):
        self.client.post("/counters/foo")
        resp = self.client.put("/counters/foo")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["counter"], 1)

    def test_update_missing_counter(self):
        resp = self.client.put("/counters/nope")
        self.assertEqual(resp.status_code, 404)

    def test_read_counter(self):
        self.client.post("/counters/foo")
        resp = self.client.get("/counters/foo")
        self.assertEqual(resp.status_code, 200)

    def test_read_missing_counter(self):
        resp = self.client.get("/counters/nope")
        self.assertEqual(resp.status_code, 404)
