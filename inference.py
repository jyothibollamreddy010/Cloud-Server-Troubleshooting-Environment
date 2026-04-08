
from environment import CloudEnv

env = CloudEnv()

state = env.reset()

print("[START]")

done = False

while not done:
    action = "restart"

    state, reward, done = env.step(action)

    print(f"[STEP] State: {state}, Reward: {reward}")

print("[END]")
