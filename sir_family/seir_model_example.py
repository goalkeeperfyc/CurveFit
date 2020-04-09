import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep

# Susceptible 0
# Infected 1
# Exposed 2
# Removed 3

# Network topology
g = nx.erdos_renyi_graph(1000, 0.1)

# Model selection
model = ep.SEIRModel(g)

# Model Configuration
cfg = mc.Configuration()
cfg.add_model_parameter('beta', 0.01)
cfg.add_model_parameter('gamma', 0.005)
cfg.add_model_parameter('alpha', 0.05)
cfg.add_model_parameter("fraction_infected", 0.05)
model.set_initial_status(cfg)

# Simulation execution
iterations = model.iteration_bunch(200)

print(iterations)