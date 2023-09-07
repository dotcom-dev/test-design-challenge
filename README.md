# Test Design Challenge

This challenge is supposed to help you to showcase your aptitude in understanding
real-life challenges in software development, and application of test design 
techniques that would find a fine balance between risk coverage and invested effort.

Please read thoroughly through the problem statement below, keeping in mind that
this description is intentionally incomplete and vague at points. After understanding
the challenge, spend no more than 30 minutes to draft up a proposed design for 
implementing tests for validating the correctness of the system under test.

The challenge does not intend to restrict you in any way in chosing your approach,
tools or event documentation format of your liking. Please keep in mind though that
the output of your work shall be easy to interpret, help others reading follow your
train of thought. The design doesn't need to be complete, perfect, shiny, but should
call out any obvious omissions, uncovered areas, in order to help assess the remaining
risk.

Send your solution to [Marton Cserbak](mailto:cm@onskeskyen.dk).
We're also grateful for any kind of feedback on the challenge, or anything really.

## Problem statement

We have a software system managing the following entities:
 * User accounts
 * Brands (having many Product Lists)
 * Product Lists (belonging to one Brand, having many Product Products)

Each of these entities have various attributes (for example: ID, Name).

### User accounts

User accounts come in 3 flavors:
 * Admin
 * Brand Admin (connected to one Brand)
 * User (not connected to any Brand)

Let's assume the Admin account already exists. Other accounts are created via registration,
and it's Admin assigning the specific roles to newly created accounts.

### Accesses

 * Admin has access to everything, including:
  * Can create, and manage Brands, Product Lists
  * Can create, and manage (grant permissions) to User Accounts
 * Brand admin has admin privileges in the context of their own Brand:
  * Can create, and manage Product Lists
  * Can manage the Brand
 * User has read-only permissions on all of the entities

Your task is to design a set of tests that'd minimize unauthorized access to the entities
in the software system.
