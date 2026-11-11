# Module 2 – Design: reference card

One page. Print it. Use it when you write or review a spec. Terms follow [GLOSSARY.md](../GLOSSARY.md).

## The one idea
Agents write code faster than people review it. The leverage moves to the design. A precise spec gives one definition of correct for people and agents.

## Concept: five parts, plus independence
```
concept <Name> [<TypeParam>, ...]   1. name and type parameters
purpose    <one sentence, user's view>   2.
principle  If <actions>, then <result>.  3. becomes acceptance scenarios
state      <what it remembers, abstract>  4.
actions    <action> (<params>)          5.
             requires: <precondition>      usual home of a refusal
             effect:   <change to state>
```
Independence test: no other concept named. This is a criterion every concept must pass, not a sixth part.
A concept is **not** a class, a module, a screen, or a data entity. "User" is usually not a concept.

## Sync
```
sync <Name>
  when  <Concept>.<action> (<args>)
  where <condition>
  then  <OtherConcept>.<action> (<args>)
```
Concepts never call each other. To change behavior, change one sync.

## Five design defects
| Defect | Test question |
|---|---|
| Overloading | Does this concept serve more than one purpose? |
| False convergence | Were two different purposes forced into one concept? |
| Denied purpose | Is the concept used for a purpose it does not serve? |
| Piggybacking | Was a new function added here instead of a new concept? |
| Redundancy | Do two concepts serve the same purpose? |

## LLM-backed action: three parts
- **Contract:** inputs, output type, what is fixed.
- **Quality criterion:** what "good enough" means, as a check. Becomes an eval in Module 3.
- **Failure behavior:** what happens when the check fails.

The model sits inside an action. It is never a concept.

## Refusals
Each refusal has an owner: a precondition or a sync condition. A refusal only in a prompt is not enforced.

## Cost: four questions
1. Model calls per user action? 2. Context per call? 3. Which calls could deterministic code replace? 4. Which calls retry, and how many times?

## Purpose-to-outcome trace
Every Module 1 outcome has a concept. Every concept serves an outcome or has a stated supporting role. Otherwise: gap, or removal candidate.

## Module check
A colleague reads your spec and predicts the behavior in 5 scenarios that you choose. They are correct in at least 4.

**Sources:** Jackson, *The Essence of Software* (2021); [essenceofsoftware.com](https://essenceofsoftware.com/tutorials/concept-basics/); [Meng and Jackson (2025)](https://arxiv.org/abs/2508.14511).
