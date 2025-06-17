import ray

ray.init(address="auto")

print("Connections:")
print(ray.nodes())

print("Resources:")
print(ray.available_resources)
