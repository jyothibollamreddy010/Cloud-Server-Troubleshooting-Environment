class CloudEnv:
    def __init__(self):
        self.state = "Server Down"
        self.done = False

    def reset(self):
        self.state = "Server Down"
        self.done = False
        return self.state

    def step(self, action):
        if self.done:
            return self.state, 0, True

        if action == "check_logs":
            self.state = "Issue Found"
            return self.state, 0.5, False

        elif action == "restart":
            self.state = "Server Running"
            self.done = True
            return self.state, 1, True

        else:
            return self.state, -1, False
