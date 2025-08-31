---
title: "Demo post-mortem and next steps: GPU/CPU, VRAM and Context Length"
description: Continuing studies in resources vs requirements for Gen AI.
date: 2025-08-30
---
I just finished up a [demo](/posts/notes/post-2-demo-pgvector-2025082001/) that primarily looked at using PostgreSQL as a
vector database to power similarity search for a simple RAG pipeline.  Though
it was very much a success, I hit a couple of issues during implementation that
I want to explore in future demos.

## Reflecting on previous demos
![](images/office_plant_compressed.jpg "I have an office plant now!!")
Running large language models on consumer hardware is an ongoing experiment, and
each trial uncovers something new. My first retrieval-augmented generation demo
used a 7B parameter model but quickly ran into GPU memory limits, forcing me to
run inference on the CPU. That wasn’t the performance boost I had hoped for
after investing in new GPUs, but it confirmed that local LLMs were at least
feasible.

My [most recent demo](/posts/notes/post-2-demo-pgvector-2025082001/) with DeepSeek’s Qwen-1.5B highlighted a different challenge:
RAM exhaustion when multiple models were loaded at once. That limitation came to
light after I realized my singleton was two-timing me, but I'd been kinda
thinking I might fit several of those into VRAM at one time.

I also encountered issues with context length during ingestion, which I solved
by tuning the max_model_len parameter in vLLM. While that fix worked, it raised
a broader question about how advertised context windows relate to configurable
parameters.

## Next demo(s): managing resources
To get a better handle on the gen AI capabilities of consumer-grade hardware, I
want to try:
* to run multiple models at once
* to run with the GPU making use of both VRAM and system DRAM
* to figure out what parameters are required to handle longer context windows
  and to figure out what the memory implications are when scaling these up
