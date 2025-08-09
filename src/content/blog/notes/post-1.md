---
title: Invocate
description: I've released a wrapper around invoke that makes namespaces simpler.
date: 2025-08-08
---

I just released [Invocate](https://pypi.org/project/invocate/) which is a
packaged-up version of a wrapper I wrote a while ago to make namespacing with
Invoke tasks a bit easier to work with.

Rather than building complex data structures with Collections, adding decorated
task functions and Collection instances to a hierarchical tree of Collection
objects, Invocate simply adds a _namespace_ parameter to the task decorator and
provides an _invocate_ executable to replace Invoke's _inv_ (or _invoke_).

Not earth-shattering news, but it will make it a lot easier to use than what
I've been doing, which is dragging around a collection of python code outside
of a proper package.
