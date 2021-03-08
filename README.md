# Invoicing POC

This is an implementation of a simple invoicing application. The idea is to test some python frameworks with a project
closer to the real world.

### Badges
[![CircleCI](https://circleci.com/gh/jrdalpra/invoicing-python.svg?style=svg)](https://circleci.com/gh/jrdalpra/invoicing-python.svg)
[![Coverage Status](https://coveralls.io/repos/github/jrdalpra/invoicing-python/badge.svg?branch=main)](https://coveralls.io/github/jrdalpra/invoicing-python?branch=main)


## Business Rules

- TODO the data model
  - Partner: an entity or person that is involved in a commercial transaction
  - Partnership: a commercial relationship between two partners
  - Marketable: anything that we can sell/buy (services, products)
  - Invoice: a commercial document 
     
- TODO rules on how to build an invoice
- TODO modules 
  - core: basic structure that will be shared between all modules
  - invoice: handle the invoicing business rules
  - billing: generate invoices based on different rules for each partnership
  - integration: create an integration layer to allow us to send/receive invoices using different protocols 
  and file formats

## Technical Details

- TODO how to build? 
- TODO how to test?
- TODO how to run locally?
- TODO which frameworks we are using?


## Things I would like to test here
- use MVP approach on any idea I would like to test
- public API with really awesome documentation - easy to any dev to use
- store the data in a NoSQL database (mongodb?)
- use a SSO server like [Keycloak](https://www.keycloak.org/)
- have a clean architecture (as much as possible - balance productivity with clean architecture)
- build good business documentation using markdown and expose this along with the API docs (a unified doc)
- re-use as much as I can existing frameworks
- build an architecture that would allow us to start small and deploy into a single container, but later scale horizontaly
and maybe have several microservices
- really dynamic business rules - different states per
- use containers
- deploy to a cloud provider
- different levels of tests (unit, integration, end-to-end, performance)
- unit tests must be as fast as possible