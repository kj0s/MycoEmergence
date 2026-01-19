# Emergent fungi properties

This project explores energy-constrained pathfinding with stochastic branching over a 2D nutrient landscape. A synthetic environment is generated as a grid of nutrient values, and an agent navigates the field by greedily selecting high-value neighboring cells while managing a limited energy budget! 

This was inspired by actual fungal growth mechanisms, particularly how mycelial networks expand through heterogeneous environments. Much like fungal hyphae, the agent prioritises nutrient-rich regions while occasionally branching to probe alternative directions, enabling exploration beyond immediate local optima. Simple local rules like energy accumulation, movement cost, and probabilistic branching, biological mechanisms that are controlled in real fungi as well, give rise to emergent, organic-looking path structures without any global planning or predefined targets.

I wrote a piece about fungal branching in OmniSci Magazine; check it out [here!]([url](https://www.omniscimag.com/issue-8/fungal-pac-man))

Rather than enforcing a single deterministic trajectory, the system introduces controlled randomness (ε-branching), allowing secondary paths to emerge and diverge. This produces a set of branching trajectories that balance exploitation (moving toward high-nutrient regions) and exploration (occasionally deviating from the optimal local choice).

The final visualisation overlays multiple colored paths onto the nutrient grid, revealing how small probabilistic deviations can produce diverse trajectories from identical starting conditions.
