# test_echoember.py
"""
Tests for EchoEmber module.
"""

import unittest
from echoember import EchoEmber

class TestEchoEmber(unittest.TestCase):
    """Test cases for EchoEmber class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EchoEmber()
        self.assertIsInstance(instance, EchoEmber)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EchoEmber()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
