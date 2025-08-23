---
title: "Demo: Pgvector"
description: A vector database implemented using Pgvector and PostgreSQL.
date: 2025-08-20
---

# Terra firma: playing at scale
## My last demo was impressive, but pitiable
For the past year or so, I've been thinking about how People can benefit from LLMs and I've been noodling out a design for sharing context in an interesting way with friends, coworkers, and customers, but I've hardly touched any code that actually does anything interesting with an LLM or any other more typically AI-adjacent construct.

But, just before that, I did a code up quick demo that showed off a simple RAG pipeline.  It worked remarkably well but it was dead simple: a lightweight model, a Chroma vector store, and some custom chunking code.

A few weeks later, I built something similar at work to mine Basecamp conversations for support information.  Again, though just a demo, the results were pretty badass.

## There were some pretty obvious scaling limitations:
* at some point, I figured I'd want to put so much data in the database that it wouldn't fit in memory and Chroma was an in-memory vector database.  I want to see the day when we can search curated libraries that house vast amounts of text, so persistent, non-resident, non-super-expensive storage is crucial.
* the model I chose didn't fit in the VRAM so I had to run it with the CPU which made it pretty slow (but not terrible really)
* it had to download the model every time it ran

## Scoping out the future
I've been eyeing a bunch of answers to the demo's shortcomings.  PostgreSQL is an easy choice if it works since I've been using it for years.  Caching the model is an obvious upgrade too.

Docling was a bit of an unknown, but it performed admirably as did vLLM in a Docker container, once I'd upgraded my drivers to the 580 version.

## This demo
This demo is simply a proof-of-concept that shows off the same sort of RAG pipeline and query solution I'd built in the past, but with some enhancements:
* A PostgreSQL-backed vector index, removing in-memory constraints.
* Docling for cleaner chunking strategies.
* vLLM with model caching, which makes small models easy to run repeatedly.
* A Dockerized GPU environment, which turned out to be easier to configure than in the past.
* EPUB ingestion, Project Gutenberg unlocked!

## Reflections
* Embedding dimensions are strict: mismatches are non-negotiable...it's a choice that's made when the DB table is created.
* Model quality has improved: Qwen 1.5B was unexpectedly strong for its size.
* Search thresholds were surprisingly low: semantic similarity scores were far lower than I expected, making me wonder if it's actually possible to set that as a constant.  it may need to reflect the content somehow.  and the oddly low number also makes me think I should be baking in some sort of full-text search (which happens to be pretty easy with postgresql).

## Closing thoughts
There were no "Eureka!" moments with this demo, but it was pretty easy to get to where all the moving parts were in place and working and the future is bright:
* the AI assistant in PyCharm was super-helpful with some key bits of this effort
* with a vector database that can scale beyond a machine's RAM capacity, a surpisingly capable but smallish model, and some solid caching options with vLLM, it looks like reliable performance on modest hardware is indeed possible

# Additional Notes
THERE ARE NO TESTS!!  HERE BE DRAGONS!  RUN AWAY!
