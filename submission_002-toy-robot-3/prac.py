  @patch("sys.stdin", StringIO("forward 10"))
    def test_split_command_input(self):
        with patch ("sys.stdout", new=StringIO()) as var:
            robot.split_command_input("forward 10")
            output = var.getvalue().strip()
            self.assertEqual(output, """""")

    @patch("sys.stdin", StringIO("forward 10"))
    def test_valid_command(self):
        with patch ("sys.stdout", new=StringIO()) as var:
            robot.valid_command("forward 10")
            output = var.getvalue().strip()
            self.assertEqual(output, """""")
            
    @patch("sys.stdin", StringIO("el\nreplay"))
    def test_handle_command(self):
        with patch ("sys.stdout", new=StringIO()) as var:
            robot.handle_command("el", "replay")
            output = var.getvalue().strip()
            self.assertEqual(output, """> el replayed 0 commands.
 > el now at position (0,0).""")
            
            
    @patch("sys.stdin", StringIO("forward 10"))
    def test_valid_command(self):
        with patch ("sys.stdout", new=StringIO()) as var:
            robot.valid_command("forward 10")
            output = var.getvalue().strip()
            self.assertEqual(output, """""")