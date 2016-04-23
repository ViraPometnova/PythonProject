# Utility for working with windows.
class WindowManager(object):
    def __init__(self, driver):
        self.driver = driver

    def switch_to_last_opened_window(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)

    def close_all_windows(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            self.driver.close()
