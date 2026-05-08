import json
import unittest
from tools import example_tool

class TestTools(unittest.TestCase):
    def test_example_tool_success(self):
        args = {"name": "Alice", "message": "Testing 123"}
        response_str = example_tool(args)
        response = json.loads(response_str)
        
        self.assertEqual(response["status"], "success")
        self.assertIn("Alice", response["greeting"])
        self.assertIn("Testing 123", response["greeting"])
        self.assertEqual(response["source"], "example-plugin")

    def test_example_tool_missing_name(self):
        args = {"message": "Should fail"}
        response_str = example_tool(args)
        response = json.loads(response_str)
        
        self.assertIn("error", response)
        self.assertEqual(response["error"], "No name provided")

    def test_example_tool_exception_handling(self):
        # Passing None to get() might cause issues if not handled, 
        # but our code uses .get("name", "").
        # Let's test with something that might trigger the try...except
        args = None 
        # In a real scenario, Hermes always passes a dict, 
        # but good to test robust code.
        try:
            response_str = example_tool(args)
            response = json.loads(response_str)
            self.assertIn("error", response)
        except Exception:
            self.fail("example_tool raised an exception instead of returning a JSON error")

if __name__ == "__main__":
    unittest.main()
