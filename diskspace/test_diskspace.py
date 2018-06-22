import unittest
import subprocess
import os
import diskspace

from diskspace import subprocess_check_output
from diskspace import bytes_to_readable
#from diskspace import du_command

class test(unittest.TestCase):

    def setUp(self):
        self.command = 'du '
        self.abs_directory = os.path.abspath('.')
        self.command += self.abs_directory
        self.path = 'home/teste'

    def test_subprocess_check_output(self):
        result = diskspace.subprocess_check_output(self.command)
        results = subprocess_check_output('du -d 1 {}'.format(self.abs_directory))

        self.assertEqual(result, results)

    def test_bytes_to_readable(self):
        blocks = 100
        result = "50.00Kb"

        self.assertEqual(bytes_to_readable(blocks), result)


        #suite = unittest.TestLoader().loadTestsFromTestCase(TestDiskspaceMethods)
        #unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    unittest.main()
