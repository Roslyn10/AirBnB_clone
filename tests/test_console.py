#!/usr/bin/python3
"""Defines unittests for console.py"""

import os
import sys
import io import StringIo
import unittest
from unittest.mock import patch


from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for the console"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down test environment"""
        pass

    def test_quit_command(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringI0()) as fake_out:
                self.assertTrue(self.console.onecmd("quit"))
                self.assertEqual(fake_out.getvalue(), "")

    def test_create_command(self):
    """Test create command"""
    with patch('sys.stdout', new=StringI0()) as fake_out:
        self.assertFalse(self.console.onecmd("create"))
        self.assertIn("** class name missing **", fake_out.getvalue())

    def test_show_command(self):
        """Test show command"""
        with patch('sys.stdout', new=StringI0()) as fake_out:
            self.assertFalse(self.console.onecmd("Show"))
            self.assertIN("** class name missing **". fake_out.getvalue())
