import sublime
import sublime_plugin

class GoToLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Prompt the user to input the line number
        self.view.window().show_input_panel("Go to line:", "", self.on_done, None, None)

    def on_done(self, user_input):
        try:
            line_number = int(user_input) - 1  # Convert to 0-based index
            if line_number >= 0 and line_number < self.view.size():
                self.view.sel().clear()
                self.view.sel().add(self.view.text_point(line_number, 0))
                self.view.show_at_center(self.view.text_point(line_number, 0))
        except ValueError:
            sublime.error_message("Invalid line number")
