import ray
from ray import tune
from ray.rllib.algorithms.ppo import PPOConfig

ray.init(address="auto")

config = (
    PPOConfig()
    .environment(env="CartPole-v1")
    .rollouts(num_rollout_workers=1)
)

tuner = tune.Tuner(
    "PPO",
    run_config=tune.RunConfig(stop={"episode_reward_mean": 195}),
    param_space=config.to_dict()
)

results = tuner.fit()
