# Family Relationship Chatbot (Python & Prolog)

## Overview
A conversational **expert system prototype** that understands and reasons about family relationships. Built with **Python** as the front-end interface and **Prolog** as the logical inference engine, the chatbot can learn new facts from user statements and answer complex relational questions through logical deduction.

This project demonstrates the integration of **symbolic logic** with **procedural programming** to manage a dynamic and consistent knowledge base.

## Features

- **Statement Processing**  
  Accepts declarative facts (e.g., *"John is the father of Mary."*) and updates the knowledge base in real time.

- **Inference Queries**  
  Answers relational questions (e.g., *"Who are the siblings of Mary?"*) by traversing and inferring from stored logical rules.

- **Consistency Validation**  
  Prevents logical contradictions such as circular parentage, gender conflicts, or a person being their own relative.

- **Broad Relationship Support**  
  Handles primitive predicates (`parent`, `male`, `female`) and derived relationships such as `sibling`, `grandparent`, `aunt/uncle`, and `niece/nephew`.

- **Dynamic Assertions**  
  Uses the **PySwip** library to inject new predicates into the Prolog engine at runtime without restarting the system.

## Supported Input Patterns

The chatbot recognizes structured natural language patterns for both learning and querying:

### Statements
- `"X is the mother of Y."`
- `"X and Y are siblings."`
- `"X, Y and Z are children of W."`

### Questions
- `"Are X and Y siblings?"`
- `"Who is the father of X?"`
- `"Is X an aunt of Y?"`

## Technical Specifications

- **Language**: Python 3.x  
- **Logic Engine**: SWI-Prolog  
- **Interface Library**: PySwip  
- **Platform**: Terminal / Command Line (via `chatbot.bat`)  

## Project Context
This project was developed for **CSINTSY – Introduction to Intelligent Systems** at De La Salle University as Major Course Output 2 (MCO2).

It focuses on:
- Designing and evaluating an expert system prototype  
- Representing facts and rules using logic programming  
- Implementing inference mechanisms to derive new knowledge from existing data  

## Design Highlights

- **Decoupled Architecture**  
  Logic is separated into:
  - `statement.py` for processing declarative inputs  
  - `question.py` for handling inference queries  
  - `util.py` for shared Prolog interaction utilities  

- **Knowledge Representation**  
  Complex relationships (e.g., `auntle` for aunt/uncle) are derived from fundamental rules defined in `prolog.pl`.

- **Robust Pattern Matching**  
  Structured string parsing maps user input to logical predicates while preserving case sensitivity for proper names.

- **Error Handling & Logical Safety**  
  The chatbot rejects invalid statements and responds with **"That's impossible!"** when an input violates logical consistency.
