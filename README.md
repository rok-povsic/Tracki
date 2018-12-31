# Tracki

[![Build Status](https://travis-ci.com/rok-povsic/tracki.svg?branch=master)](https://travis-ci.com/rok-povsic/tracki)

Tracki is a simple time tracker for tracking work-related tasks.

## Architecture

The main point of this project is its architecture which is using the Clean Architecture approach 
following 
[Robert C. Martin](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164) 
and [Sebastian Buczyński](https://cleanarchitecture.io/). Its main benefits are separations of 
concerns where the business logic is at the core layer of the architecture, and things such as a
data storage and the web framework used are details.
 
This allows, for example, to maximize the speed of tests of the core business logic.

> Note: This architecture makes the project "scalable" in terms of code-size/number of features. 
Since the functionality of this project is small at this point, the architecture may seem 
over-engineered.
