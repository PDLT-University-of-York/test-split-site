---
tags:
    - Assessment
    - Communication
    - Ultra
---

# Tools for group assignments

!!! Summary 

    Group assignments are best managed using built in Ultra tools. Currently this can only handle non-anonymous group assessment.

## Course Groups & Ultra Assignment

For written or other file-based group assignments, the most suitable tools available are the built-in Ultra **Course Groups** used together with an **Ultra Assignment** submission point set up for group submission:

- Any of the students can submit the final file on behalf of the group.
- All students can view their group's submission, grade and feedback.
- Submissions can be marked directly through the Ultra Gradebook. 

!!! Warning

    Ultra Assignments don't yet support anonymous marking for group submissions, so can only be used for formative or non-anonymous summative work.
    
    Turnitin Feedback Studio can't be used to manage group submissions.


## Process

The process for managing a group assignment is very similar to other written assignment workflows.

As they are formative or non-anonyous, they can be set up by the admin team or module teaching staff (refer to your departmental guidelines).

<!-- Guide to diagram: https://squidfunk.github.io/mkdocs-material/reference/diagrams/ -->
``` mermaid
flowchart TB
    accTitle: Process for managing a group assignment
    accDescr {
        1. Set up: create Course Groups and Ultra assignment group submission point. Release to students
        2. Students: Complete assigment and submit
        3. Marking team grade in Ultra Gradebook
        4. Admin team review and release marks
    }

    subgraph set-up [Set up]
    direction TB
    id1(Set up Course Groups) --> id2(Create Create Ultra Assignment group submission point) 
    id2 --> id3(Release submission point to students)
    end
    subgraph students [Students]
    direction TB
    id4(Complete assignment and submit)
    end
    subgraph marking [Marking & release]
    direction TB
    id5(Marking team: grade assignments in Ultra Gradebook)
    id5 --> id6(Admin team: review and release marks)
    end
    set-up --> students --> marking
```

## Useful guides

See our specific guides for information on managing aspects of the group assignment workflow:

- [Set up Course Groups](../ultra/course-groups.md)
- [Ultra Assignment: set up](../ultra/assignment-set-up.md) (with in-depth guides for setting up formative and summative Group Assignments)
- [Ultra Assignment: marking](../ultra/assignment-marking.md)