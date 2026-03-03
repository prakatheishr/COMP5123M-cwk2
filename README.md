# COMP5123M-cwk2: Kubernetes VNF Performance Evaluation

## Overview
This project evaluates the performance of a containerised Virtual Network Function (VNF) deployed in:

1. Cloud-like Kubernetes environment
2. Edge-like Kubernetes environment

The same VNF and workload configuration are used to ensure fair comparison.

## Structure

- k8s/        -> Kubernetes manifests
- scripts/    -> Benchmark and metric collection scripts
- results/    -> Raw experimental outputs
- docs/       -> Setup notes and troubleshooting

## Reproducibility

To reproduce experiments:

1. Deploy manifests from k8s/
2. Run benchmark script from scripts/
3. Results will be stored in results/