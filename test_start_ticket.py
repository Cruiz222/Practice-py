import unittest


class TestTicketWorkflow(unittest.TestCase):

    def test_cannot_start_unassigned_ticket(self):
        ticket = {
            "id": "T001",
            "status": "open",
            "assigned_to": None
        }

        with self.assertRaises(ValueError):
            result = start_ticket()

        with self.assertEqual(ticket["status"] == "open")  
        with self.assertEqual(ticket["assigned_to" == None]) 
