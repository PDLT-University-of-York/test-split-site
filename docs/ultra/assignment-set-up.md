---
tags:
    - Key guide - admin
    - Assessment
    - Ultra
---

# Assignment: set up

!!! Summary

    Assignment is the built-in assignment submission and marking tool in the Learn Ultra VLE. It is mostly used for formatives, non-anonymous summatives and group assignments.

    This guide covers setting up Assignment submission points, and is aimed at **Administrators** and **Teaching staff**.

!!! principle "Relevant [VLE site design principles](../ultra/site-design-principles.md)"

    - 4.1 Essential: The assessment section contains all information about module assessments.
    - 4.2 Essential: Assessment instructions are clearly labelled and explain the task and requirements.
    - 4.3 Essential: Provide marking criteria or other grading policies showing how work is marked.

![Example Assignment for a formative essay with task instructions](images/assignment-example.png)

## When to use Assignment

Assignment is most suitable for:

- formative and non-anonymous summative assignments
- individual or group assignments
- a range of file types up to 100MB (eg. text documents, slide decks, low res video and audio)

The Assignment tool does techncally allow anonymous submissions, however **we don't recommend using Assignment anonymously** as this:

1. can be turned off with a single button click, and can't be turned back on
2. limits the marking tools and filtering options available
3. makes it very difficult to apply SSP adjustments

If you want to run an anonymous summative assignment, see our [TurnItIn Feedback Studio set up guide](../assessment/tfs/set-up.md).

## Submission points

!!! Warning

    All formal assessment information and submission points (including formative) must be located in the Assessment section of a module site.

- As Ultra Assignments are used for formatives or non-anonymous summatives, submission points can be set up by teaching staff or admins.
- Submission points must appear in the Assessment section of the module site. If desired, a Course Link to the submission point can also be added in a weekly content folder.
- Give clear instructions on the assessment task and requirements, either within the submission point or in its own item also within the Assessment section.
- Marking criteria or grading policies for the assignment must be available or linked within the Assessment section.

### Individual assessment (Formative or non-anonymous summative)

![Decorative](images/assignment-set-up.png)

1. In the **Assessment section**, hover where you want to add the Assignment and click the **purple plus icon**.
2. Select **Assignment**.
3. Add a **title**, set [appropriate **visibility**](../ultra/content-visibility.md) and add **instructions** as text or a file.
4. Click the **cog icon** to set a Due Date (this must be within working hours) and adjust other settings (see below)
5. Click **Save** when finished.

Appropriate settings will depend on your particular assessment, but here are our general recommended settings:

=== "Formative"

    - **Details & Information**
        - set a *Due date* (this must be within working hours) or tick *No due date*
        - leave all other options unticked
    - **Formative Tools**
        - tick *Formative assessment*
        - leave *Display formative label to students* ticked
    - **Marking & Submissions**
        - *Mark category*: in most cases, leave this as Assignment, but you can change to another option (eg. Presentation). This determines the icon shown on the item in the Course Content area and can be used to filter the Gradebook.
        - *Attempts allowed*: set to Unlimited
        - *Attempts to mark*: set to Last attempt
        - *Mark using*: leave as Points or change to Percentage or a qualitative marking schema (eg. Complete/Incomplete)
        - *Maximum points*: leave as 100 or change to another amount. For formative work, that is often '1' to show the work is marked.
        - *Anonymous marking*: not recommended
        - *Evaluation options*: Peer review can't be used with if multiple attempts are allowed
        - *Assessment mark*: in most cases, leave *Post marks automatically* unticked to release marks manually. If this is ticked, marks and feedback are released to students immediately when a mark is entered for a submission; this could be useful to streamline workflow for large cohorts with lots of markers.
    - **Assessment Security**: leave unticked
    - **Additional Tools**
        - *Time limit*: not recommended unless there is a clear pedagogic rationale
        - *Use marking rubric*: if desired, attach a marking rubric to streamlime marking and feedback
        - *Goals & standards*: leave unticked, not used at UoY
        - *Assigned groups*: not relevant to individual assignments
        - *Originality Report*: not recommended for formative work
    - **Description**: if desired, enter a description to show on the item in the Course Content area (ie. students can see this before they open the Assignment).

=== "Non-anonymous summative"

    - **Details & Information**
        - set a *Due date* (this must be within working hours)
        - leave all other options unticked
    - **Formative Tools**
        - leave unticked
    - **Marking & Submissions**
        - *Mark category*: in most cases, leave this as Assignment, but you can change to another option (eg. Presentation). This determines the icon shown on the item in the Course Content area and can be used to filter the Gradebook.
        - *Attempts allowed*: set to Unlimited
        - *Attempts to mark*: set to Last attempt
        - *Mark using*: leave as Points or change to Percentage or a qualitative marking schema (eg. Pass/Fail)
        - *Maximum points*: most likely leave as the default 100
        - *Anonymous marking*: do not use - Assignment can only be used for *non-anonymous* summative assessment
        - *Evaluation options*:
            - Two markers per student: not recommended (ie. every assignment must be second marked)
            - Peer review can't be used with if multiple attempts are allowed
            - Delegated marking: usually not necessary
        - *Assessment mark*: leave *Post marks automatically* unticked to release marks manually once the marking process is complete.
    - **Assessment Security**: leave unticked
    - **Additional Tools**
        - *Time limit*: not recommended unless there is a clear pedagogic rationale
        - *Use marking rubric*: if desired, attach a marking rubric to streamlime marking and feedback
        - *Goals & standards*: not used at UoY
        - *Assigned groups*: not relevant to individual assignments
        - *Originality Report*: not currently recommended
    - **Description**: if desired, enter a description to show on the item in the Course Content area (ie. students can see this before they open the Assignment)

For more detail, see [Staff Help: Ultra Assignment Set Up & Use - Blackboard's Own Guide](https://help.blackboard.com/Learn/Instructor/Ultra/Assignments)

### Group assessment

Assignment can be used with Course Groups to allow a student to transparently make a submission on behalf of the whole group, and for marks and feedback to be released to all group members.

See our [guide to Group Assignments](../ultra/assignment-groups.md) for full details.

!!! Warning
    Files uploaded to Learn VLE sites (eg. PDF or Word documents) are technically accessible to all site users, even if hidden from students in the Course Content area.
    
    When **uploading assessment-related files** where access needs to be limited (eg. assessment briefs or test materials), view and apply [our guidance on Strict File Access Control for Sensitive Files](https://docs.google.com/document/d/1j6g1k2W0Ont1kA8DfSq7VuLYwgIhbDI7vzwd0-tQAaM/edit).