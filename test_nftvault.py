# test_nftvault.py
"""
Tests for NFTVault module.
"""

import unittest
from nftvault import NFTVault

class TestNFTVault(unittest.TestCase):
    """Test cases for NFTVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NFTVault()
        self.assertIsInstance(instance, NFTVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NFTVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
