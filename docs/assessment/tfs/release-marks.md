---
tags:
    - Key guide - admin
    - Assessment
    - Ultra
---

# TFS & E:Vision: release feedback & marks
!!! Summary

    **Administrator guide**: the process for releasing feedback with Turnitin Feedback Studio (TFS) and releasing marks on E:Vision

## Overview of process

Once the marking/moderation staff have confirmed that marking is complete, feedback has been given and final marks have been agreed, admin staff take over again to release feedback and marks to students. 

The suggested process for this is:

<!-- Guide to diagram: https://squidfunk.github.io/mkdocs-material/reference/diagrams/ -->
``` mermaid
flowchart TB
    accTitle: Process to release feedback & marks
    accDescr {
        1. Marking team: marks & feedback complete, handover to admin staff
        2. Review agreed marks and apply late penalties
        3. TFS: Update marks & feedback
        4. E:Vision: Assign non-standard grades
        5. E:Vision: Upload marks
        6. Ready for release
        7. TFS: Release feedback
        8. E:Vision: Release marks
    }

    id1(Marking team: marks & feedback complete) --> |handover to admin staff|id2(Review agreed marks and apply late penalties)
    id3[TFS: Update marks & feedback]
    id4[E:Vision: Assign non-standard grades]
    id2 ---> id3
    id2 --> id4
    id4 --> id5[E:Vision: Upload marks]
    id3 ---> id6(Ready for release)
    id5 --> id6
    id6 --> id7[TFS: Release feedback]
    id6 --> id8[E:Vision: Release marks]
```
**Note**: There are also considerations for managing extensions and late submissions.

## In-depth guide

A detailed walk through of this process is given in our [guide to releasing feedback and marks in TFS [Google Doc]](https://docs.google.com/document/d/1vFc560KVNJGQDmlV8mE4HKsPTtVHtwoth1tLFwD6LT0/edit?usp=sharing).

This is aimed at workflows using the Assessment Tracker, but the same process can be used without the Tracker.